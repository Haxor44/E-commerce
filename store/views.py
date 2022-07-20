from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerialize
from shop.models import Product

# Create your views here.
@api_view()
def product(request):
	return Response('Ok')

@api_view()
def product_detail(request,id):
	try:
		product = Product.objects.get(pk=id)
		serialize = ProductSerialize(product)
		return Response(serialize.data)
	except Product.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)