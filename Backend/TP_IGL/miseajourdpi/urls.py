from django.urls import path
from .views import AjouterConsultation,RemplirSoin,GetPatients

urlpatterns =[
    path('ajouterConsultation/',AjouterConsultation.as_view(),name='ajouter_consultation'),
    path('remplirSoin/',RemplirSoin.as_view(),name='remplir_Soin'),
    path('getPatients/',GetPatients.as_view(),name='get_patients')
]


