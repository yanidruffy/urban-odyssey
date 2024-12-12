from django.shortcuts import render
from .models import About


def about_view(request):
    """ A view to return the about page """

    about = About.objects.first()
    if not about:
        about = {
            'title': 'About Us',
            'mission': (
                'Our mission is to empower digital nomads '
                'and adventurers with stylish, '
                'durable, and minimalist products.'
            ),
            'history': (
                'Founded with the goal of redefining urban mobility, '
                'we partner with leading brands '
                'to deliver innovative solutions.'
            ),
            'vision': (
                'To become the go-to platform for digital nomads '
                'seeking premium everyday carry solutions.'
            ),
        }
    return render(request, 'about/about.html', {'about': about})
