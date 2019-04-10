from django.urls import path
from .views import get_document

urlpatterns = [
    path('api/get_document', get_document, name="get_document"),
]