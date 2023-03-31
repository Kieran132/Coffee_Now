from django.urls import path
from . import views

urlpatterns = [
    path(
        'coffee_accessories/', views.coffee_accessories, name='coffee_accessories'),
]
