from django.urls import path
from .views import add_to_wishlist, wishlist, wishlist_delete

urlpatterns = [
    path(
        'wishlist/add/coffee/<int:coffee_id>/',
        add_to_wishlist, name='add_coffee_to_wishlist'),
    path(
        'wishlist/add/accessory/<int:accessory_id>/',
        add_to_wishlist, name='add_accessory_to_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),
    path(
        'wishlist/delete/<int:item_id>/',
        wishlist_delete, name='wishlist-delete'),
]
