from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import InputDataViewset

router = routers.DefaultRouter()
router.register("", InputDataViewset, basename="proof_of_concept")

urlpatterns = [
    path('', include(router.urls)),
]