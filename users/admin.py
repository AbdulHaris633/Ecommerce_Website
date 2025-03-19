from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsermodel  

class CustomUserAdmin(UserAdmin):
    model = CustomUsermodel
    list_display = ('username', 'email', 'is_staff', 'is_active', "is_superuser")    

admin.site.register(CustomUsermodel, CustomUserAdmin)  
    