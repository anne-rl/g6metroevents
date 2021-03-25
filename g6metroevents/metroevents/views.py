from django.contrib import auth
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group, User, auth
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Event, Organizer, Review
from django.db.models import Q
from .auxfunctions import *

class Landing(View):
    def get(self, request):
        return render(request, 'landing.html')

    def post(self, request):
        return render(request, 'landing.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'signup_login.html')

    def post(self,request):
        if 'btn-login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #admin
                if request.user.is_staff or request.user.is_superuser: 
                    return HttpResponseRedirect(reverse('admin:index'))
                #organizer
                elif hasattr(request.user,'organizer'):
                    return redirect('user:o-eventlist')
                #user    
                else:
                    return redirect('user:eventlist')
            else:
                context = {'msg': 'Invalid username or password!'}
                return render(request, 'signup_login.html', context = context)

        if 'btn-register' in request.POST:
            print("register")
            username = request.POST.get('username')
            password = request.POST.get('password')
            passwordRepeat = request.POST.get('password-repeat')
            email = request.POST.get('email')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            
            if password == passwordRepeat:
                if not User.objects.filter(username=username).exists():  
                    if not User.objects.filter(email=email).exists():
                        User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)
                        return redirect('user:login')
                    else:   
                        return HttpResponse('email exists')  
                else:
                    return HttpResponse('Username exists')  
            else:
                return HttpResponse('passwords do not match')  
            return redirect('user:login')
        
def LogoutView(request):
        logout(request)
        return redirect ('user:landing')

#--------- USER DASHBOARD
class UserDashboard_EventList(View):
    def get(self, request):
        currentUserID = request.user.id
        currentUser = User.objects.get(id=currentUserID)
        print(currentUser)
        organizer = "false"
        admin = "false"
        if hasattr(currentUser, 'organizer'):
            organizer = "true"
        if hasattr(currentUser, 'administrator'):
            admin = "true"
        events = Event.objects.all()
        notifcount = Notification.objects.filter(user_id= currentUserID).count()
        joinedEventsCount = currentUser.event_set.all().count()
        joinedEvents = currentUser.event_set.all()
        joinedEventsCount = joinedEvents.count()

        context = {
            "username" : currentUser.username,
            "isOrganizer" : organizer,
            "isAdmin": admin,
            "events" : events,
            "notifcount": notifcount,
            "joinedEventsCount": joinedEventsCount,
            "joinedEvents" : joinedEvents,
        }
        return render(request, 'userdashboard_eventList.html', context = context)

    def post(self, request):
        print(request.POST)
        if 'btnOrganizerRoleRequest' in request.POST:
            requestOrganizer(request.user.id)
        if 'btnAdminRoleRequest' in request.POST:
            requestAdmin(request.user.id)
        if 'btnJoinEvent' in request.POST:
            eventID = request.POST.get('eventID')
            userID = request.user.id
            requestJoinEvent(userID, eventID)
        if 'btnUpvote' in request.POST:
            eventID = request.POST.get('eventID')
            user = request.user
            upvoteEvent(eventID)
            return redirect("user:joinedevents")
        elif 'btnDownvote' in request.POST:
            eventID = request.POST.get('eventID')
            user = request.user
            downvoteEvent(eventID)
            return redirect("user:joinedevents")
        elif 'btnReview' in request.POST:
            user = request.user
            eventID = request.POST.get('eventID')
            title = request.POST.get('title')
            description = request.POST.get('description')
            event = Event.objects.get(id = eventID)
            review = Review.objects.create(user = user, event=event, title=title, createdDateTime=dt.now(), description=description)
            return redirect("user:joinedevents")
        return redirect ("user:eventlist")

class UserDashboard_JoinedEvents(View):
    def get(self, request):
        currentUserID = request.user.id
        currentUser = User.objects.get(id=currentUserID)
        joinedEvents = currentUser.event_set.all()
        notifcount = Notification.objects.filter(user_id= currentUserID).count()
        joinedEventsCount = joinedEvents.count()
        context = {
            "joinedEvents" : joinedEvents,
            "username" : currentUser.username,
            "joinedEventsCount" :joinedEventsCount,
            'notifcount': notifcount,
        }
        return render(request, 'userdashboard_joinedEvents.html', context = context)

    def post(self, request):
        if 'btnUpvote' in request.POST:
            eventID = request.POST.get('eventID')
            user = request.user
            upvoteEvent(eventID)
            return redirect("user:joinedevents")
        elif 'btnDownvote' in request.POST:
            eventID = request.POST.get('eventID')
            user = request.user
            downvoteEvent(eventID)
            return redirect("user:joinedevents")
        elif 'btnReview' in request.POST:
            user = request.user
            eventID = request.POST.get('eventID')
            title = request.POST.get('title')
            description = request.POST.get('description')
            event = Event.objects.get(id = eventID)
            review = Review.objects.create(user = user, event=event, title=title, createdDateTime=dt.now(), description=description)
            return redirect("user:joinedevents")
        else:
            #error message here
            return render(request, 'userdashboard_joinedEvents.html')

        return render(request, 'userdashboard_joinedEvents.html')

class UserDashboard_Notifications(View):

    def get(self, request):
        currentUserID = request.user.id
        currentUser = User.objects.get(id=currentUserID)
        notifications = currentUser.notifications.all()
        notifcount = Notification.objects.filter(user_id= currentUserID).count()
        context = {
            "username" : currentUser.username,
            'notifcount': notifcount,
            'notifications': notifications
        }
        return render(request, 'userdashboard_notifications.html', context= context)

    def post(self, request):
        return render(request, 'userdashboard_notifications.html')

#--------- ORGANIZER DASHBOARD
class OrgDashboard_EventList(View):
    def get(self, request):
        user = request.user
        organizer = user.organizer
        events = organizer.events.filter(status = "Upcoming")
        requests = Request.objects.filter(responseStatus = "Pending", organizer = organizer)
        # notifcount = Notification.objects.filter(user_id= user.id).count()
        notifcount = Notification.objects.filter(organizer=organizer.id).count()

        #count all concluded events for the concluded events badge
        concludedEvents = organizer.events.filter(status = "Done")
        concludedEventsCount = concludedEvents.count()
        context = {
            'events':events,
            'user' : user,
            "username" : user.username,
            'requests': requests,
            'notifcount': notifcount,
            'concludedEvents': concludedEvents,
            'concludedEventsCount': concludedEventsCount,
        }
        return render(request, 'orgdashboard_eventList.html', context)

    def post(self, request):
        if 'btnAdd' in request.POST:
            name = request.POST.get("name")
            type = request.POST.get("type")
            startDateTime = request.POST.get("startdate")
            endDateTime = request.POST.get("endDate")
            description = request.POST.get("description")
            organizerName = request.POST.get("organizer")
            if Event.objects.filter(name=name).exists():
                return HttpResponse('Event Name Already Exists')
            else:
                organizer = request.user.organizer
                event = Event.objects.create(name = name, type = type, startDateTime = startDateTime, endDateTime = endDateTime,
                                    description = description, upvotes = 0, participantsCount = 0,organizer = organizer)
            return redirect ("user:o-eventlist")

        elif 'btnUpdate' in request.POST:
            currentUserID = request.user.id
            id = request.POST.get("eventID")
            name = request.POST.get("name")
            type = request.POST.get("type")
            startDateTime = request.POST.get("startdate")
            endDateTime = request.POST.get("endDate")
            description = request.POST.get("description")
            participantsCount = request.POST.get("participantsCount")
            status = request.POST.get("status")
            organizer = Organizer.objects.get(user_id = currentUserID)
            Event.objects.filter(id=id).update(name=name, type=type, startDateTime=startDateTime, status=status,
                    endDateTime=endDateTime, description=description, participantsCount=participantsCount,
                    organizer = Organizer.objects.get(id = organizer.id))

            return redirect ("user:o-eventlist")

        elif 'btnCancel' in request.POST:
            eventID = request.POST.get("eventID")
            event = Event.objects.filter(id = eventID).update(status = "Cancelled")

            return redirect ("user:o-eventlist")

        elif 'btnAdminRoleRequest' in request.POST:
            requestAdmin(request.user.id)
        
        elif 'btnAcceptRequest' in request.POST:
            requestID = request.POST.get('requestID')
            acceptRequest(requestID)
            
        elif 'btnDeclineRequest' in request.POST:
            requestID = request.POST.get('requestID')
            declineRequest(requestID)

        # else:
        #     return redirect(request, 'orgdashboard_eventList.html')

        return redirect('user:o-eventlist')

class OrgDashboard_ConcludedEvents(View):
    def get(self, request):
        organizer = request.user.organizer
        events = Event.objects.filter(organizer = organizer, status = "Done")
        notifcount = Notification.objects.filter(organizer=organizer.id).count()
        # notifcount = Notification.objects.filter(user_id = request.user.id).count()
        reviews = Review.objects.all()

        #count all events for the event list badge
        eventCount = organizer.events.filter(status = "Upcoming").count()
        context = {
            "events" : events,
            "notifcount": notifcount,
            "reviews": reviews,
            "eventCount": eventCount,
        }
        return render(request, 'orgdashboard_concludedevents.html', context = context)

    def post(self, request):
        return render(request, 'orgdashboard_concludedevents.html')

class OrgDashboard_Notifications(View):
    def get(self, request):
        user = request.user
        organizer = user.organizer
        notifcount = Notification.objects.filter(organizer=organizer.id).count()
        # notifcount = Notification.objects.filter(user_id= user.id).count()
        # notifications = user.notifications.all()
        notifications = organizer.notifications.all()
        context = {
            "user" : user,
            "username" : user.username,
            "notifcount": notifcount,
            "notifications" : notifications, 
        }
        return render(request, 'orgdashboard_notifications.html', context=context)

    def post(self, request):
        return render(request, 'orgdashboard_notifications.html')


