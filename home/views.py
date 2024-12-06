from django.shortcuts import render
from faq.models import Faq

# Create your views here.

def index(request):
	faqs = Faq.objects.filter(published=True).order_by('-created')[:3]
	return render(request, 'home/index.html', {'faqs': faqs})
