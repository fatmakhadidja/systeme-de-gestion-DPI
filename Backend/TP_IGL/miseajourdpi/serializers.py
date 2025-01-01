from rest_framework import serializers
<<<<<<< HEAD
from gestiondpi.models import (
    Consultation,
    DPI,
    Resume,
    Ordonnance,
    Prescription,
    Soin,
    Patient,
    Infirmier,
    BilanRadiologique,
    BilanBiologique,
)
=======
from gestiondpi.models import Consultation, DPI, Resume, Ordonnance, Prescription, Medicament,Soin,Patient,Infirmier
from gestiondpi.models import BilanRadiologique, BilanBiologique
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d
from datetime import date


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["diagnostic", "symptomes", "antecedents", "autres_informations"]


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = Prescription
        fields = ["dose", "duree", "medicament"]
        extra_kwargs = {
            "dose": {"allow_blank": True},
            "duree": {"allow_blank": True},
            "medicament": {"allow_blank": True},
        }
=======
        model = Medicament
        fields = ['nom', 'description', 'prix', 'quantite']



class PrescriptionSerializer(serializers.ModelSerializer):
    medicament = MedicamentSerializer()

    class Meta : 
        model =Prescription
        fields = ['dose','duree','medicament']
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d

    def create(self, validated_data):
        # Extract the medicament data
        medicament_data = validated_data.pop('medicament')

        # Create the Medicament instance
        medicament = Medicament.objects.create(**medicament_data)

        # Create the Prescription instance and associate the medicament
        prescription = Prescription.objects.create(medicament=medicament, **validated_data)

        return prescription    
  

class OrdonnanceSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    prescription = PrescriptionSerializer(
        many=True, required=False
    )  # Nested prescriptions

    class Meta:
        model = Ordonnance
        fields = ["prescription"]

    def create(self, validated_data):
        prescription_data = validated_data.pop("prescription", [])

        # Set default values for Ordonnance
        validated_data["date_prescription"] = date.today()
        validated_data["etat_ordonnance"] = False

=======
    # Include the PrescriptionSerializer to handle the nested prescriptions
    prescription = PrescriptionSerializer(many=True, required=False)

    class Meta:
        model = Ordonnance
        fields = ['date_prescription', 'etat_ordonnance', 'prescription']

    def create(self, validated_data):
        # Extract prescription data from validated_data
        prescription_data = validated_data.pop('prescription', [])

>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d
        # Create the Ordonnance instance
        ordonnance = Ordonnance.objects.create(**validated_data)

        # Create and associate prescriptions if data is provided
        for prescription in prescription_data:
            prescription_serializer = PrescriptionSerializer(data=prescription)
            if prescription_serializer.is_valid(raise_exception=True):
                prescription_serializer.save(ordonnance=ordonnance)

        return ordonnance
    



class BilanRadiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanRadiologique
<<<<<<< HEAD
        fields = ["description", "type"]
        extra_kwargs = {
            "description": {"allow_blank": True},
            "type": {"allow_blank": True},
        }
=======
        fields = ['description', 'type']
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d

class BilanBiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanBiologique
<<<<<<< HEAD
        fields = ["description"]
        extra_kwargs = {
            "description": {"allow_blank": True},
        }
=======
        fields = ['description']
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d

class ConsultationSerializer(serializers.ModelSerializer):
    dpi = serializers.PrimaryKeyRelatedField(queryset=DPI.objects.all())
    resume = ResumeSerializer(required=True)
    ordonnance = OrdonnanceSerializer(required=False)
    
    # Use the Bilan serializers
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

        # Create the Resume instance
        resume = Resume.objects.create(**resume_data)

        # Create the Ordonnance instance if data is provided
        ordonnance = None
<<<<<<< HEAD
        if ordonnance_data and ordonnance_data.get("prescription"):
            valid_prescriptions = [
                pres
                for pres in ordonnance_data["prescription"]
                if all(pres.get(field) for field in ["dose", "duree", "medicament"])
            ]

            if valid_prescriptions:
                ordonnance_serializer = OrdonnanceSerializer(
                    data={"prescription": valid_prescriptions}
                )
                if ordonnance_serializer.is_valid(raise_exception=True):
                    ordonnance = ordonnance_serializer.save()

        # Create BilanBiologique if data is valid
        bilan_biologique = None
        if bilan_biologique_data:
            valid_bilan_biologique = {
                field: bilan_biologique_data.get(field)
                for field in ["description"]
                if bilan_biologique_data.get(field)
            }
            if valid_bilan_biologique:
                bilan_biologique_serializer = BilanBiologiqueSerializer(
                    data=valid_bilan_biologique
                )
                if bilan_biologique_serializer.is_valid(raise_exception=True):
                    bilan_biologique = bilan_biologique_serializer.save()

        # Create BilanRadiologique if data is valid
        bilan_radiologue = None
        if bilan_radiologue_data:
            valid_bilan_radiologue = {
                field: bilan_radiologue_data.get(field)
                for field in ["description", "type"]
                if bilan_radiologue_data.get(field)
            }
            if valid_bilan_radiologue:
                bilan_radiologue_serializer = BilanRadiologiqueSerializer(
                    data=valid_bilan_radiologue
                )
                if bilan_radiologue_serializer.is_valid(raise_exception=True):
                    bilan_radiologue = bilan_radiologue_serializer.save()

        # Create Consultation instance
=======
        if ordonnance_data:
            ordonnance_serializer = OrdonnanceSerializer(data=ordonnance_data)
            if ordonnance_serializer.is_valid(raise_exception=True):
                ordonnance = ordonnance_serializer.save()

            # Create Prescriptions if provided in ordonnance
            prescription_data = ordonnance_data.get('prescription', [])
            if prescription_data:
                for prescription in prescription_data:
                    prescription_serializer = PrescriptionSerializer(data=prescription)
                    if prescription_serializer.is_valid(raise_exception=True):
                        prescription_serializer.save(ordonnance=ordonnance)

        # Create the Consultation instance
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d
        consultation = Consultation.objects.create(
            dpi=dpi,
            resume=resume,
            ordonnance=ordonnance,
            date_consult=date.today(),
<<<<<<< HEAD
            bilan_biologique=bilan_biologique,
            bilan_radiologue=bilan_radiologue,
=======
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d
        )

        # Create BilanBiologique if data is provided
        if bilan_biologique_data:
            bilan_biologique_serializer = BilanBiologiqueSerializer(data=bilan_biologique_data)
            if bilan_biologique_serializer.is_valid(raise_exception=True):
                bilan_biologique = bilan_biologique_serializer.save()
                consultation.bilan_biologique = bilan_biologique

        # Create BilanRadiologique if data is provided
        if bilan_radiologue_data:
            bilan_radiologue_serializer = BilanRadiologiqueSerializer(data=bilan_radiologue_data)
            if bilan_radiologue_serializer.is_valid(raise_exception=True):
                bilan_radiologue = bilan_radiologue_serializer.save()
                consultation.bilan_radiologue = bilan_radiologue

        # Save the consultation after adding bilan objects
        consultation.save()

        return consultation


# Serializer for Soin model
class SoinSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    dpi = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), required=False
    )  # Reference Patient by ID
    infirmier = serializers.PrimaryKeyRelatedField(queryset=Infirmier.objects.all())
=======
    dpi = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=False)  # Removed required=True for dpi
    infirmier = serializers.PrimaryKeyRelatedField(queryset=Infirmier.objects.all())  # Reference Infirmier by ID
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d

    class Meta:
        model = Soin
        fields = ["dpi", "infirmier", "description", "date_soin", "observation"]

    def create(self, validated_data):
<<<<<<< HEAD
        patient_id = validated_data.pop("dpi")
=======
        # Extract patient_id (from frontend)
        patient_id = validated_data.pop('dpi')  # This will be the id_patient
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d

        # Find the corresponding DPI object based on the patient_id
        try:
            dpi = DPI.objects.get(patient=patient_id)  # the DPI has a ForeignKey to the Patient model
        except DPI.DoesNotExist:
            raise serializers.ValidationError(
                "DPI for the given patient does not exist."
            )

        # Extract infirmier reference 
        infirmier = validated_data.pop('infirmier')
       

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
<<<<<<< HEAD
    first_name = serializers.CharField(source="utilisateur.first_name")
    last_name = serializers.CharField(source="utilisateur.last_name")

    class Meta:
        model = Patient
        fields = ["id_patient", "first_name", "last_name"]
=======
    first_name = serializers.CharField(source='utilisateur.first_name')  # Get first_name from the User model
    last_name = serializers.CharField(source='utilisateur.last_name')    # Get last_name from the User model

    class Meta:
        model = Patient
        fields = ['id_patient', 'first_name', 'last_name']   
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d

class DPISerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta : 
        model = DPI
<<<<<<< HEAD
        fields = ["patient"]
=======
        fields=['patient']        
>>>>>>> 211d2ed8dfccbcf5a7a41ee5fb2c472200e4107d
