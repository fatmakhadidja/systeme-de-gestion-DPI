from django.test import RequestFactory
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from gestiondpi.models import DPI, Medecin, Consultation, Patient, Resume, Ordonnance, BilanBiologique, BilanRadiologique
from authentification.models import User
from datetime import date, datetime
from miseajourdpi.views import AjouterConsultation


@pytest.fixture
def setup_data(db):
    # Create a test user for the medecin
    medecin_user = User.objects.create_user(
        email="medecin@example.com",
        password="securepassword",
        first_name="John",
        last_name="Doe"
    )

    # Create a test Medecin
    medecin = Medecin.objects.create(
        utilisateur=medecin_user,
        specialite="Cardiologist"
    )

    # Create a test user for the patient
    patient_user = User.objects.create_user(
        email="patient@example.com",
        password="securepassword",
        first_name="Jane",
        last_name="Smith"
    )

    # Create a Patient instance
    patient = Patient.objects.create(
        NSS="111111",
        utilisateur=patient_user,
        date_de_naissance=datetime(1995, 12, 15)
    )

    # Create a DPI instance
    dpi = DPI.objects.create(
        patient=patient,
        medecin=medecin,
    )

    # Create a Resume instance
    resume = Resume.objects.create(
        diagnostic="Mild fever and cough",
        symptomes="Coughing, mild fever"
    )

    # Create an Ordonnance instance
    ordonnance = Ordonnance.objects.create(
         date_prescription=date.today(),
         etat_ordonnance=False
    )

    # Create a BilanBiologique instance
    bilan_biologique = BilanBiologique.objects.create(
        description="Basic blood test"
    )

    # Create a BilanRadiologique instance
    bilan_radiologique = BilanRadiologique.objects.create(
        description="Chest X-ray",
        type="X-ray"
    )

    # Create a Consultation instance
    consultation = Consultation.objects.create(
        dpi=dpi,
        date_consult=date.today(),
        resume=resume,
        ordonnance=ordonnance,
        bilan_biologique=bilan_biologique,
        bilan_radiologue=bilan_radiologique
    )
    print(f"Consultation created with ID: {consultation.id_consultation}")
    return {
        "consultation": consultation,
        "medecin": medecin,
        "patient": patient,
    }

def test_get_bilan_radiologique_by_consultation(setup_data):
    # Initialize the test client
    client = APIClient()

    # Retrieve the consultation from the setup data
    consultation = setup_data["consultation"]

    # Send a GET request to the endpoint with the consultation ID
    url = f"/api/radiology/dpi/{consultation.id_consultation}/bilanparconsult/"
    response = client.get(url)

    # Validate the response
    assert response.status_code == status.HTTP_200_OK
    assert response.data["consultation_id"] == consultation.id_consultation
    assert response.data["bilan_radiologique"]["description"] == "Chest X-ray"
    assert response.data["bilan_radiologique"]["type"] == "X-ray"
    print("Test passed: BilanRadiologique fetched successfully.")

def test_get_bilan_radiologique_invalid_consultation_id(setup_data):
    # Initialize the test client
    client = APIClient()

    # Create a consultation ID that doesn't exist
    invalid_consultation_id = 99999  # An ID that does not exist

    # Send a GET request to the endpoint with the invalid consultation ID
    url = f"/api/radiology/dpi/{invalid_consultation_id}/bilanparconsult/"
    response = client.get(url)

    # Validate the response for 404 error
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["message"] == "Consultation not found."
    print("Test passed: 404 error returned for invalid consultation ID.")



