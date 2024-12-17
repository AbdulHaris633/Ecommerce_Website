from django.urls import path
from .views import checkout,success

urlpatterns = [
    # Other URLs...
    path('check/', checkout, name='checkout'),   
    path('check/payment', success, name='success'),     
           
]