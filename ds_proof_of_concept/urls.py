from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import InputDataViewset, BasicDataTestView

router = routers.DefaultRouter()
router.register("input", InputDataViewset, basename="proof_of_concept")

urlpatterns = [
    path('', include(router.urls)),
    url(r'^basic/$', BasicDataTestView.as_view()),
]