from django.urls import path
from . import views

urlpatterns = [
    path('coffee_list/', views.coffee_list, name='coffee_list'),
    path('coffee_detail/<int:id>', views.coffee_detail, name='coffee_detail'),
    path('add/', views.add_product, name="add_product"),
    path('edit/<int:coffee_id>', views.edit_product, name="edit_product"),
    path(
        'delete/<int:id>/',
        views.delete_product, name='delete_product'),
]
