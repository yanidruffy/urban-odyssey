from django.shortcuts import render
from .models import About

# Create your views here.

def about_view(request):
	""" A view to return the about page """

	about = About.objects.first()

	return render(request, 'about/about.html', {'about': about})
