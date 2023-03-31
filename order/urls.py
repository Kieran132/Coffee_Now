from django.urls import path
from . import views

urlpatterns = [
    path('coffee_list/', views.coffee_list, name='coffee_list'),
    path('coffee_detail/', views.coffee_detail, name='coffee_detail'),
]
