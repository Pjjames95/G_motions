from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductsForm, SearchForm
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Products, CartItem, Cart
from django.contrib import messages
from .templatetags.multiplication import total_price_in_kes, total_price
from decimal import Decimal


def products_list(request):
    products = Products.objects.all()
    return render(request, 'auto_parts/products_listing.html', {"products": products})


def search(request):
    form = SearchForm()
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Products.objects.filter(product_name__icontains=query)
    return render(request, 'auto_parts/search_results.html', {'form': form, 'results': results})


@user_passes_test(lambda u: u.is_superuser)
def products_add(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect('products_list')
    else:
        form = ProductsForm()
    return render(request, 'auto_parts/add_products.html', {"form": form})


@user_passes_test(lambda u: u.is_superuser)
def products_edit(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('products_list')
    else:
        form = ProductsForm(instance=product)
    return render(request, 'auto_parts/add_products.html', {"form": form})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'auto_parts/product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart, created = Cart.objects.get_or_create(CustomUser=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem


@login_required
def cart_view(request):
    # Get or create the cart for the logged-in user
    cart, created = Cart.objects.get_or_create(CustomUser=request.user)

    # Fetch cart items
    items = cart.cartitem_set.all()
    print("Cart_items:", items)  # Debugging: Check cart items

    if not items:
        return render(request, 'auto_parts/cart.html', {
            'items': items,
            'total_price': Decimal('0.00'),
            'total_price_in_kes': Decimal('0.00'),
        })

        # Conversion rate
    conversion_rate_kes = Decimal('112.50')

    # Calculate total price in USD
    total_price_usd = sum(item.product.price * item.quantity for item in items)

    # Debugging: Print the total price in USD calculated
    print("Total Price (USD):", total_price_usd)

    # Calculate total price in KES
    total_price_kes = total_price_usd * conversion_rate_kes

    # Debugging: Print the total price in KES calculated
    print("Total Price (KES):", total_price_kes)

    return render(request, 'auto_parts/cart.html', {
        'items': items,
        'total_price': total_price_usd,
        'total_price_in_kes': total_price_kes,
    })


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__CustomUser=request.user)
    cart_item.delete()
    return redirect('cart')
