from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Wishlist


@login_required
def wishlist_list(request):
    wishlist_items = Wishlist.objects.filter(user=request.user.userprofile)

    context = {"wishlist_items": wishlist_items}
    return render(request, "wishlist/wishlist_list.html", context)


@login_required
def add_to_wishlist(request, id):
    """Add a product to the user's wishlist"""
    product = get_object_or_404(Product, id=id)

    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user.userprofile, product=product
    )

    if created:
        messages.success(
            request, f"{product.name} added to your wishlist!"
        )
    else:
        messages.info(
            request, f"{product.name} is already in your wishlist."
        )

    return redirect(
        "products:product_detail", id=product.id, slug=product.slug
    )


@login_required
def remove_from_wishlist(request, id):
    """Remove a product from the user's wishlist"""
    product = get_object_or_404(Product, id=id)
    wishlist_item = Wishlist.objects.filter(
        user=request.user.userprofile, product=product
    ).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(
            request, f"{product.name} removed from your wishlist!"
        )
    else:
        messages.error(
            request, f"{product.name} was not in your wishlist."
        )

    return redirect("wishlist:wishlist_list")


@login_required
def delete_wishlist(request):
    """Delete all items from the user's wishlist with confirmation"""
    wishlist_items = Wishlist.objects.filter(user=request.user.userprofile)

    if not wishlist_items.exists():
        messages.info(request, "Your wishlist is already empty.")
        return redirect("wishlist:wishlist_list")

    if request.method == "POST":
        wishlist_items.delete()
        messages.success(request, "Your wishlist has been cleared!")
        return redirect("wishlist:wishlist_list")

    return render(
        request, "wishlist/confirm_delete.html", {"wishlist": wishlist_items}
    )
