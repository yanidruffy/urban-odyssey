from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    list_filter = ('created_at', 'read')
    search_fields = ('name', 'email', 'subject')
    list_editable = ('read',)
    ordering = ('-created_at',)
