from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('<slug:category_slug>/', views.product_list, name='category_product_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]