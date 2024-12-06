import re
from decimal import Decimal
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from rest_framework.templatetags.rest_framework import items

from auto_parts.templatetags.multiplication import total_in_kes
from user_authentication.models import CustomUser
from .models import Order

def confirm_order(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        address = request.POST.get('address')
        total_price = request.POST.get('total_price')
        product = request.POST.get('product')

        try:
            # Validate & convert the total price input
            total_price = Decimal(total_price)

            # Regular expression for validating an email
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

            # Validate email address
            if not re.match(email_regex, email):
                return HttpResponse('Invalid email address', status=400)

            # Create the order instance
            order = Order(
                phone=email,
                address=address,
                total_price=total_price,
                status='Pending',
                payment_method='Pay on Delivery'
            )
            order.save()

            # Prepare the email message
            email_message = (
                f'Order Details:\n\n'  
                f'Email: {email}\n'  
                f'Address: {address}\n'  
                f'Total Price: {total_price}\n'  
                f'Items: {product}'  
                f'message: Your order is under delivery and will soon arrive at your address. Keep an eye on your notifications.'
                f' Thank you for making an order with us.'
                f'Best regards, G Motions. Your one stop for all motion products and companion in your motion.'

            )
            html_message = (
                f"<p>Dear customer,</p>"
                f"<p>Thank you for your order of {total_price} for {order}</p>"
                f"<p>Your payment order number is {order.id}</p>"
                f"<p>Your order is under delivery and will soon arrive at your address. Keep an eye on your notifications.</p>"
                f"<p>Thank you for making an order with us</p>"
                f"<p>Best regards, G Motions. Your one stop for all motion products and companion in your motion.</p>"
            )
            print("Payment receipt email sent successfully")

            # Send confirmation email
            send_mail(
                subject='Your Order Confirmation',
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
                html_message=html_message
            )
            print("Payment receipt email sent successfully")

            return redirect('thank_you')  # Redirect to thank you page after successful order
        except ValueError as e:
            return HttpResponse(f'Invalid value provided: {e}', status=400)
        except Exception as e:
            return HttpResponse(f'Error processing order: {e}', status=500)

    return HttpResponse('Invalid request method', status=405)

def payment_selection(request):
    amount = request.GET.get('amount')
    currency = request.GET.get('currency')
    print(f"Amount: {amount}, Currency: {currency}")
    return render(request, 'payments/payments_selection.html', {'amount': amount, 'currency': currency})


def pay_on_delivery(request):
    return render(request, 'payments/confirm_order_form.html')  # Create this template


def thank_you(request):
    return render(request, "payments/Thank you.html")

def mpesa_payment(request):
    return render(request, 'payments/unavailable_method.html')