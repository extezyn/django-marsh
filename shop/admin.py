from django.contrib import admin
from .models import * 
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass

    def display_photo(self, obj):
        return obj.photo and f'<img src="{obj.photo.url}" width="100" />'
    display_photo.allow_tags = True
    display_photo.short_description = 'Фото'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

@admin.register(DamageReport)
class DamageReportAdmin(admin.ModelAdmin):
    pass

    def display_damage_photo(self, obj):
        return obj.photo and f'<img src="{obj.photo.url}" width="100" />'
    display_damage_photo.allow_tags = True
    display_damage_photo.short_description = 'Фото повреждения'

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    pass