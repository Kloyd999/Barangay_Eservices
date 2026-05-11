from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import ServiceRequest

# Create your views here.

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'purpose']
        widgets = {
            'purpose': forms.Textarea(attrs={'rows': 4}),
        }

@login_required
def service_list(request):
    services = ServiceRequest.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def service_detail(request, pk):
    service = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

@login_required
def request_service(request):
    if request.user.role != 'resident':
        messages.error(request, 'Only residents can request services.')
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.resident = request.user.resident
            service_request.save()
            messages.success(request, 'Service request submitted successfully.')
            return redirect('services:my_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/request_service.html', {'form': form})

@login_required
def my_requests(request):
    if request.user.role != 'resident':
        messages.error(request, 'Access denied.')
        return redirect('core:dashboard')
    
    requests = ServiceRequest.objects.filter(resident=request.user.resident)
    return render(request, 'services/my_requests.html', {'requests': requests})

@login_required
def complete_service(request, pk):
    if request.user.role not in ['staff', 'admin']:
        messages.error(request, 'Only staff can mark services as complete.')
        return redirect('core:dashboard')
    
    service = get_object_or_404(ServiceRequest, pk=pk)
    service.status = 'completed'
    service.save()
    messages.success(request, 'Service request marked as completed.')
    return redirect('services:service_list')

@login_required
def delete_service(request, pk):
    if request.user.role not in ['staff', 'admin']:
        messages.error(request, 'Only staff can delete service requests.')
        return redirect('core:dashboard')
    
    service = get_object_or_404(ServiceRequest, pk=pk)
    service.delete()
    messages.success(request, 'Service request deleted successfully.')
    return redirect('services:service_list')
