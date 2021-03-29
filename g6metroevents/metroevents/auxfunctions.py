from .models import *
from datetime import datetime as dt

# request to be organizer method
# types = requestAdmin, requestOrganizer, joinEvent
def requestOrganizer(userID):
    user = User.objects.get(id = userID)
    print(user.first_name)
    request = Request.objects.create(user = user, type = "requestOrganizer", requestDateTime = dt.now())

    notification = Notification(user = user, notifType = "Request to be Organizer", 
                                title = "Send Organizer Role Request", description = "User " + user.first_name + " " + user.last_name + " wants to become an Organizer", 
                                sentDateTime = dt.now(), request = request)

    # request.save()
    notification.save()
    print("request Organizer sent")

# request to be admin methods
def requestAdmin(userID):
    user = User.objects.get(id = userID)
    request = Request.objects.create(user = user, type = "requestAdmin", requestDateTime = dt.now())

    notification = Notification(user = user, notifType = "Request to be Admin", 
                                title = "Send Administrator Role Request", description = "User " + user.first_name + " " + user.last_name + " wants to become an Administrator", 
                                sentDateTime = dt.now(), request = request)

    # request.save()
    notification.save()
    print("request Admin sent")

def requestJoinEvent(userID, eventID):
    user = User.objects.get(id = userID)
    event = Event.objects.get(id = eventID)
    organizer = event.organizer
    request = Request.objects.create(user = user, event = event, organizer = organizer, type = "joinEvent", requestDateTime = dt.now())
    notification = Notification(user = user, event = event, request = request, notifType = "Request to Join Event", organizer = organizer,
                                title = "Join Event", description = "User " + user.first_name + " " + user.last_name + " wants to join " + event.name + ".", 
                                sentDateTime = dt.now())
    # request.save()
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

def deleteRequest(requestID):
    request = Request.objects.filter(id = requestID).delete()

def acceptOrganizer(requestID):
    request = Request.objects.get(id = requestID)
    request.responseDateTime = dt.now()
    request.responseStatus = "Accepted"
    user = request.user
    request.save()
    organizer = Organizer()
    organizer.user = User.objects.get(id=user.id)
    organizer.save()
    notification = Notification(user = user, request = request, notifType = "Request to be Organizer", 
                            title = "Request to be Organizer Accepted", description = "Your request to be Organizer is accepted!", 
                            sentDateTime = dt.now())
    # delete all pending user organizer requests as he is already an organizer except newly accepted request
    user.requests.filter(type = "requestOrganizer", responseStatus="Pending").exclude(id = request.id).delete()
    user.notifications.filter(notifType = "Request to be Organizer", request_id__responseStatus = "Pending").exclude(request_id = request.id).delete()
    notification.save()

    

def declineOrganizer(requestID):
    request = Request.objects.get(id = requestID)
    request.responseDateTime = dt.now()
    request.responseStatus = "Declined"
    user = request.user
    request.save()
    request.notifications.all().delete()
    notification = Notification(user = user, request = request, notifType = "Request to be Organizer", 
                            title = "Request to be Organizer Declined", description = "Your request to be Organizer is declined!", 
                            sentDateTime = dt.now())
    notification.save()

    
# acceptAdminRequest
def acceptAdmin(requestID):
    request = Request.objects.get(id = requestID)
    request.responseDateTime = dt.now()
    request.responseStatus = "Accepted"
    request.save()
    user = request.user
    user.is_staff = True
    user.is_superuser = True
    user.save()
    notification = Notification(user = user, request = request, notifType = "Request to be Administrator", 
                            title = "Request to be Administrator Accepted", description = "Your request to be Administrator is accepted!", 
                            sentDateTime = dt.now())
    notification.save()

    # delete all pending user admin role requests as he is already an admin
    user.requests.filter(type = "requestAdmin", responseStatus="Pending").exclude(id = request.id).delete()
    user.notifications.filter(notifType = "Request to be Administrator", request_id__responseStatus = "Pending").exclude(request_id = request.id).delete()
    
    admin = Administrator()
    admin.user = User.objects.get(id=user.id)
    admin.save()

def declineAdmin(requestID):
    request = Request.objects.get(id = requestID)
    request.responseDateTime = dt.now()
    request.responseStatus = "Declined"
    request.save()
    request.notifications.all().delete()
    user = request.user
    notification = Notification(user = user, request = request, notifType = "Request to be Administrator", 
                            title = "Request to be Administrator Declined", description = "Your request to be Administrator is declined!", 
                            sentDateTime = dt.now())
    notification.save()                        
    
    
    
