

from django.urls import path
from .views import payment_selection, pay_on_delivery, confirm_order, thank_you
from .import views

urlpatterns = [
    path('payment_selection/', views.payment_selection, name='payment_selection'),
    path('pay_on_delivery/', views.pay_on_delivery, name='pay_on_delivery'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('mpesa_payment', views.mpesa_payment, name='mpesa_payment'),
]
