from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Wishlist

# Create your views here.

@login_required
def wishlist_list(request):
    wishlist_items = Wishlist.objects.filter(user=request.user.userprofile)

    context = {'wishlist_items': wishlist_items}
    return render (request, 'wishlist/wishlist_list.html', context)