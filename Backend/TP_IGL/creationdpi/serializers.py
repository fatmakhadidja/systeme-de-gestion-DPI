from rest_framework import serializers
from gestiondpi.models import Patient, DPI, Medecin
from authentification.models import User


import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

class DPICreationSerializer(serializers.Serializer):
    nom_patient = serializers.CharField(max_length=100)
    prenom_patient = serializers.CharField(max_length=100)
    nss = serializers.CharField(max_length=20)
    date_de_naissance = serializers.DateField()
    adresse = serializers.CharField()
    telephone = serializers.CharField(max_length=15)
    mutuelle = serializers.CharField(max_length=100)
    personne_a_contacter = serializers.CharField(max_length=100)
    nom_medecin = serializers.CharField(max_length=100)
    antecedents = serializers.CharField(allow_blank=True, default="")  # Nouveau champ pour les antécédents

    def validate(self, data):
        # Recherche du patient
        try:
            utilisateur_patient = User.objects.get(
                first_name=data['nom_patient'],
                last_name=data['prenom_patient'],
                role=User.PATIENT
            )
        except User.DoesNotExist:
            raise serializers.ValidationError({"patient": "Patient introuvable avec ce nom et prénom."})

        # Recherche du médecin
        try:
            utilisateur_medecin = User.objects.get(
                first_name=data['nom_medecin'],
                role=User.MEDECIN
            )
        except User.DoesNotExist:
            raise serializers.ValidationError({"medecin": "Médecin introuvable avec ce nom."})

        # Ajout des utilisateurs validés au contexte
        data['utilisateur_patient'] = utilisateur_patient
        data['utilisateur_medecin'] = utilisateur_medecin
        return data

    def create(self, validated_data):
        # Création du patient
        patient = Patient.objects.create(
            utilisateur=validated_data['utilisateur_patient'],
            NSS=validated_data['nss'],
            date_de_naissance=validated_data['date_de_naissance'],
            adresse=validated_data['adresse'],
            telephone=validated_data['telephone'],
            mutuelle=validated_data['mutuelle'],
            personne_a_contacter=validated_data['personne_a_contacter']
        )

        # Recherche ou création du médecin
        medecin, created = Medecin.objects.get_or_create(
            utilisateur=validated_data['utilisateur_medecin']
        )

        # Création du DPI avec les antécédents fournis
        dpi = DPI.objects.create(
            patient=patient,
            medecin=medecin,
            antecedents=validated_data.get("antecedents", "")  # Ajouter les antécédents ici
        )

        # Génération et sauvegarde du QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(str(dpi.id_dpi))  # Ajoutez l'ID du DPI au QR code
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        file_name = f"dpi_{dpi.id_dpi}_qrcode.png"
        dpi.qr_code.save(file_name, ContentFile(buffer.getvalue()), save=False)
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


