from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from adverts import admin
from .import views

urlpatterns = [
    path('add_garage', views.add_garage, name='add_garage'),
    path('garage_list', views.garages_list, name='garage_list'),
    path('complaint', views.complaint, name='complaint'),
    path('complaint_success', views.complaint_success, name='complaint_success'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
