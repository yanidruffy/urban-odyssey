from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, id=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    item_id = str(item_id)

    if item_id in bag:
        bag[str(item_id)] += quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[str(item_id)] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, id=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag:view_bag'))


def remove_from_bag(request, item_id):
    """Remove item from shopping bag"""

    try:
        product = get_object_or_404(Product, id=item_id)
        bag = request.session.get('bag', {})

        if str(item_id) in bag:
            bag.pop(str(item_id))
            messages.success(request, f'Removed {product.name} from your bag')
        else:
            messages.error(request, f'Item not found in the bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
