from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConsultationSerializer,SoinSerializer

# the expected format of the info from the frontend
# {
#   "dpi": 1,
#   "resume": {
#     "diagnostic": "Patient is stable after surgery.",
#     "symptomes": "Pain in the abdomen.",
#     "antecedents": "No known previous conditions.",
#     "autres_informations": "Patient needs a follow-up visit."
#   },
#   "prescription": {
#     "dose": "500mg",
#     "duree": "7 days",
#     "medicament": {
#       "nom": "Aspirin",
#       "description": "Pain relief",
#       "prix": 10.99,
#       "quantite": 30
#     },
#     "ordonnance": {
#       "date_prescription": "2023-12-21",
#       "etat_ordonnance": true
#     }
#   },
#   "examen": [
#     {
#       "type": "biologique",
#       "description": "Blood test",
#       "parametres": ["WBC count", "Hemoglobin"]
#     },
#     {
#       "type": "radiologique",
#       "description": "Chest X-ray",
#       "parametres": ["X-ray report"]
#     }
#   ]
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
