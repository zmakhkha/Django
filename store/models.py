from django.db import models

class Promotion(models.Model):
	description = models.CharField(max_length=255)
	discount = models.FloatField()
	#product_set 
class collection(models.Model):
	title = models.CharField(max_length=255)
	# featured_product = models.ForeignKey(
	# 	'Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
	#sku = models.CharField(max_length=10, primary_key=True) # this will replace the primary key
	title=models.CharField(max_length=255)
	slug = models.SlugField(default='-')
	description=models.TextField()
	price=models.DecimalField(max_digits=6, decimal_places=2)
	inventory = models.IntegerField()
	last_update=models.DateTimeField(auto_now = True)
	collection = models.ForeignKey(collection, on_delete=models.PROTECT)
	Promotions = models.ManyToManyField(Promotion)

class Costomer(models.Model):
	MEMBERSHIP_BRONZE = 'B'
	MEMBERSHIP_SILVER = 'S'
	MEMBERSHIP_GOLD = 'G'
	MEMBERSHIP_CHOICES=[
		(MEMBERSHIP_BRONZE, 'BRONZE'),
		(MEMBERSHIP_SILVER, 'SILVER'),
		(MEMBERSHIP_GOLD, 'GOLD'),
	]
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=255)
	birth_date= models.DateField(null = True)
	membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
	collection = models.ForeignKey(collection, on_delete=models.PROTECT)


class Order(models.Model):
	PAYEMENT_PENDING= 'P'
	PAYEMENT_COMPLETE= 'C'
	PAYEMENT_FAILED= 'F'
	PAYEMENT_STATUS = [
		(PAYEMENT_PENDING, 'PENDING'),
		(PAYEMENT_COMPLETE, 'COMPLETE'),
		(PAYEMENT_FAILED, 'FAILED'),
	]
	placed_at=models.DateTimeField(auto_now_add = True)
	payement_satus=models.CharField(max_length=1, choices=PAYEMENT_STATUS, default=PAYEMENT_PENDING)

class Adress(models.Model):
	street = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	costumer = models.OneToOneField(Costomer, on_delete=models.CASCADE, primary_key = True)

class OrderItem():
	order = models.ForeignKey(Order, on_delete=models.PROTECT)
	product = models.ForeignKey(Product, on_delete=models.PROTECT)
	quantity = models.PositiveSmallIntegerField()
	unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveSmallIntegerField