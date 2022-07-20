from rest_framework import serializers

class ProductSerialize(serializers.Serializer):
	"""docstring for ProductSerialize"""
	id = serializers.IntegerField()
	title = serializers.CharField(max_length=255)
	unit_price = serializers.DecimalField(max_digits=6,decimal_places=2)