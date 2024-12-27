from rest_framework import serializers
from gestiondpi.models import BilanRadiologique, RadiologyImage,Consultation


class RadiologyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyImage
        fields = '__all__'

class BilanRadiologiqueSerializer(serializers.ModelSerializer):
    images = RadiologyImageSerializer(many=True, read_only=True)

    class Meta:
        model = BilanRadiologique
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    bilan_radiologique = BilanRadiologiqueSerializer(read_only=True)
    

    class Meta:
        model = Consultation
        fields = '__all__'
