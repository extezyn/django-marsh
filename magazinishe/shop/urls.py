from django.urls import path
from .views import *

urlpatterns = [
    path('main', main_view, name = 'main_view'),

    path('contact', contact_view, name = 'contact_view'),

    path ('about', about_view, name = 'about_view'),

    path ('cart', cart_view, name = 'cart_view'),

    path('products', products_view, name = 'products_view'),

    path('categories', categories_view, name = 'categories_view'),

    path('clothes/', ClothesListView.as_view(), name = 'clothes_list'),

    path('clothes/<int:pk>/', ClothesDetailView.as_view(), name = 'clothes_detail'),

    path ('clothes<int:pk>/update/', ClothesUpdateView.as_view(), name = 'clothes_update'),

    path ('clothes<int:pk>/delete/', ClothesDeleteView.as_view(), name = 'clothes_delete'),
]
