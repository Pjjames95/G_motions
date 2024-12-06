from django import template
from decimal import Decimal, InvalidOperation

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return Decimal(value) * Decimal(arg)
    except (ValueError, TypeError, InvalidOperation):
        return Decimal('0.00')

@register.filter
def to_kes(value, conversion_rate=Decimal('112.50')):
    try:
        return Decimal(value) * conversion_rate
    except (ValueError, TypeError, InvalidOperation):
        return Decimal('0.00')

@register.filter
def total_in_kes(price, quantity, conversion_rate=Decimal('112.50')):
    try:
        total = Decimal(price) * Decimal(quantity)
        return total * conversion_rate
    except (ValueError, TypeError, InvalidOperation):
        return Decimal('0.00')

@register.filter
def total_price(items):
    try:
        return sum(Decimal(item.product.price) * Decimal(item.quantity) for item in items)
    except (ValueError, TypeError, InvalidOperation):
        return Decimal('0.00')

@register.filter
def total_price_in_kes(items, conversion_rate=Decimal('112.50')):
    try:
        total_usd = sum(Decimal(item.product.price) * Decimal(item.quantity) for item in items)
        return total_usd * conversion_rate
    except (ValueError, TypeError, InvalidOperation):
        return Decimal('0.00')
