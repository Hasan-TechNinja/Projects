from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from . forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages

# Create your views here.

def HomeView(request):
    
    return render(request, 'home.html')


def RegistrationView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = CustomUserCreationForm()

    context = {
        'form':form
    }
    return render(request, 'registration.html', context)



def LoginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # Redirect to the home page or wherever you want
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()

    context = {
        'form':form
    }
    return render(request, 'login.html', context)



def LogoutView(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')