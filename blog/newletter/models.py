from django.db import models
from django.utils import timezone
# Create your models here.

def update_location(instance,filename):
	return "%s/%s" %(instance.id,filename)

class post(models.Model):
	title=models.CharField(max_length=150)
	content=models.TextField()
	image=models.ImageField(upload_to=update_location,null=True,blank=True)
	publish=models.DateField(default=timezone.now)
	create=models.DateField(auto_now_add=True)
	update=models.DateField(auto_now=True)
	def __str__(self):
		return self.title

