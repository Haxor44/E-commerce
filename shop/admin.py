from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'price','inventory_status']
	list_editable = ['price']

	@admin.display(ordering='inventory')
	def inventory_status(self,product):
		if product.inventory < 10 :
			return 'Low'
		return 'Ok'


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
	list_display  = ['customer','date_ordered','complete','transaction_id']

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display  = ['user','first_name','last_name','email','phone','birth_date']