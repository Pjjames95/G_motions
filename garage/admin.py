from django.contrib import admin
from .models import Garage_services, ComplainMessage
from .forms import GarageForms, ComplainMessageForm


@admin.register(Garage_services)
class GarageAdmin(admin.ModelAdmin):
    form = GarageForms
    list_display = ('garage_name', 'garage_location', 'garage_image', 'garage_contacts')

@admin.register(ComplainMessage)
class ComplainMessageAdmin(admin.ModelAdmin):
    form = ComplainMessageForm
    list_display = ('email', 'message')
    list_filter = ('email', 'message')
    search_fields = ['email']
