from django.shortcuts import render
from faq.models import Faq

# Create your views here.

def faq_list(request):
	"""View for the FAQ page"""
	faqs = Faq.objects.filter(published=True).order_by('-created')
	return render(request, 'faq/faq.html', {'faqs': faqs})
