from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products:product_list'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q6BCvAJF78M6q6g5a5jqqe8cNU51mG7IdTmfeH7GPBayqkAAD0EdcYYBm8Rhd4daEV30DA3NkmxX2F3zgdd6GOc00YGsX7FDe',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)