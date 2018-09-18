from django.contrib import admin
from django.urls import path
from .views import(
	 post_list,
     create,
     contact,
	)
urlpatterns = [
    path('',post_list,name='post_list'),
    path('create/',create,name='create'),
    path('contact/',contact,name='contact'),
]