from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.hello),
	path('tfoo/', views.hello),
	path('lala/', views.hello),
	path('no/', views.hello),
]