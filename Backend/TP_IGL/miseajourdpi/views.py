from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConsultationSerializer,SoinSerializer,PatientSerializer
from gestiondpi.models import Patient,Soin,Consultation,Ordonnance,Prescription

# the expected format of the info from the frontend
# {
#     "dpi": 1, 
#     "resume": {
#         "diagnostic": "string", 
#         "symptomes": "string", 
#         "antecedents": "string", 
#         "autres_informations": "string"
#     },
#     
#           "ordonnance": {
#             "date_prescription": "2025-05-30",
#             "etat_ordonnance": true,
#             "prescription": [{
#                 "dose": "string",
#                 "duree": "string",
#                 "medicament": {
#                 "nom": "string",
#                 "description": "string",
#                 "prix": 10,
#                 "quantite": 5
#           }],
#         }
#     },
#     "bilan_biologique": {
#         "description": "string"
#     },
#     "bilan_radiologique": {
#         "description": "string",
#         "type": "string"
#     }
# }

class AjouterConsultation(APIView):
    def post(self, request):
        # Serialize the data from the frontend to create a new consultation
        serializer = ConsultationSerializer(data=request.data)  
        
        if serializer.is_valid():
            # Explicitly call the create method to handle the nested logic
            consultation = serializer.create(serializer.validated_data)
            
            # Serialize the consultation object again to return it as a response
            consultation_serializer = ConsultationSerializer(consultation)
            
            return Response(consultation_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#-------------------------------------------------------------------------------------------  
# the expected format of the info from the frontend
# {
#   "patient": 1,  //ID 
#   "infirmier": 2,  //ID
#   "description": "Administered medication to the patient.",  
#   "date_soin": "2023-12-21",  
#   "observation": "Patient showed positive reaction to the medication."  
# }
class RemplirSoin(APIView):
    def post(self, request):
        # Extract id_patient from the request data
        data = request.data.copy()
        if 'patient' in data:  # If id_patient is provided by the frontend
            data['dpi'] = data.pop('patient')  # Rename id_patient to dpi (since it's the field expected by the serializer)

        # Use the updated data to validate the request
        serializer = SoinSerializer(data=data)

        if serializer.is_valid():
            soin = serializer.create(serializer.validated_data)

            soin_serializer = SoinSerializer(soin)

            return Response(soin_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetPatients(APIView):
    def get(self, request):
        patients = Patient.objects.all()  # Get all patients
        serializer = PatientSerializer(patients, many=True)  # Serialize the queryset
        return Response(serializer.data)  # Return serialized data in the response
# the data sent to the front end will be in this format (list of JSON data):
# [
# {'dpi': "",
#  'infirmier' : " ",
#  'description' : " ", 
# 'date_soin' : " ",
#  'observation' : " "}
#  ]   
class GetSoins(APIView):
    def get(self,request):
        soins = Soin.objects.all()  
        serializer = SoinSerializer(soins,many=True)
        return Response(serializer.data) 
    

class GetConsultations(APIView):
    
    def get(self, request):
        data = []
        consultations = Consultation.objects.all()
        for consultation in consultations:
        
            data.append({
               "num_consult": consultation.id_consultation,
               "date_consult": consultation.date_consult,
               "ordonnance": bool(consultation.ordonnance),
               "prescription": bool(Prescription.objects.filter(ordonnance=consultation.ordonnance).exists()),
               "resume": bool(consultation.resume),
            })
        return Response(data)

            

