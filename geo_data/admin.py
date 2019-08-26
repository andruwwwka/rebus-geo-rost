from django.contrib import admin
from geo_data.models import Category, GeoObject


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'radius', 'power', 'is_active')
    search_fields = ('name', )
    list_filter = ['is_active', 'power', 'radius']
    ordering = ['name']


class GeoObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address')
    search_fields = ('name',)
    ordering = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(GeoObject, GeoObjectAdmin)
