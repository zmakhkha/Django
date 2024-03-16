from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
def hello(request):
	query_set = Product.objects.filter(title__icontains='coffee')
	return render(request, 'hello.html', {"name" : "zmakhkha", 'products':list(query_set)})