from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Complaint

# Create your views here.

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['respondent_name', 'complaint_details']
        widgets = {
            'complaint_details': forms.Textarea(attrs={'rows': 4}),
        }

@login_required
def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})

@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'complaints/complaint_detail.html', {'complaint': complaint})

@login_required
def file_complaint(request):
    if request.user.role != 'resident':
        messages.error(request, 'Only residents can file complaints.')
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.complainant = request.user.resident
            complaint.save()
            messages.success(request, 'Complaint filed successfully.')
            return redirect('complaints:my_complaints')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/file_complaint.html', {'form': form})

@login_required
def my_complaints(request):
    if request.user.role != 'resident':
        messages.error(request, 'Access denied.')
        return redirect('core:dashboard')
    
    complaints = Complaint.objects.filter(complainant=request.user.resident)
    return render(request, 'complaints/my_complaints.html', {'complaints': complaints})

@login_required
def resolve_complaint(request, pk):
    if request.user.role not in ['staff', 'admin']:
        messages.error(request, 'Only staff can resolve complaints.')
        return redirect('core:dashboard')
    
    complaint = get_object_or_404(Complaint, pk=pk)
    complaint.status = 'resolved'
    complaint.save()
    messages.success(request, 'Complaint marked as resolved.')
    return redirect('complaints:complaint_list')

@login_required
def delete_complaint(request, pk):
    if request.user.role not in ['staff', 'admin']:
        messages.error(request, 'Only staff can delete complaints.')
        return redirect('core:dashboard')
    
    complaint = get_object_or_404(Complaint, pk=pk)
    complaint.delete()
    messages.success(request, 'Complaint deleted successfully.')
    return redirect('complaints:complaint_list')
