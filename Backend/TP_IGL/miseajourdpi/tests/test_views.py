import pytest
from rest_framework.test import APIClient
from rest_framework import status
from gestiondpi.models import DPI, Medecin, Consultation,Patient
from authentification.models import User
from datetime import datetime


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

    patient = Patient.objects.create(
        utilisateur=patient_user,
        date_de_naissance = datetime(1995, 12, 15)
    )

    # Create a test DPI (Patient record)
    dpi = DPI.objects.create(
        patient=patient,
        medecin=medecin,
    )

    # Return setup data for tests
    return {
        "client": APIClient(),
        "url": "/api/miseajourdpi/ajouterConsultation/",
        "dpi": dpi,
        "valid_data": {
            "dpi": dpi.id_dpi,
            "resume": {
                "diagnostic": "Test Diagnostic",
                "symptomes": "Test Symptomes",
                "antecedents": "Test Antecedents",
                "autres_informations": "Other Information",
            },
            "ordonnance": {
                "date_prescription": "2025-05-30",
                "etat_ordonnance": True,
                "prescription": [
                    {
                        "dose": "500mg",
                        "duree": "5 days",
                        "medicament": {
                            "nom": "Paracetamol",
                            "description": "Painkiller",
                            "prix": 10.0,
                            "quantite": 20,
                        },
                    }
                ],
            },
            "bilan_biologique": {"description": "Normal blood work"},
            "bilan_radiologique": {"description": "No issues", "type": "X-ray"},
        }
    }


def test_ajouter_consultation_success(setup_data):
    client = setup_data["client"]
    url = setup_data["url"]
    valid_data = setup_data["valid_data"]

    # Send a POST request with valid data
    response = client.post(url, valid_data, format="json")

    # Assert the response status code
    assert response.status_code == status.HTTP_201_CREATED

    # Assert that the Consultation object was created
    assert Consultation.objects.count() == 1

    # Assert that the response contains the correct data
    consultation = Consultation.objects.first()
    assert consultation.dpi.id_dpi == valid_data["dpi"]
    assert response.data["resume"]["diagnostic"] == "Test Diagnostic"


def test_ajouter_consultation_invalid_data(setup_data):
    client = setup_data["client"]
    url = setup_data["url"]
    valid_data = setup_data["valid_data"]

    # Send a POST request with invalid data (e.g., missing dpi)
    invalid_data = valid_data.copy()
    invalid_data.pop("dpi")
    response = client.post(url, invalid_data, format="json")

    # Assert the response status code
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Assert that no Consultation object was created
    assert Consultation.objects.count() == 0
