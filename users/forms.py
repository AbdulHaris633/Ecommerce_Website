from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUsermodel

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is required

    class Meta:
        model = CustomUsermodel
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUsermodel.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email      
       