from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name']
	ordering = ['first_name','last_name']
	search_fields = ['first_name__istartswith', 'last_name__istartswith']

