from django.contrib import admin

from .models import Fitting_order


class Fitting_orderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Fitting_order._meta.fields]
    list_filter = ['fit_date']
    search_fields = ['phone', 'name']
admin.site.register(Fitting_order,Fitting_orderAdmin)