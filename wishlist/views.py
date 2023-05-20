from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from order.models import CoffeeBean
from accessories.models import Accessory
from django.contrib import messages


def add_to_wishlist(request, coffee_id=None, accessory_id=None):
    """
    This function allows the user to add their chosen product to their wishlist
    by using information from pre-existing models. Once added a pop up message
    appears telling the user they have added a product#
    """
    user = request.user
    coffee = None
    accessory = None

    if coffee_id:
        coffee = get_object_or_404(CoffeeBean, id=coffee_id)
    elif accessory_id:
        accessory = get_object_or_404(Accessory, id=accessory_id)

    # Check if the item already exists in the user's wishlist
    item_exists = Wishlist.objects.filter(
        user=user, CoffeeBean=coffee, Accessory=accessory).exists()

    if item_exists:
        messages.warning(request, "This item is already in your wishlist.")
    else:
        wishlist = Wishlist(user=user, CoffeeBean=coffee, Accessory=accessory)
        wishlist.save()
        messages.success(request, "Item added to wishlist successfully.")

    return redirect('wishlist')


def wishlist(request):
    """
    This function enables to user to view the wishlist page
    """
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})


def wishlist_delete(request, item_id):
    """
    This function allows the user to delete a product from their wishlist page.
    """
    item = get_object_or_404(Wishlist, pk=item_id)
    if item.CoffeeBean:
        product = get_object_or_404(CoffeeBean, pk=item.CoffeeBean.pk)
    elif item.Accessory:
        product = get_object_or_404(Accessory, pk=item.Accessory.pk)
    else:
        return redirect('wishlist')

    item.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect('wishlist')
