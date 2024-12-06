from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faq.models import Faq
from .forms import FaqForm

# Create your views here.

def faq_list(request):
	"""View for the FAQ page"""
	faqs = Faq.objects.filter(published=True).order_by('-created')
	return render(request, 'faq/faq.html', {'faqs': faqs})

@login_required
def add_faq(request):
	"""View for adding a new FAQ"""
	if not request.user.is_superuser:
		messages.error(request, "You do not have permission to access this page.")
		return redirect('fag:faq_list')

	if request.method == 'POST':
		faq_form = FaqForm(request.POST)
		if faq_form.is_valid():
			faq_form.save()
			messages.success(request, "FAQ added successfully.")
			return redirect('faq:faq_list')
	else:
		faq_form = FaqForm()
	return render(request, 'faq/add_faq.html', {'faq_form': faq_form})
