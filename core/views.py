from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    username = request.user.username
    role = request.user.role

    context = {
        'username': username,
        'role': role,
    }
    return render(request, 'dashboard.html', context)