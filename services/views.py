from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest

# Create your views here.

@login_required
def service_list(request):
    services = ServiceRequest.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def service_detail(request, pk):
    service = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})
