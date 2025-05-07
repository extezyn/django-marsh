from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_view, name='main_view'),
    path('contact/', contact_view, name='contact_view'),
    path('about/', about_view, name='about_view'),
    path('cart/', cart_view, name='cart_view'),
    path('products/', products_view, name='products_view'),
    path('categories/', categories_view, name='categories_view'),

    # Equipment 
    path('equipment/', equipmentListView.as_view(), name='equipment_list'),
    path('equipment/create/', equipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/', equipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/<int:pk>/update/', equipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', equipmentDeleteView.as_view(), name='equipment_delete'),
    
    # Employer 
    path('employer/', EmployerListView.as_view(), name='employer_list'),
    path('employer/create/', EmployerCreateView.as_view(), name='employer_create'),
    path('employer/<int:pk>/', EmployerDetailView.as_view(), name='employer_detail'),
    path('employer/<int:pk>/update/', EmployerUpdateView.as_view(), name='employer_update'),
    path('employer/<int:pk>/delete/', EmployerDeleteView.as_view(), name='employer_delete'),
    
    # Client 
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    
    # Payment
    path('payment/', PaymentListView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('payment/<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('payment/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment_update'),
    path('payment/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),
    
    # Rental 
    path('rental/', RentalListView.as_view(), name='rental_list'),
    path('rental/create/', RentalCreateView.as_view(), name='rental_create'),
    path('rental/<int:pk>/', RentalDetailView.as_view(), name='rental_detail'),
    path('rental/<int:pk>/update/', RentalUpdateView.as_view(), name='rental_update'),
    path('rental/<int:pk>/delete/', RentalDeleteView.as_view(), name='rental_delete'),

    path('login/', login_user, name='login_user'),
    path('registration/', registration_user, name='registration_user'),
    path('logout/', logout_user, name='logout_user'),
]