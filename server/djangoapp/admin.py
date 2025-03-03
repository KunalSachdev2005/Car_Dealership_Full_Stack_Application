from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1
    fields = ['name', 'type', 'year', 'engine_type', 'horsepower']


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'engine_type', 'horsepower']
    search_fields = ['name', 'description', 'car_make__name']
    list_filter = ['car_make', 'type', 'year']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'country_of_origin']
    search_fields = ['name', 'description', 'country_of_origin']
    list_filter = ['country_of_origin']
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
