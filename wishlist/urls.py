from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist_list, name='wishlist_list'),
    path('add/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('delete/', views.delete_wishlist, name='delete_wishlist'),
]
