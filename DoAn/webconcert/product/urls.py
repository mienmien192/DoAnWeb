from django.contrib import admin  
from django.urls import path  
from . import views  

urlpatterns = [
    path('',views.pro),
    path('search', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
