from rest_framework import serializers
from gestiondpi.models import Consultation, DPI, Resume, Ordonnance, Prescription, Medicament, Examen,Soin,Patient,Infirmier
from datetime import date

class ExamenSerializer(serializers.ModelSerializer):
    parametres = serializers.ListField(child=serializers.CharField(), required=False, default=list)

    class Meta:
        model = Examen
        fields = ['type', 'description', 'parametres']

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['diagnostic', 'symptomes', 'antecedents', 'autres_informations']

class OrdonnanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordonnance
        fields = ['date_prescription', 'etat_ordonnance']

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = ['nom', 'description', 'prix', 'quantite']

class PrescriptionSerializer(serializers.ModelSerializer):
    ordonnance = OrdonnanceSerializer()
    medicament = MedicamentSerializer()

    class Meta:
        model = Prescription
        fields = ['dose', 'duree', 'medicament', 'ordonnance']

    def create(self, validated_data):
        ordonnance_data = validated_data.pop('ordonnance')
        medicament_data = validated_data.pop('medicament')

        ordonnance = Ordonnance.objects.create(**ordonnance_data)
        medicament = Medicament.objects.create(**medicament_data)

        prescription = Prescription.objects.create(
            ordonnance=ordonnance,
            medicament=medicament,
            **validated_data
        )
        return prescription

class ConsultationSerializer(serializers.ModelSerializer):
    dpi = serializers.PrimaryKeyRelatedField(queryset=DPI.objects.all())
    resume = ResumeSerializer()
    prescription = PrescriptionSerializer()
    examen = ExamenSerializer(many=True, required=False)  # Accepts a list of exams

    class Meta:
        model = Consultation
        fields = ['dpi', 'resume', 'prescription', 'examen']  # Include examen as a list

    def create(self, validated_data):
        dpi = validated_data.pop('dpi')
        resume_data = validated_data.pop('resume')
        prescription_data = validated_data.pop('prescription')
        examen_data = validated_data.pop('examen', [])  # Get list of examen (empty list if none)

        resume = Resume.objects.create(**resume_data)

        prescription_serializer = PrescriptionSerializer(data=prescription_data)
        if prescription_serializer.is_valid(raise_exception=True):
            prescription = prescription_serializer.save()

        # Handle creation of multiple Examen objects if present
        examens = []
        for examen in examen_data:
            examen_serializer = ExamenSerializer(data=examen)
            if examen_serializer.is_valid(raise_exception=True):
                examen = examen_serializer.save()
                examens.append(examen)

        consultation = Consultation.objects.create(
            dpi=dpi,
            resume=resume,
            prescription=prescription,
            date_consult=date.today(),
        )

        # Add each created examen to the consultation (many-to-many relationship)
        consultation.examen.set(examens)

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