from django.shortcuts import render, redirect
from .models import Wishlist


def add_to_wishlist(request, coffee_id=None, accessory_id=None):
    if coffee_id:
        wishlist = Wishlist(user=request.user, id=coffee_id)
    elif accessory_id:
        wishlist = Wishlist(user=request.user, id=accessory.id)
    wishlist.save()
    return redirect('wishlist')


def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})
