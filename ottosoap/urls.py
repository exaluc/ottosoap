from django.conf.urls import url
from rhino.views import saisie_soap_service

urlpatterns = [
    url(r'^api/otto/', saisie_soap_service),
]
