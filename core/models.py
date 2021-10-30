from django.db import models

# Create your models here.

class Contact(models.Model):
	date = models.DateField(auto_now=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	
	def __str__(self):
		return self.email