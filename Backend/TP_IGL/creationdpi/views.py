from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DPICreationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from gestiondpi.models import DPI ,Patient
from .serializers import QRCodeSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from pyzbar.pyzbar import decode
from PIL import Image

class DPICreationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DPICreationSerializer(data=request.data)
        if serializer.is_valid():
            dpi = serializer.save()
            return Response(
                {
                    "message": "DPI created successfully",
                    "dpi_id": dpi.id_dpi,
                    "qr_code": dpi.qr_code.url,  # URL of the generated QR code
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class QRCodeView(APIView):
    def get(self, request, dpi_id):
        # Récupérer le DPI par son ID
        dpi = get_object_or_404(DPI, id_dpi=dpi_id)

        # Sérialiser l'objet DPI pour obtenir l'URL du QR code
        serializer = QRCodeSerializer(dpi)

        return Response(serializer.data, status=status.HTTP_200_OK)
