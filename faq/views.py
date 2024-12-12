from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faq.models import Faq
from .forms import FaqForm


def faq_list(request):
    """View for the FAQ page"""
    if request.user.is_superuser:
        faqs = Faq.objects.all().order_by("-created")
    else:
        faqs = Faq.objects.filter(published=True).order_by("-created")
    return render(request, "faq/faq.html", {"faqs": faqs})


@login_required
def add_faq(request):
    """View for adding a new FAQ"""
    if not request.user.is_superuser:
        messages.error(
            request,
            "You do not have permission to access this page.")
        return redirect("fag:faq_list")

    if request.method == "POST":
        faq_form = FaqForm(request.POST)
        if faq_form.is_valid():
            faq_form.save()
            messages.success(request, "FAQ added successfully.")
            return redirect("faq:faq_list")
        else:
            messages.error(request, "Sorry, you are not authorised.")
    else:
        faq_form = FaqForm()
    return render(request, "faq/add_faq.html", {"faq_form": faq_form})


@login_required
def edit_faq(request, id):
    """View to edit a FAQ"""
    faq = get_object_or_404(Faq, id=id)
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this FAQ.")
        return redirect("faq:faq_list")

    if request.method == "POST":
        faq_form = FaqForm(request.POST, instance=faq)
        if faq_form.is_valid():
            faq_form.save()
            messages.success(request, "FAQ updated successfully!")
            return redirect("faq:faq_list")
        else:
            messages.error(
                request,
                "Something went wrong. Editing FAQ failed.")
    else:
        faq_form = FaqForm(instance=faq)
        messages.info(request, f"You are editing {faq.question}")

    return render(request, "faq/edit_faq.html", {"faq_form": faq_form})


@login_required
def delete_faq(request, id):
    """View to delete a FAQ"""
    faq = get_object_or_404(Faq, id=id)
    if not request.user.is_superuser:
        messages.error(
            request,
            "You do not have permission to delete this FAQ.")
        return redirect("faq:faq_list")

    if request.method == "POST":
        faq.delete()
        messages.success(request, "FAQ deleted successfully!")
        return redirect("faq:faq_list")

    return render(request, "faq/confirm_delete_faq.html", {"faq": faq})
