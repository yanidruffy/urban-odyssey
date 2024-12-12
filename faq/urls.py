from django.urls import path
from . import views

app_name = "faq"

urlpatterns = [
    path("", views.faq_list, name="faq_list"),
    path("add/", views.add_faq, name="add_faq"),
    path("edit/<int:id>/", views.edit_faq, name="edit_faq"),
    path("delete/<int:id>/", views.delete_faq, name="delete_faq"),
]
