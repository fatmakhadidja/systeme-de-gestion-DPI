from rest_framework import serializers
from gestiondpi.models import (
<<<<<<< HEAD
    Consultation, DPI, Resume, Ordonnance, Prescription, Soin, Patient, Infirmier,
    BilanRadiologique, BilanBiologique
)
=======
    Consultation,
    DPI,
    Resume,
    Ordonnance,
    Prescription,
    Medicament,
    Soin,
    Patient,
    Infirmier,
)
from gestiondpi.models import BilanRadiologique, BilanBiologique
>>>>>>> mary
from datetime import date


# -------------------------------------------------------------------------------------------
# Serializer for the Resume model
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["diagnostic", "symptomes", "antecedents", "autres_informations"]


<<<<<<< HEAD
# -------------------------------------------------------------------------------------------
# Serializer for the Prescription model
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['dose', 'duree', 'medicament']
        extra_kwargs = {
            'dose': {'allow_blank': True},
            'duree': {'allow_blank': True},
            'medicament': {'allow_blank': True},
        }

    def create(self, validated_data):
        # Create and return a Prescription instance
        prescription = Prescription.objects.create(**validated_data)
        return prescription

=======
class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = ["nom", "description", "prix", "quantite"]


class PrescriptionSerializer(serializers.ModelSerializer):
    medicament = MedicamentSerializer()

    class Meta:
        model = Prescription
        fields = ["dose", "duree", "medicament"]

    def create(self, validated_data):
        # Extract the medicament data
        medicament_data = validated_data.pop("medicament")

        # Create the Medicament instance
        medicament = Medicament.objects.create(**medicament_data)

        # Create the Prescription instance and associate the medicament
        prescription = Prescription.objects.create(
            medicament=medicament, **validated_data
        )

        return prescription

>>>>>>> mary

# -------------------------------------------------------------------------------------------
# Serializer for the Ordonnance model
class OrdonnanceSerializer(serializers.ModelSerializer):
    prescription = PrescriptionSerializer(many=True, required=False)  # Nested prescriptions

    class Meta:
        model = Ordonnance
<<<<<<< HEAD
        fields = ['prescription']

    def create(self, validated_data):
        prescription_data = validated_data.pop('prescription', [])
=======
        fields = ["date_prescription", "etat_ordonnance", "prescription"]

    def create(self, validated_data):
        # Extract prescription data from validated_data
        prescription_data = validated_data.pop("prescription", [])
>>>>>>> mary

        # Set default values for Ordonnance
        validated_data['date_prescription'] = date.today()
        validated_data['etat_ordonnance'] = False

        # Create the Ordonnance instance
        ordonnance = Ordonnance.objects.create(**validated_data)

        # Create associated prescriptions
        for prescription in prescription_data:
            prescription_serializer = PrescriptionSerializer(data=prescription)
            if prescription_serializer.is_valid(raise_exception=True):
                prescription_serializer.save(ordonnance=ordonnance)

        return ordonnance


# -------------------------------------------------------------------------------------------
# Serializer for the BilanRadiologique model
class BilanRadiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanRadiologique
<<<<<<< HEAD
        fields = ['description', 'type']
        extra_kwargs = {
            'description': {'allow_blank': True},
            'type': {'allow_blank': True},
        }
=======
        fields = ["description", "type"]

>>>>>>> mary


# -------------------------------------------------------------------------------------------
# Serializer for the BilanBiologique model
class BilanBiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanBiologique
<<<<<<< HEAD
        fields = ['description']
        extra_kwargs = {
            'description': {'allow_blank': True},
        }
=======
        fields = ["description"]

>>>>>>> mary


# -------------------------------------------------------------------------------------------
# Serializer for the Consultation model
class ConsultationSerializer(serializers.ModelSerializer):
    dpi = serializers.PrimaryKeyRelatedField(queryset=DPI.objects.all())
    resume = ResumeSerializer(required=True)
    ordonnance = OrdonnanceSerializer(required=False)
<<<<<<< HEAD
=======

    # Use the Bilan serializers
>>>>>>> mary
    bilan_biologique = BilanBiologiqueSerializer(required=False)
    bilan_radiologue = BilanRadiologiqueSerializer(required=False)

    class Meta:
        model = Consultation
        fields = ["dpi", "resume", "ordonnance", "bilan_biologique", "bilan_radiologue"]

    def create(self, validated_data):
        dpi = validated_data.pop("dpi")
        resume_data = validated_data.pop("resume")
        ordonnance_data = validated_data.pop("ordonnance", None)
        bilan_biologique_data = validated_data.pop("bilan_biologique", None)
        bilan_radiologue_data = validated_data.pop("bilan_radiologue", None)

        # Create Resume instance
        resume = Resume.objects.create(**resume_data)

        # Create Ordonnance if data is valid
        ordonnance = None
        if ordonnance_data and ordonnance_data.get('prescription'):
            valid_prescriptions = [
                pres for pres in ordonnance_data['prescription']
                if all(pres.get(field) for field in ['dose', 'duree', 'medicament'])
            ]

<<<<<<< HEAD
            if valid_prescriptions:
                ordonnance_serializer = OrdonnanceSerializer(data={'prescription': valid_prescriptions})
                if ordonnance_serializer.is_valid(raise_exception=True):
                    ordonnance = ordonnance_serializer.save()
=======
            # Create Prescriptions if provided in ordonnance
            prescription_data = ordonnance_data.get("prescription", [])
            if prescription_data:
                for prescription in prescription_data:
                    prescription_serializer = PrescriptionSerializer(data=prescription)
                    if prescription_serializer.is_valid(raise_exception=True):
                        prescription_serializer.save(ordonnance=ordonnance)
>>>>>>> mary

        # Create BilanBiologique if data is valid
        bilan_biologique = None
        if bilan_biologique_data:
            valid_bilan_biologique = {
                field: bilan_biologique_data.get(field)
                for field in ['description'] if bilan_biologique_data.get(field)
            }
            if valid_bilan_biologique:
                bilan_biologique_serializer = BilanBiologiqueSerializer(data=valid_bilan_biologique)
                if bilan_biologique_serializer.is_valid(raise_exception=True):
                    bilan_biologique = bilan_biologique_serializer.save()

        # Create BilanRadiologique if data is valid
        bilan_radiologue = None
        if bilan_radiologue_data:
            valid_bilan_radiologue = {
                field: bilan_radiologue_data.get(field)
                for field in ['description', 'type'] if bilan_radiologue_data.get(field)
            }
            if valid_bilan_radiologue:
                bilan_radiologue_serializer = BilanRadiologiqueSerializer(data=valid_bilan_radiologue)
                if bilan_radiologue_serializer.is_valid(raise_exception=True):
                    bilan_radiologue = bilan_radiologue_serializer.save()

        # Create Consultation instance
        consultation = Consultation.objects.create(
            dpi=dpi,
            resume=resume,
            ordonnance=ordonnance,
            date_consult=date.today(),
            bilan_biologique=bilan_biologique,
            bilan_radiologue=bilan_radiologue
        )

<<<<<<< HEAD
=======
        # Create BilanBiologique if data is provided
        if bilan_biologique_data:
            bilan_biologique_serializer = BilanBiologiqueSerializer(
                data=bilan_biologique_data
            )
            if bilan_biologique_serializer.is_valid(raise_exception=True):
                bilan_biologique = bilan_biologique_serializer.save()
                consultation.bilan_biologique = bilan_biologique

        # Create BilanRadiologique if data is provided
        if bilan_radiologue_data:
            bilan_radiologue_serializer = BilanRadiologiqueSerializer(
                data=bilan_radiologue_data
            )
            if bilan_radiologue_serializer.is_valid(raise_exception=True):
                bilan_radiologue = bilan_radiologue_serializer.save()
                consultation.bilan_radiologue = bilan_radiologue

        # Save the consultation after adding bilan objects
        consultation.save()

>>>>>>> mary
        return consultation


# -------------------------------------------------------------------------------------------
# Serializer for the Soin model
class SoinSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    dpi = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=False)  # Reference Patient by ID
    infirmier = serializers.PrimaryKeyRelatedField(queryset=Infirmier.objects.all())
=======
    dpi = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), required=False
    )  # Removed required=True for dpi
    infirmier = serializers.PrimaryKeyRelatedField(
        queryset=Infirmier.objects.all()
    )  # Reference Infirmier by ID
>>>>>>> mary

    class Meta:
        model = Soin
        fields = ["dpi", "infirmier", "description", "date_soin", "observation"]

    def create(self, validated_data):
<<<<<<< HEAD
        patient_id = validated_data.pop('dpi')
=======
        # Extract patient_id (from frontend)
        patient_id = validated_data.pop("dpi")  # This will be the id_patient
>>>>>>> mary

        # Retrieve the corresponding DPI
        try:
<<<<<<< HEAD
            dpi = DPI.objects.get(patient=patient_id)
=======
            dpi = DPI.objects.get(
                patient=patient_id
            )  # the DPI has a ForeignKey to the Patient model
>>>>>>> mary
        except DPI.DoesNotExist:
            raise serializers.ValidationError(
                "DPI for the given patient does not exist."
            )

<<<<<<< HEAD
        # Create and return Soin instance
        soin = Soin.objects.create(dpi=dpi, **validated_data)
        return soin


# -------------------------------------------------------------------------------------------
# Serializer for the Patient model
class PatientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='utilisateur.first_name')
    last_name = serializers.CharField(source='utilisateur.last_name')

    class Meta:
        model = Patient
        fields = ['id_patient', 'first_name', 'last_name']
=======
        # Extract infirmier reference
        infirmier = validated_data.pop("infirmier")

        # Create and return the Soin instance
        soin = Soin.objects.create(dpi=dpi, infirmier=infirmier, **validated_data)
        return soin


# the info sent to the frontend
#  [
#     {
#         "id_patient": 1,
#         "first_name": "Lokman",
#         "last_name": "Djerfi"
#     }
# ]
class PatientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        source="utilisateur.first_name"
    )  # Get first_name from the User model
    last_name = serializers.CharField(
        source="utilisateur.last_name"
    )  # Get last_name from the User model

    class Meta:
        model = Patient
        fields = ["id_patient", "first_name", "last_name"]

>>>>>>> mary


# -------------------------------------------------------------------------------------------
# Serializer for the DPI model
class DPISerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = DPI
<<<<<<< HEAD
        fields = ['patient']
=======
        fields = ["patient"]
>>>>>>> mary
