from django.contrib import admin
from .models import Cars, AdminMessage
from .forms import CarsForm, AdminMessageForm

# Register your models here.
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    form = CarsForm
    list_display = ('car_name', 'car_make', 'car_model', 'property_1', 'property_2', 'description', 'car_image', 'short_description')

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            form.save()
            self.message_user(request, 'Car Added Successfully')

@admin.register(AdminMessage)
class AdminMessageAdmin(admin.ModelAdmin):
    form = AdminMessageForm
    list_display = ('name', 'email', 'message')


