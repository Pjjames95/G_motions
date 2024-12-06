from django.shortcuts import render, redirect, get_object_or_404

from auto_parts.forms import SearchForm
from .forms import CarsForm, ContactForm
from django.core.mail import send_mail
from .models import Cars, AdminMessage
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

# Display the list of cars
def cars_list(request):
    car_makes = Cars.objects.values_list('car_make', flat=True).distinct()
    return render(request, 'adverts/cars_list.html', {"car_makes": car_makes})


@user_passes_test(lambda u: u.is_superuser)
def cars_add(request):
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Advert added successfully')
            return redirect('cars_list')
    else:
        form = CarsForm()
    return render(request, 'adverts/add_car.html', {"form": form})

def cars_detail(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    return render(request, 'adverts/cars_detail.html', {"car": car})

@user_passes_test(lambda u: u.is_superuser)
def cars_edit(request, pk):
    car = Cars.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Advert edited successfully')
            return redirect('cars_list')
    else:
        form = CarsForm(instance=car)
    return render(request, 'adverts/add_car.html', {"form": form})

def search_car(request):
    form = SearchForm()
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Cars.objects.filter(car_name__icontains=query)
    return render(request, 'adverts/search_car.html', {"form": form, "results": results})

def cars_by_make(request, car_make):
    cars = Cars.objects.filter(car_make=car_make)
    return render(request, 'adverts/cars_by_make.html', {"cars": cars, "car_make": car_make})

def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save the message to the database
            AdminMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'adverts/contact_admin.html', {'form': form})

def contact_success(request):
    return render(request, 'adverts/contact_success.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_message_list(request):
    messages = AdminMessage.objects.all()  # Corrected from "message" to "messages"
    return render(request, 'adverts/admin_message_list.html', {'messages': messages})

@user_passes_test(lambda u: u.is_superuser)
def delete_admin_message(request, pk):
    message = get_object_or_404(AdminMessage, pk=pk)
    message.delete()
    return redirect('admin_message_list')



