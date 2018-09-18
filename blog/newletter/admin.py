from django.contrib import admin
from .models import post
# Register your models here.
class postAdmin(admin.ModelAdmin):
	list_display=['title','content','publish','create','update']
	ordering=['create','update']
	search_fields=['title','create','update']
	list_filter=['create','update']
admin.site.register(post,postAdmin)
		