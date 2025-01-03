<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 5.1.3 on 2024-12-29 15:17
=======
# Generated by Django 5.1.4 on 2025-01-03 10:50
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
=======
# Generated by Django 5.1.4 on 2025-01-01 22:32
>>>>>>> mary

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> mary
            name='Medicament',
            fields=[
                ('id_medicament', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
            name='Ordonnance',
            fields=[
                ('id_ordonnance', models.AutoField(primary_key=True, serialize=False)),
                ('date_prescription', models.DateField()),
                ('etat_ordonnance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic', models.TextField(blank=True, null=True)),
                ('symptomes', models.TextField(blank=True, null=True)),
                ('antecedents', models.TextField(blank=True, null=True)),
                ('autres_informations', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Infirmier',
            fields=[
                ('id_infirmier', models.AutoField(primary_key=True, serialize=False)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Laborantin',
            fields=[
                ('id_laborantin', models.AutoField(primary_key=True, serialize=False)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BilanBiologique',
            fields=[
                ('id_bilanbiologique', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(default='')),
                ('laborantin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bilanbiologiques', to='gestiondpi.laborantin')),
            ],
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id_medecin', models.AutoField(primary_key=True, serialize=False)),
                ('specialite', models.CharField(max_length=100)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParametreBioMesure',
            fields=[
                ('id_parametrebiomesure', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('unite_mesure', models.CharField(max_length=20)),
                ('valeur_normale', models.CharField(max_length=100)),
                ('valeur_mesuree', models.CharField(max_length=100)),
                ('date_mesure', models.DateField()),
                ('bilan_biologique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parametre_bio_mesures', to='gestiondpi.bilanbiologique')),
            ],
        ),
        migrations.AddField(
            model_name='bilanbiologique',
            name='parametres_bio_mesures',
            field=models.ManyToManyField(related_name='bilans_biologiques', to='gestiondpi.parametrebiomesure'),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_patient', models.AutoField(primary_key=True, serialize=False)),
                ('NSS', models.CharField(max_length=20, unique=True)),
                ('date_de_naissance', models.DateField()),
                ('adresse', models.TextField()),
                ('telephone', models.CharField(max_length=15)),
                ('mutuelle', models.CharField(max_length=100)),
                ('personne_a_contacter', models.CharField(max_length=100)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DPI',
            fields=[
                ('id_dpi', models.AutoField(primary_key=True, serialize=False)),
<<<<<<< HEAD
<<<<<<< HEAD
                ('antecedents', models.TextField(blank=True)),
=======
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
=======
                ('antecedents', models.TextField(blank=True)),
>>>>>>> mary
                ('qr_code', models.ImageField(unique=True, upload_to='qrcodes/')),
                ('medecin', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='medcin', to='gestiondpi.medecin')),
                ('patient', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestiondpi.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PharmacienHospitalier',
            fields=[
                ('id_pharmacienHospitalier', models.AutoField(primary_key=True, serialize=False)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id_prescription', models.AutoField(primary_key=True, serialize=False)),
                ('dose', models.CharField(max_length=50)),
                ('duree', models.CharField(max_length=50)),
<<<<<<< HEAD
<<<<<<< HEAD
                ('medicament', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='gestiondpi.medicament')),
=======
                ('medicament', models.CharField(default='Default Value', max_length=100)),
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
=======
                ('medicament', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='gestiondpi.medicament')),
>>>>>>> mary
                ('ordonnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='gestiondpi.ordonnance')),
            ],
        ),
        migrations.CreateModel(
            name='Radiologue',
            fields=[
                ('id_radiologue', models.AutoField(primary_key=True, serialize=False)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BilanRadiologique',
            fields=[
                ('id_bilanradiologique', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(default='')),
                ('type', models.TextField(default='')),
                ('compte_rendu', models.TextField()),
                ('radiologue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bilanradiologiques', to='gestiondpi.radiologue')),
            ],
        ),
        migrations.CreateModel(
            name='RadiologyImage',
            fields=[
                ('id_image', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='radiologies/')),
                ('bilan_radiologique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gestiondpi.bilanradiologique')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id_consultation', models.AutoField(primary_key=True, serialize=False)),
                ('date_consult', models.DateField()),
                ('bilan_biologique', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultations', to='gestiondpi.bilanbiologique')),
                ('bilan_radiologue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultations', to='gestiondpi.bilanradiologique')),
                ('dpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='gestiondpi.dpi')),
<<<<<<< HEAD
<<<<<<< HEAD
                ('ordonnance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='gestiondpi.ordonnance')),
=======
                ('ordonnance', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='gestiondpi.ordonnance')),
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
=======
                ('ordonnance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='gestiondpi.ordonnance')),
>>>>>>> mary
                ('resume', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='gestiondpi.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Soin',
            fields=[
                ('id_soin', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('date_soin', models.DateField()),
                ('observation', models.TextField()),
                ('dpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soins', to='gestiondpi.dpi')),
                ('infirmier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soins', to='gestiondpi.infirmier')),
            ],
        ),
    ]
