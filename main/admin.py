from django.contrib import admin

from .models import City


# Register your models here.
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("city_name",)}
    list_display = ("city_name", "slug")


admin.site.register(City, CityAdmin)
