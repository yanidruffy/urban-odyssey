from django.contrib import admin
from .models import Faq

# Register your models here.

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
	list_display = ['question', 'published', 'created', 'updated']
	list_filter = ['published', 'created', 'updated']
	search_fields = ['question', 'answer']
	list_editable = ['published']
	date_hierarchy = 'created'
	ordering = ['published', '-created']
