from django.urls import path

from .views import checkout

urlpatterns = [
    path("check/", checkout, name="checkout"),
]
