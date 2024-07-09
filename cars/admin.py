from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)
    list_filter = ('brand',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
