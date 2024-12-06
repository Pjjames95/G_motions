from compileall import compile_path

from django.urls import path
from auto_parts.views import products_list
from adverts.views import cars_list
from garage.views import garages_list
from payments.views import confirm_order, payment_selection
# from payments.views import index, stk_push
from .import views

urlpatterns = [
    path('', views.landing_page, name='app_landing'),
    path('home_view/', views.home_view, name='home_view'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile_update/', views.profile_update_view, name='profile_update'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_page, name='about'),
    path('auto_parts/', products_list, name='auto_parts app'),
    path('adverts/', cars_list, name='adverts app'),
    path('garage/', garages_list, name='garages app'),
    path('payments/', confirm_order, name='payments'),
    path('payments/payment_selection/', payment_selection, name='payment_selection'),
]
