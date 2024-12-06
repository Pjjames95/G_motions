from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns = [
    path('cars_list/', views.cars_list, name='cars_list'),
    path('cars_add/', views.cars_add, name='cars_add'),
    path('cars_edit/<int:pk>/', views.cars_edit, name='cars_edit'),
    path('search_car/', views.search_car, name='search_car'),
    path('cars_detail/<int:pk>/', views.cars_detail, name='cars_detail'),
    path('cars_by_make/<str:car_make>/', views.cars_by_make, name='cars_by_make'),
    path('contact_admin/', views.contact_admin, name='contact_admin'),
    path('contact_success', views.contact_success, name='contact_success'),
    path('admin_message_list', views.admin_message_list, name='admin_message_list'),
    path('delete_message/<int:pk>/', views.delete_admin_message, name='delete_message'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)