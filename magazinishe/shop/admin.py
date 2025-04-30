from django.contrib import admin
from .models import * 
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Clothes)
class ClothesCollection(admin.ModelAdmin):
    pass