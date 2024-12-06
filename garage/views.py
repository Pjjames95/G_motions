from django.shortcuts import render,redirect
from .forms import GarageForms, ComplainMessageForm
from .models import Garage_services, ComplainMessage
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def garages_list(request):
    garage_services = Garage_services.objects.all()
    return render(request, 'garage/garages_list.html', {'garage_services': garage_services})

@user_passes_test(lambda u: u.is_superuser)
def add_garage(request):
    form = GarageForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Service added successfully')
        return redirect('garages_list')
    else:
        form = GarageForms()
    return render(request, 'garage/add_garage.html', {'form': form})

def complaint(request):
    if request.method == 'POST':
        form = ComplainMessageForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ComplainMessage.objects.create(email=email, message=message)
            messages.success(request, 'Complaint was sent successfully.')
            return redirect('complaint_success')
        else:
            messages.error(request, 'There was an error submitting your complaint. Please correct the errors below.')

    else:
        form = ComplainMessageForm()

    return render(request, 'garage/complaint.html', {'form': form})

def complaint_success(request):
    return render(request, 'garage/complaint_success.html')
