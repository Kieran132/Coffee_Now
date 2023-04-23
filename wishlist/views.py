from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from order.models import CoffeeBean
from accessories.models import Accessory


def add_to_wishlist(request, coffee_id=None, accessory_id=None):
    if coffee_id:
        coffee = CoffeeBean.objects.get(id=coffee_id)
        wishlist = Wishlist(user=request.user, CoffeeBean=coffee)
    elif accessory_id:
        accessory = Accessory.objects.get(id=accessory_id)
        wishlist = Wishlist(user=request.user, Accessory=accessory)
    wishlist.save()
    return redirect('wishlist')


def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})


def wishlist_delete(request, item_id):
    item = get_object_or_404(Wishlist, pk=item_id)
    if item.CoffeeBean:
        product = get_object_or_404(CoffeeBean, pk=item.CoffeeBean.pk)
    elif item.Accessory:
        product = get_object_or_404(Accessory, pk=item.Accessory.pk)
    else:
        return redirect('wishlist')

    item.delete()
    return redirect('wishlist')
