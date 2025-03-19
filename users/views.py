from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib import messages

def user_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('users:login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})   

def user_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            
           
            if user.is_superuser:
                return redirect("homepage2")   
            else:
                return redirect("homepage1")  

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "users/login.html")  

def user_logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("users:login")   