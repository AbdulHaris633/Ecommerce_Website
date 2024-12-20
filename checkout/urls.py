from django.urls import path

from .views import checkout

urlpatterns = [
    # Other URLs...
    path("check/", checkout, name="checkout"),
]
