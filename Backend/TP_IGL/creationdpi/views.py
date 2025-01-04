
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import  DPICreationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
<<<<<<< HEAD
from gestiondpi.models import DPI, Patient
from .serializers import QRCodeSerializer, DPIListSerializer, DPIDetailSerializer
=======
from gestiondpi.models import DPI ,Patient
from .serializers import QRCodeSerializer , DPIListSerializer ,DPIDetailSerializer
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
from rest_framework.parsers import MultiPartParser, FormParser
from pyzbar.pyzbar import decode
from PIL import Image
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

<<<<<<< HEAD
###########################################CREATION DPI###########################################################"

=======



###########################################CREATION DPI###########################################################"
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2

class DPICreationView(APIView):
    def post(self, request, *args, **kwargs):
        # Sérialisation et validation des données de la requête
        serializer = DPICreationSerializer(data=request.data)
        if serializer.is_valid():
            # Création du DPI (l'utilisateur est automatiquement créé via le sérialiseur)
            dpi = serializer.save()

            return Response(
                {
                    "message": "DPI créé avec succès",
                    "dpi_id": dpi.id_dpi,
                    "qr_code": dpi.qr_code.url,  # URL du QR code généré
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QRCodeView(APIView):
    def get(self, request, dpi_id):
        # Récupérer le DPI par son ID
        dpi = get_object_or_404(DPI, id_dpi=dpi_id)

        # Sérialiser l'objet DPI pour obtenir l'URL du QR code
        serializer = QRCodeSerializer(dpi)

        return Response(serializer.data, status=status.HTTP_200_OK)


<<<<<<< HEAD
=======


>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
########################################RECHERCHE###########################################################################""


class SearchDPIByNSSView(APIView):
    def get(self, request):
        # Obtenir le NSS depuis les paramètres de requête
        nss = request.query_params.get("nss")

        if not nss:
<<<<<<< HEAD
            return Response(
                {"error": "NSS parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
=======
            return Response({"error": "NSS parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2

        try:
            # Récupérer le patient via le NSS
            patient = Patient.objects.get(NSS=nss)

            # Récupérer le DPI associé
            dpi = DPI.objects.get(patient=patient)

            # Utiliser le serializer pour formater les données
            serializer = DPIListSerializer(dpi)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Patient.DoesNotExist:
<<<<<<< HEAD
            return Response(
                {"error": "Patient with this NSS does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except DPI.DoesNotExist:
            return Response(
                {"error": "DPI not found for this patient."},
                status=status.HTTP_404_NOT_FOUND,
            )
=======
            return Response({"error": "Patient with this NSS does not exist."}, status=status.HTTP_404_NOT_FOUND)

        except DPI.DoesNotExist:
            return Response({"error": "DPI not found for this patient."}, status=status.HTTP_404_NOT_FOUND)
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2


class QRCodeScanView(APIView):
    # Permettre l'upload de fichiers image
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # Obtenir le fichier image téléchargé
<<<<<<< HEAD
        uploaded_file = request.FILES.get(
            "file"
        )  # 'file' est la clé pour l'image téléchargée

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST
            )
=======
        uploaded_file = request.FILES.get("file")  # 'file' est la clé pour l'image téléchargée

        if not uploaded_file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2

        try:
            # Ouvrir l'image téléchargée et décoder le QR code
            image = Image.open(uploaded_file)
            decoded_objects = decode(image)

            # Vérifier si le QR code a été décodé avec succès
            if not decoded_objects:
<<<<<<< HEAD
                return Response(
                    {"error": "No QR code found in the image."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
=======
                return Response({"error": "No QR code found in the image."}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2

            # Extraire le NSS des données décodées
            nss = decoded_objects[0].data.decode("utf-8")  # NSS décodé

            # Récupérer le patient et le DPI associé via le NSS
            try:
                patient = Patient.objects.get(NSS=nss)
                dpi = DPI.objects.get(patient=patient)

                # Utiliser le serializer pour formater les données
                serializer = DPIListSerializer(dpi)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Patient.DoesNotExist:
<<<<<<< HEAD
                return Response(
                    {"error": "Patient not found for this QR code."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            except DPI.DoesNotExist:
                return Response(
                    {"error": "DPI not found for this patient."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


############################################"AFFICHAGE####################################################


=======
                return Response({"error": "Patient not found for this QR code."}, status=status.HTTP_404_NOT_FOUND)
            except DPI.DoesNotExist:
                return Response({"error": "DPI not found for this patient."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

############################################"AFFICHAGE####################################################

>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
class ConsultDPIView(APIView):
    def get(self, request, utilisateur_id):
        # Récupérer le patient associé à l'utilisateur
        try:
            patient = Patient.objects.get(utilisateur__id=utilisateur_id)
        except Patient.DoesNotExist:
            raise NotFound("Aucun patient trouvé pour cet utilisateur.")

        # Récupérer le DPI du patient
        try:
            dpi = DPI.objects.get(patient=patient)
        except DPI.DoesNotExist:
            raise NotFound("Aucun DPI trouvé pour ce patient.")

        # Sérialiser les données du DPI
        serializer = DPIDetailSerializer(dpi)
        return Response(serializer.data)

<<<<<<< HEAD

class DPIListView(ListAPIView):
    queryset = DPI.objects.all()
    serializer_class = DPIListSerializer


=======
class DPIListView(ListAPIView):
    queryset = DPI.objects.all()
    serializer_class = DPIListSerializer
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
class DPIDetailView(RetrieveAPIView):
    queryset = DPI.objects.all()
    serializer_class = DPIDetailSerializer
