from django.urls import path
from .views import *

urlpatterns = [
    path('main', main_view, name='main_view'),

    path('contact', contact_view, name='contact_view'),

    path ('about', about_view, name='about_view'),

    path ('cart', cart_view, name='cart_view'),

    path('products', products_view, name='products_view'),

    path('categories', categories_view, name='categories_view')
]
