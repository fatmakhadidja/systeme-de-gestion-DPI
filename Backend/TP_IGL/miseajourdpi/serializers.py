from rest_framework import serializers
from gestiondpi.models import Consultation, DPI, Resume, Ordonnance, Prescription,Soin,Patient,Infirmier
from gestiondpi.models import BilanRadiologique, BilanBiologique
from datetime import date


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['diagnostic', 'symptomes', 'antecedents', 'autres_informations']


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta : 
        model =Prescription
        fields = ['dose','duree','medicament']
        extra_kwargs = {
            'dose': {'allow_blank': True},
            'duree': {'allow_blank': True},
            'medicament': {'allow_blank': True},
        }
    def create(self, validated_data):       
        # Create the Prescription instance and associate the medicament
        prescription = Prescription.objects.create(**validated_data)

        return prescription    
  

class OrdonnanceSerializer(serializers.ModelSerializer):
    # Include the PrescriptionSerializer to handle the nested prescriptions
    prescription = PrescriptionSerializer(many=True, required=False)

    class Meta:
        model = Ordonnance
        fields = ['prescription']  # Exclude 'date_prescription'
        
    def create(self, validated_data):
        
        prescription_data = validated_data.pop('prescription', [])

        # Set the value for date_prescription explicitly
        validated_data['date_prescription'] = date.today()  
        validated_data['etat_ordonnance'] = False

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
        fields = ['description', 'type']
        extra_kwargs = {
            'description': {'allow_blank': True},
            'type': {'allow_blank': True},
        }

class BilanBiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanBiologique
        fields = ['description']
        extra_kwargs = {
            'description': {'allow_blank': True},
        }


class ConsultationSerializer(serializers.ModelSerializer):
    dpi = serializers.PrimaryKeyRelatedField(queryset=DPI.objects.all())
    resume = ResumeSerializer(required=True)
    ordonnance = OrdonnanceSerializer(required=False)
    
    # Use the Bilan serializers
    bilan_biologique = BilanBiologiqueSerializer(required=False)
    bilan_radiologue = BilanRadiologiqueSerializer(required=False)

    class Meta:
        model = Consultation
        fields = ['dpi', 'resume', 'ordonnance', 'bilan_biologique', 'bilan_radiologue']

    def create(self, validated_data):
     dpi = validated_data.pop('dpi')
     resume_data = validated_data.pop('resume')
     ordonnance_data = validated_data.pop('ordonnance', None)
     bilan_biologique_data = validated_data.pop('bilan_biologique', None)
     bilan_radiologue_data = validated_data.pop('bilan_radiologue', None)

    # Create the Resume instance
     resume = Resume.objects.create(**resume_data)

    # Create the Ordonnance instance if data is provided and valid
     ordonnance = None
     if ordonnance_data and ordonnance_data.get('prescription'):
        # Check if prescriptions are not empty strings
        prescription_data = ordonnance_data['prescription']
        valid_prescriptions = [
            pres for pres in prescription_data
            if all(pres.get(field) for field in ['dose', 'duree', 'medicament'])
        ]

        if valid_prescriptions:  # Proceed only if there are valid prescriptions
            ordonnance_serializer = OrdonnanceSerializer(data={'prescription': valid_prescriptions})
            if ordonnance_serializer.is_valid(raise_exception=True):
                ordonnance = ordonnance_serializer.save()

    # Create BilanBiologique if data is provided and valid
     bilan_biologique = None
     if bilan_biologique_data:
        valid_bilan_biologique = {
            field: bilan_biologique_data.get(field)
            for field in ['description'] if bilan_biologique_data.get(field)
        }
        if valid_bilan_biologique:  # Proceed only if the field is valid
            bilan_biologique_serializer = BilanBiologiqueSerializer(data=valid_bilan_biologique)
            if bilan_biologique_serializer.is_valid(raise_exception=True):
                bilan_biologique = bilan_biologique_serializer.save()

    # Create BilanRadiologique if data is provided and valid
     bilan_radiologue = None
     if bilan_radiologue_data:
        valid_bilan_radiologue = {
            field: bilan_radiologue_data.get(field)
            for field in ['description', 'type'] if bilan_radiologue_data.get(field)
        }
        if valid_bilan_radiologue:  # Proceed only if the fields are valid
            bilan_radiologue_serializer = BilanRadiologiqueSerializer(data=valid_bilan_radiologue)
            if bilan_radiologue_serializer.is_valid(raise_exception=True):
                bilan_radiologue = bilan_radiologue_serializer.save()

    # Create the Consultation instance and link bilan objects
        consultation = Consultation.objects.create(
        dpi=dpi,
        resume=resume,
        ordonnance=ordonnance,
        date_consult=date.today(),
        bilan_biologique=bilan_biologique,
        bilan_radiologue=bilan_radiologue
    )

     return consultation



# Serializer for Soin model
class SoinSerializer(serializers.ModelSerializer):
    dpi = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=False)  # Removed required=True for dpi
    infirmier = serializers.PrimaryKeyRelatedField(queryset=Infirmier.objects.all())  # Reference Infirmier by ID

    class Meta:
        model = Soin
        fields = ['dpi', 'infirmier', 'description', 'date_soin', 'observation']

    def create(self, validated_data):
        # Extract patient_id (from frontend)
        patient_id = validated_data.pop('dpi')  # This will be the id_patient

        # Find the corresponding DPI object based on the patient_id
        try:
            dpi = DPI.objects.get(patient=patient_id)  # the DPI has a ForeignKey to the Patient model
        except DPI.DoesNotExist:
            raise serializers.ValidationError("DPI for the given patient does not exist.")

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
    first_name = serializers.CharField(source='utilisateur.first_name')  
    last_name = serializers.CharField(source='utilisateur.last_name')    


    class Meta:
        model = Patient
        fields = ['id_patient', 'first_name', 'last_name']   

class DPISerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta : 
        model = DPI
        fields=['patient']        