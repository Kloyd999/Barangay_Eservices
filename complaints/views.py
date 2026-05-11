from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Complaint

# Create your views here.

@login_required
def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})

@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'complaints/complaint_detail.html', {'complaint': complaint})
