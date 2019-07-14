from django.contrib import admin
from .models import Contarcts, Customers

admin.site.register(Contarcts)
admin.site.register(Customers)
# @admin.register(Contarcts)
# class Contcracts_Admin(admin.ModelAdmin):
#     list_display = ('number_contr', 'customer', 'txt_contact')
#
#
# @admin.register(Customers)
# class Contcracts_Admin(admin.ModelAdmin):
#     list_display = ('inn', 'ogrn', 'name_customer')


# Register your models here.
