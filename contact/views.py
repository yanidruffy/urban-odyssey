from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact_us(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			contact_form.save()
			messages.success(request, 'Your message has been sent successfully. Thank you for contacting us.')
			return redirect('contact:contact_us')
	else:
		contact_form = ContactForm()
	return render(request, 'contact/contact_us.html', {'contact_form': contact_form})
