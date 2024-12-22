from rest_framework import serializers
from gestiondpi.models import Patient, DPI, Medecin
from authentification.models import User
from authentification.views import AddUserView
from authentification.serializers import UserRegisterSerializer

import qrcode
from io import BytesIO
from django.core.files.base import ContentFile


from io import BytesIO
from django.core.files.base import ContentFile
import qrcode
import uuid  # To ensure a unique filename
from django.db import IntegrityError

class DPICreationSerializer(serializers.Serializer):
    nom_patient = serializers.CharField(max_length=100)
    prenom_patient = serializers.CharField(max_length=100)
    nss = serializers.CharField(max_length=20)
    date_de_naissance = serializers.DateField()
    adresse = serializers.CharField()
    telephone = serializers.CharField(max_length=15)
    mutuelle = serializers.CharField(max_length=100)
    personne_a_contacter = serializers.CharField(max_length=100)
    nom_complet_medecin = serializers.CharField(max_length=200)  # Nom complet du médecin (prénom + nom)
    antecedents = serializers.CharField(allow_blank=True, default="")

    def validate(self, data):
        # Séparer le nom et le prénom du médecin à partir de nom_complet_medecin
        try:
            prenom_medecin, nom_medecin = data['nom_complet_medecin'].split()
        except ValueError:
            raise serializers.ValidationError({"medecin": "Le nom du médecin doit être composé d'un prénom et d'un nom."})

        # Recherche du médecin avec prénom et nom
        try:
            utilisateur_medecin = User.objects.get(
                first_name=prenom_medecin,  # Prénom
                last_name=nom_medecin,      # Nom
                role=User.MEDECIN           # Rôle du médecin
            )
        except User.DoesNotExist:
            raise serializers.ValidationError({"medecin": "Médecin introuvable avec ce nom et prénom."})

        # Ajout du médecin validé au contexte
        data['utilisateur_medecin'] = utilisateur_medecin
        return data

    def create(self, validated_data):
        # Création de l'email patient
        email = f"{validated_data['prenom_patient'].lower()}{validated_data['nom_patient'].lower()}{validated_data['nss']}@gmail.com"
        # Création du mot de passe avec le NSS
        password = validated_data['nss']

        # Créer l'utilisateur patient avec UserRegisterSerializer
        user_data = {
            'email': email,
            'first_name': validated_data['prenom_patient'],
            'last_name': validated_data['nom_patient'],
            'role': User.PATIENT,
            'password': password,
            'password2': password,
        }

        # Utiliser UserRegisterSerializer pour créer l'utilisateur
        user_serializer = UserRegisterSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        utilisateur_patient = user_serializer.save()  # L'utilisateur est créé ici

        # Création du dossier patient
        patient = Patient.objects.create(
            utilisateur=utilisateur_patient,
            NSS=validated_data['nss'],
            date_de_naissance=validated_data['date_de_naissance'],
            adresse=validated_data['adresse'],
            telephone=validated_data['telephone'],
            mutuelle=validated_data['mutuelle'],
            personne_a_contacter=validated_data['personne_a_contacter']
        )

        # Récupération ou création du médecin
        medecin, created = Medecin.objects.get_or_create(
            utilisateur=validated_data['utilisateur_medecin']
        )

        # Création du DPI
        dpi = DPI.objects.create(
            patient=patient,
            medecin=medecin,
            antecedents=validated_data.get("antecedents", "")
        )

        # Génération automatique du QR code
        dpi.save()

        return dpi


class QRCodeSerializer(serializers.ModelSerializer):
    qr_code_url = serializers.SerializerMethodField()

    class Meta:
        model = DPI
        fields = ['id_dpi', 'qr_code_url']

    def get_qr_code_url(self, obj):
        if obj.qr_code:
            return obj.qr_code.url
        return None