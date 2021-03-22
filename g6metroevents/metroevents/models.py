from django.db import models

# Create your models here.

class Person(models.Model):
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length=100)
	firstName = models.CharField(max_length = 100)
	middleName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	address = models.CharField(max_length = 300)
	#profilePicture = 
	isDisabled = models.IntegerField(default = 0)