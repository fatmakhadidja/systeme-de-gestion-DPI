from django.db import models
from authentification.models import User
import qrcode
import uuid
from io import BytesIO
from django.core.files.base import ContentFile


class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # One-to-one link with User
    NSS = models.CharField(max_length=20, unique=True)  # Unique Social Security Number
    date_de_naissance = models.DateField()  # Date of birth
    adresse = models.TextField()  # Address
    telephone = models.CharField(max_length=15)  # Phone number
    mutuelle = models.CharField(max_length=100)  # Insurance provider
    personne_a_contacter = models.CharField(max_length=100)  # Emergency contact


# Represents a doctor with a specialty, linked to a User account
class Medecin(models.Model):
    id_medecin = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # One-to-one link with User
    specialite = models.CharField(max_length=100)  # Medical specialty


# Represents a nurse, linked to a User account
class Infirmier(models.Model):
    id_infirmier = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # One-to-one link with User


class Laborantin(models.Model):
    id_laborantin = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)


# Represents a radiologist, linked to a User account


class Radiologue(models.Model):
    id_radiologue = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # One-to-one link with User


# Represents an administrator, linked to a User account
class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # One-to-one link with User


# Represents a hospital pharmacist with a method to validate prescriptions
class PharmacienHospitalier(models.Model):
    id_pharmacienHospitalier = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # One-to-one link with User

    def valider_ordonnance(self, ordonnance):
        """Marks a prescription as validated."""
        ordonnance.etat_ordonnance = True
        ordonnance.save()


class DPI(models.Model):
    id_dpi = models.AutoField(primary_key=True)
    patient = models.OneToOneField("Patient", on_delete=models.CASCADE, default=1)
    medecin = models.ForeignKey(
        "Medecin", related_name="medcin", on_delete=models.CASCADE, default=1
    )
    antecedents = models.TextField(blank=True)
    qr_code = models.ImageField(
        upload_to="qrcodes/", unique=True
    )  # don t set default here

    def save(self, *args, **kwargs):
        # Génère le QR code avant de sauvegarder
        if not self.qr_code:  # Vérifie si un QR code n'a pas déjà été assigné
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        """Génère et sauvegarde un QR code unique basé sur le NSS du patient."""
        if not self.patient or not self.patient.NSS:
            raise ValueError("Le NSS du patient est requis pour générer un QR code.")

        # Generate QR code data and image
        nom_patient = self.patient.utilisateur.last_name
        prenom_patient = self.patient.utilisateur.first_name
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.patient.NSS)  # NSS as QR code data
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Génère un chemin unique pour le fichier avec prénom et nom
        unique_filename = f"qrcodes/{nom_patient}_{prenom_patient}_{self.patient.NSS}_qrcode_{uuid.uuid4().hex}.png"
        self.qr_code.save(unique_filename, ContentFile(buffer.getvalue()), save=False)

        # Represents a summary of medical information

        # Create a unique filename for the QR code
        unique_filename = f"qrcodes/{nom_patient}_{prenom_patient}_{self.patient.NSS}_qrcode_{uuid.uuid4().hex}.png"
        self.qr_code.save(unique_filename, ContentFile(buffer.getvalue()), save=False)


# Represents a summary of medical information
class Resume(models.Model):
    diagnostic = models.TextField(blank=True, null=True)  # Diagnostic details
    symptomes = models.TextField(blank=True, null=True)  # Symptoms
    antecedents = models.TextField(blank=True, null=True)  # Medical history
    autres_informations = models.TextField(blank=True, null=True)  # Other information

    def __str__(self):
        return "Résumé"


# Represents a prescription document
class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True)
    date_prescription = models.DateField()  # Date of prescription
    etat_ordonnance = models.BooleanField(default=False)  # Validation status


class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)
    dpi = models.ForeignKey(DPI, related_name="consultations", on_delete=models.CASCADE)
    date_consult = models.DateField()
    resume = models.OneToOneField(
        Resume, related_name="consultation", on_delete=models.CASCADE
    )
    ordonnance = models.OneToOneField(
        Ordonnance, related_name="consultation", on_delete=models.CASCADE
    )

    # Add bilanRadiologue and bilanBiologique, allowing them to be null
    bilan_radiologue = models.ForeignKey(
        "BilanRadiologique",
        related_name="consultations",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    bilan_biologique = models.ForeignKey(
        "BilanBiologique",
        related_name="consultations",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Consultation {self.id_consultation} pour DPI {self.dpi.id_dpi}"


# Represents a prescription within an ordonnance
class Prescription(models.Model):
    id_prescription = models.AutoField(primary_key=True)
    ordonnance = models.ForeignKey(
        Ordonnance, related_name="prescriptions", on_delete=models.CASCADE
    )
    dose = models.CharField(max_length=50)
    duree = models.CharField(max_length=50)
    medicament = models.OneToOneField(
        Medicament, related_name="prescription", on_delete=models.CASCADE, default=1
    )


"""class BilanBiologique(models.Model):
    id_bilanbiologique = models.AutoField(primary_key=True)
    description = models.TextField(default="")
    parametres = models.ManyToManyField('ParametreBiologique', related_name="bilans_biologiques")
    laborantin = models.ForeignKey('Laborantin', related_name="bilanbiologiques", on_delete=models.CASCADE,null=True,)

class ParametreBiologique(models.Model):
    id_parametrebiologique = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    unite_mesure = models.CharField(max_length=20)
    valeur_normale = models.CharField(max_length=100)

class ParametreBioMesure(models.Model):
    id_parametrebiomesure = models.AutoField(primary_key=True)
    parametre_biologique = models.ForeignKey('ParametreBiologique', on_delete=models.CASCADE, related_name="mesures")
    bilan_biologique = models.ForeignKey('BilanBiologique', on_delete=models.CASCADE, related_name="parametre_bio_mesures")
    valeur_mesuree = models.CharField(max_length=100)
    date_mesure = models.DateField()"""


class BilanBiologique(models.Model):
    id_bilanbiologique = models.AutoField(primary_key=True)
    description = models.TextField(default="")
    # One BilanBiologique can have many ParametreBioMesure instances
    parametres_bio_mesures = models.ManyToManyField(
        "ParametreBioMesure", related_name="bilans_biologiques"
    )
    laborantin = models.ForeignKey(
        "Laborantin",
        related_name="bilanbiologiques",
        on_delete=models.CASCADE,
        null=True,
    )


class ParametreBioMesure(models.Model):
    id_parametrebiomesure = models.AutoField(primary_key=True)
    # Linking to a single BilanBiologique
    bilan_biologique = models.ForeignKey(
        "BilanBiologique",
        on_delete=models.CASCADE,
        related_name="parametre_bio_mesures",
    )
    nom = models.CharField(max_length=100)
    unite_mesure = models.CharField(max_length=20)
    valeur_normale = models.CharField(max_length=100)
    valeur_mesuree = models.CharField(max_length=100)
    date_mesure = models.DateField()

    # This ensures each ParametreBioMesure is only linked to one BilanBiologique
    """class Meta:
        unique_together = ('bilan_biologique', 'nom')  # Prevents a BilanBiologique from being linked to the same ParametreBioMesure twice"""


class BilanRadiologique(models.Model):
    id_bilanradiologique = models.AutoField(primary_key=True)
    description = models.TextField(default="")
    type = models.TextField(default="")
    compte_rendu = models.TextField()
    radiologue = models.ForeignKey(
        "Radiologue",
        related_name="bilanradiologiques",
        on_delete=models.CASCADE,
        null=True,
    )


class RadiologyImage(models.Model):
    id_image = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="radiologies/")
    bilan_radiologique = models.ForeignKey(
        BilanRadiologique, related_name="images", on_delete=models.CASCADE
    )


# Represents a nursing care record
class Soin(models.Model):
    id_soin = models.AutoField(primary_key=True)
    dpi = models.ForeignKey(DPI, related_name="soins", on_delete=models.CASCADE)
    infirmier = models.ForeignKey(
        Infirmier, related_name="soins", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)  # Description du soin
    date_soin = models.DateField()  # Date du soin
    observation = models.TextField()
