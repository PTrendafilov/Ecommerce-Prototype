from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('contacts/', views.contacts, name='contacts'),
    path('discounts/', views.discounts, name='discounts'),

    path('products/', views.products, name='products'),

    path('product', views.product, name='product'),

    path('update_item/', views.updateItem, name='update_item'),
]