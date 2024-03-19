from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Collection
		fields=['id', 'title']
	# id = serializers.IntegerField()
	# title = serializers.CharField(max_length=255)

# class ProductSerializer(serializers.Serializer):
# 	id = serializers.IntegerField()
# 	title = serializers.CharField(max_length=255)
# 	price = serializers.DecimalField(source='unit_price',max_digits=6, decimal_places=2)
# 	price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
# 	Collection = CollectionSerializer( )
class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=Product
		fields=['id', 'title', 'unit_price', 'price_with_tax']
	price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

	def calculate_tax(self, product: Product):
		return product.unit_price * Decimal(1.1) 