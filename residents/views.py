from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resident

# Create your views here.

@login_required
def resident_list(request):
    residents = Resident.objects.all()
    return render(request, 'residents/resident_list.html', {'residents': residents})

@login_required
def resident_detail(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    return render(request, 'residents/resident_detail.html', {'resident': resident})
