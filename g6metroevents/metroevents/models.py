from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
	userName = models.CharField(max_length = 100, primary_key=True)
	userPassword = models.CharField(max_length=100)
	lastName = models.CharField(max_length = 100)
	firstName = models.CharField(max_length = 100)
	middleName = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	address = models.CharField(max_length = 300)
	# profilepic = models.ImageField(upload_to = 'media/')
	# isDisabled = models.IntegerField(default = 0)
class Event(models.Model):
	eventID = models.AutoField(primary_key=True)
	eventName = models.CharField(max_length = 100)
	description = models.CharField(max_length=100)
	location = models.CharField(max_length = 100)
	startdate = models.DateField(auto_now_add = True)
	enddate = models.DateField(auto_now_add = True)
	starttime = models.TimeField(default = timezone.now)
	endtime = models.TimeField(default = timezone.now)
	numparticipants = models.CharField(max_length = 300)
	eventType = models.CharField(max_length = 300)
	eventStatus = models.CharField(max_length = 300)

