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

from .serializers import SearchDPIByNSSSerializer
from .serializers import QRSearchSerializer
class DPICreationView(APIView):
    def post(self, request):
        serializer = DPICreationSerializer(data=request.data)
        if serializer.is_valid():
            dpi = serializer.save()
            return Response(
                {
                    "message": "DPI créé avec succès",
                    "dpi_id": dpi.id_dpi,
                    "qr_code_url": dpi.qr_code.url,  # Retourner l'URL du QR code
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

class SearchDPIByNSSView(APIView):
    def get(self, request):
        # Get the NSS from the query parameters
        nss = request.query_params.get('nss')

        if not nss:
            return Response({"error": "NSS parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the patient using the NSS
            patient = Patient.objects.get(NSS=nss)
            # Retrieve the associated DPI
            dpi = DPI.objects.get(patient=patient)

            # Prepare response data
            response_data = {
                "id_dpi": dpi.id_dpi,
                "antecedents": dpi.antecedents,
                "qr_code_url": dpi.qr_code.url if dpi.qr_code else None,
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Patient.DoesNotExist:
            return Response({"error": "Patient with this NSS does not exist."}, status=status.HTTP_404_NOT_FOUND)

        except DPI.DoesNotExist:
            return Response({"error": "DPI not found for this patient."}, status=status.HTTP_404_NOT_FOUND)


class QRCodeSearchView(APIView):
    # Allow image file upload
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # Get the uploaded QR code image
        uploaded_file = request.FILES.get('file')  # 'file' is the key for the uploaded image

        if not uploaded_file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Open the uploaded image and decode the QR code
            image = Image.open(uploaded_file)
            decoded_objects = decode(image)

            # Check if QR code is decoded successfully
            if not decoded_objects:
                return Response({"error": "No QR code found in the image."}, status=status.HTTP_400_BAD_REQUEST)

            # Extract DPI ID from decoded QR code data (assuming it's in the QR code)
            dpi_id = decoded_objects[0].data.decode('utf-8')

            try:
                # Retrieve the corresponding DPI record using the decoded ID
                dpi = DPI.objects.get(id_dpi=dpi_id)

                # Serialize the DPI data using the new serializer
                serializer = QRSearchSerializer(dpi)  # Updated serializer name

                return Response(serializer.data, status=status.HTTP_200_OK)

            except DPI.DoesNotExist:
                return Response({"error": "DPI not found for this QR code."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)