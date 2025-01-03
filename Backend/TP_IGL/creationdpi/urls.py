from django.urls import path

<<<<<<< HEAD
from .views import SearchDPIByNSSView, QRCodeScanView

from .views import (
    DPICreationView,
    QRCodeView,
    DPIListView,
    DPIDetailView,
    ConsultDPIView,
)
=======
from creationdpi.views import  SearchDPIByNSSView ,QRCodeScanView

from creationdpi.views import DPICreationView ,QRCodeView , DPIListView ,DPIDetailView , ConsultDPIView
>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path("create-dpi/", DPICreationView.as_view(), name="create_dpi"),
    path("<int:dpi_id>/qrcode/", QRCodeView.as_view(), name="qr_code_download"),
    path("NssSearch/", SearchDPIByNSSView.as_view(), name="search-dpi-by-nss"),
    path("QRCodeSearch/", QRCodeScanView.as_view(), name="qr-code-search"),
    path(
        "consulterdpi/<int:utilisateur_id>/",
        ConsultDPIView.as_view(),
        name="consult_dpi",
    ),
    path("dpis/", DPIListView.as_view(), name="dpi-list"),
    path("dpis/<int:pk>/", DPIDetailView.as_view(), name="dpi-detail"),
=======
    path('create-dpi/', DPICreationView.as_view(), name='create_dpi'),
    path('<int:dpi_id>/qrcode/', QRCodeView.as_view(), name='qr_code_download'),

    path('NssSearch/', SearchDPIByNSSView.as_view(), name='search-dpi-by-nss'),
    path('QRCodeSearch/', QRCodeScanView.as_view(), name='qr-code-search'),


    path('consulterdpi/<int:utilisateur_id>/', ConsultDPIView.as_view(), name='consult_dpi'),


    path('dpis/', DPIListView.as_view(), name='dpi-list'),
    path('dpis/<int:pk>/', DPIDetailView.as_view(), name='dpi-detail'),


>>>>>>> d00efe31b7deaa069ca3991ebafad176a081ced2
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
