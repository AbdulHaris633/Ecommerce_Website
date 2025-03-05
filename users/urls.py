from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
       path('login/', views.custom_login_view, name='login'), 
       path('register/', views.register, name='register'),
       path('logout/', views.custom_logout_view, name='logout'),
]             