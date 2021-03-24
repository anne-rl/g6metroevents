from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt



# Create your models here.
# class RegularUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
#   # firstname = models.CharField(max_length=100, null=False)
#   # middlename = models.CharField(max_length=100)
#   # lastname = models.CharField(max_length=100, null=False)
#   # password = models.CharField(max_length=100, null=False)
#   # email = models.CharField(max_length=100)
#   # isDeactivated = models.BooleanField(default=False) #tinyint
    
#   class Meta:
#       db_table = User

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null = True, blank = True)

    class Meta:
        db_table = "Organizers"

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null = True, blank = True)

    class Meta:
        db_table = "Administrators"

# status = "Upcoming", "Cancelled", "Ongoing", "Done"
class Event(models.Model):
    name = models.CharField(max_length = 100, null = False)
    description = models.TextField()
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    upvotes = models.IntegerField()
    participantsCount = models.IntegerField()
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=45, default="Upcoming")
    users = models.ManyToManyField(User)
    organizer = models.ForeignKey(Organizer, on_delete = models.CASCADE, null = True, related_name = "events")

    class Meta:
        db_table = "Events"

# types = requestAdmin, requestOrganizer, joinEvent
# responseStatus = Pending, Accepted, Declined
class Request(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "requests")
    event = models.ForeignKey(Event, on_delete = models.CASCADE, null = True, related_name = "requests")
    organizer = models.ForeignKey(Organizer, on_delete = models.SET_NULL, null = True, blank = True)
    type = models.CharField(max_length=100)
    requestDateTime = models.DateTimeField()
    responseDateTime = models.DateTimeField(null = True)
    responseStatus = models.CharField(max_length=100, default = "Pending")

    class Meta:
        db_table = "Requests"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "reviews")
    event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = "reviews")
    title = models.CharField(max_length=45)
    description = models.TextField()
    createdDateTime = models.DateTimeField(default = dt.now)

    class Meta:
        db_table = "Reviews"

# notifType = "Request to be Administrator", "Request to be Organizer", "Request to Join Event"
# title = "Administrator Role Request", "Organizer Role Request", "Join Event"
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "notifications")
    # user = models.ManyToManyField(User)
    organizer = models.ForeignKey(Organizer, on_delete = models.CASCADE, related_name="notifications", null=True, blank=True)
    event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = "notifications", null=True, blank=True)
    request = models.ForeignKey(Request, on_delete = models.CASCADE, related_name = "notifications", null=True, blank=True)
    notifType = models.CharField(max_length=50)
    title = models.CharField(max_length=45)
    description = models.TextField()
    sentDateTime = models.DateTimeField(default = dt.now)
    isViewed = models.BooleanField(default=False)

    class Meta:
        db_table = "Notifications"


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "upvotes")
    event = models.ManyToManyField(Event)

    class Meta:
        db_table = "Upvotes"