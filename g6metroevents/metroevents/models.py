from django.db import models

# Create your models here.

class User(models.Model):
	userName = models.CharField(max_length = 100)
	userPassword = models.CharField(max_length=100)
	lastName = models.CharField(max_length = 100)
	firstName = models.CharField(max_length = 100)
	middleName = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	address = models.CharField(max_length = 300)
	# profilepic = models.ImageField(upload_to = 'media/')
	# isDisabled = models.IntegerField(default = 0)