from rest_framework import serializers
from shop.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            'id',
            'name',
            'category',
            'description',
            'price_per_day',
            'deposit',
            'photo',
            'is_available'
        ]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'passport'
        ]

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = [
            'id',
            'equipment',
            'client',
            'start_date',
            'end_date',
            'total_price',
            'is_active'
        ]

class DamageReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamageReport
        fields = [
            'id',
            'rental',
            'description',
            'photo',
            'repair_cost',
            'date_reported'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'rental',
            'amount',
            'payment_date',
            'payment_method'
        ]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'last_name',
            'position',
            'hire_date'
        ]

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = [
            'id',
            'equipment',
            'employee',
            'maintenance_date',
            'description',
            'is_completed'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'daet_create',
            'date_finish',
            'equipment'
        ]

class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'id',
            'equipment',
            'order',
            'count',
            'discount'
        ]