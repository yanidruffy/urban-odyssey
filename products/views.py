from django.shortcuts import get_object_or_404, render
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

    return render(request, 'products/product_list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)