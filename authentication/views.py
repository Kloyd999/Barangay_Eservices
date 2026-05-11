from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from residents.models import Resident
# Create your views here.

def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('core:dashboard')

        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core:dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        except Exception as e:
            return render(request, 'login.html', {'error': 'Login failed. Please try again.'})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('contact_number')
        purok = request.POST.get('purok')
        address = request.POST.get('address')
        civil_status = request.POST.get('civil_status')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        try:
            user = User.objects.create_user(username=username, password=password, email=email, role='resident')
            Resident.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                birth_date=birth_date,
                gender=gender,
                contact_number=contact_number,
                purok=purok,
                address=address,
                civil_status=civil_status
            )
            login(request, user)
            return redirect('core:dashboard')
        except Exception as e:
            return render(request, 'register.html', {'error': 'Registration failed. Please try again.'})

    return render(request, 'register.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('authentication:login_user')