from django.shortcuts import render
from about.models import About
from faq.models import Faq
from products.models import Product


def index(request):
    """ A view to return the index page """
    about = About.objects.first()
    faqs = Faq.objects.filter(published=True).order_by('-created')[:3]
    top_products = Product.objects.filter(
        available=True, rating__isnull=False).order_by('-rating')[:3]

    context = {
        'about': about,
        'faqs': faqs,
        'top_products': top_products,
    }
    return render(request, 'home/index.html', context)
