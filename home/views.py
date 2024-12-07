from django.shortcuts import render
from about.models import About
from faq.models import Faq

# Create your views here.

def index(request):
	""" A view to return the index page """
	about = About.objects.first()
	faqs = Faq.objects.filter(published=True).order_by('-created')[:3]

	context = {
		'about': about,
		'faqs': faqs,
	}
	return render(request, 'home/index.html', context)
