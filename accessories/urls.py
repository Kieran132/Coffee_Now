from django.urls import path
from . import views

urlpatterns = [
    path(
        'coffee_accessories',
        views.coffee_accessories, name='coffee_accessories'),
    path('add_product_b/', views.add_product_b, name="add_product_b"),
    path(
        'edit_product_b/<int:accessory_id>',
        views.edit_product_b, name="edit_product_b"),
]
