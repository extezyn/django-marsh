from .views import *
from rest_framework import routers

urlpatterns = [
    
]

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('equipment', EquipmentViewSet, basename='equipment')
router.register('client', ClientViewSet, basename='client')
router.register('rental', RentalViewSet, basename='rental')
router.register('damagereport', DamageReportViewSet, basename='damagereport')
router.register('payment', PaymentViewSet, basename='payment')
router.register('employee', EmployeeViewSet, basename='employee')
router.register('maintenance', MaintenanceViewSet, basename='maintenance')
router.register('order', OrderViewSet, basename='order')
router.register('pos-order', PosOrderViewSet, basename='pos-order')
urlpatterns += router.urls
