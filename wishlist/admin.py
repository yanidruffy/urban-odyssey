from django.contrib import admin
from .models import Wishlist

# Register your models here.

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_on')
    list_filter = ('added_on',)
    search_fields = ('product__name', 'user__user__username')
    date_hierarchy = 'added_on'
