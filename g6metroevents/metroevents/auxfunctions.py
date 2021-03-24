from .models import *
from datetime import datetime as dt

# request to be organizer method
# types = requestAdmin, requestOrganizer, joinEvent
def requestOrganizer(userID):
    user = User.objects.get(id = userID)
    print(user.first_name)
    request = Request(user = user, type = "requestOrganizer", requestDateTime = dt.now())

    notification = Notification(user = user, notifType = "Request to be Organizer", 
                                title = "Organizer Role Request", description = "User " + user.first_name + " " + user.last_name + " wants to become an Organizer", 
                                sentDateTime = dt.now(), request = request)

    request.save()
    notification.save()
    print("request Organizer sent")

# request to be admin methods
def requestAdmin(userID):
    user = User.objects.get(id = userID)
    print(user.first_name)
    request = Request(user = user, type = "requestAdmin", requestDateTime = dt.now())

    notification = Notification(user = user, notifType = "Request to be Admin", 
                                title = "Administrator Role Request", description = "User " + user.first_name + " " + user.last_name + " wants to become an Administrator", 
                                sentDateTime = dt.now(), request = request)

    request.save()
    notification.save()
    print("request Admin sent")

def requestJoinEvent(userID, eventID):
    user = User.objects.get(id = userID)
    event = Event.objects.get(id = eventID)
    organizer = event.organizer
    print("request Join Event sent")
    request = Request(user = user, event = event, organizer = organizer, type = "joinEvent", requestDateTime = dt.now())
    notification = Notification(user = user, event = event, request = request, notifType = "Request to Join Event", organizer = organizer,
                                title = "Join Event", description = "User " + user.first_name + " " + user.last_name + " wants to join " + event.name + ".", 
                                sentDateTime = dt.now())
    request.save()
    notification.save()
    print("request Join Event sent")

# acceptJoinEvent
def acceptRequest(requestID):
    request = Request.objects.get(id = requestID)
    request.responseDateTime = dt.now()
    request.responseStatus = "Accepted"
    request.save()
    user = request.user
    event = request.event
    notification = Notification(user = user, event = event, request = request, notifType = "joinEvent", 
                            title = "Request Accepted", description = "Your request to join " + event.name + " is accepted!", 
                            sentDateTime = dt.now())
    notification.save()
    event.participantsCount = event.participantsCount + 1
    event.users.add(user)
    event.save()

def declineRequest(requestID):
    request = Request.objects.get(id = requestID)
    request.responseDateTime = dt.now()
    request.responseStatus = "Declined"
    request.save()
    user = request.user
    event = request.event
    notification = Notification(user = user, event = event, request = request, notifType = "joinEvent", 
                            title = "Request Declined", description = "Your request to join " + event.name + " is declined.", 
                            sentDateTime = dt.now())
    notification.save()

def upvoteEvent(eventID):
    event = Event.objects.get(id = eventID)
    event.upvotes = event.upvotes + 1
    event.save()

def downvoteEvent(eventID):
    event = Event.objects.get(id = eventID)
    event.upvotes = event.upvotes - 1
    event.save()