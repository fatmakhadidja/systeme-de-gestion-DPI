from django.urls import path
from .views import AjouterConsultation,RemplirSoin

urlpatterns =[
    path('ajouterConsultation/',AjouterConsultation.as_view(),name='ajouter_consultation'),
    path('remplirSoin/',RemplirSoin.as_view(),name='remplir_Soin')
]


