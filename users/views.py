from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],  
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            UserProfile.objects.create(user=user)
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('users:login')  # Replace with your login URL
    else:
        form = RegistrationForm() 
    return render(request, "users/register.html", {"form": form}) 

      
def custom_login_view(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Session Data:", request.session.items()) 
                messages.success(request, f"Welcome back, {username}!")
                return redirect('homepage1')  # Or another valid URL 
            else:
                messages.error(request, "Invalid username or password.") 
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()     
    return render(request, 'users/login.html', {'form': form}) 

                
def custom_logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/users/login/')    