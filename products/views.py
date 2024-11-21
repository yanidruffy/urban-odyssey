from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def product_list(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }

    return render(request, 'products/list.html', context)