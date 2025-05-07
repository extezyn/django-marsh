from django.shortcuts import render

from .permission import CustomPermissions, PaginationPage
from .serializers import *
from rest_framework import viewsets
from shop.models import * 
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class DamageReportViewSet(viewsets.ModelViewSet):
    queryset = DamageReport.objects.all()
    serializer_class = DamageReportSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = Pos_order.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage