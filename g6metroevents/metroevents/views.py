
from django.views.generic import View, TemplateView
from .forms import UserForm
from .forms import EventForm
from django.http import Http404
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *


# Create your views here.
class LandingIndexView(View):
        def get(self, request):
            return render(request, 'index.html')

class UserRegistrationView(View):
        def get(self, request):
            return render(request, 'registration.html')

        def post(self, request):       
	        form = UserForm(request.POST)

	        if form.is_valid():
	            #try
	            uname = request.POST.get("username")
	            userpass = request.POST.get("password")
	            fname = request.POST.get("firstname")
	            mname = request.POST.get("middlename")
	            lname = request.POST.get("lastname")
	            email = request.POST.get("email")
	            form = User(username = uname, password = userpass, firstname = fname, middlename = mname, lastname = lname, email = email)

	            form.save()

	            return redirect('metroevents:index')
	          
	            # except:
	            #   raise Http404
	            
	        else:
	            print(form.errors)
	            return HttpResponse('not valid')


class AdministratorView(View):
        def get(self, request):
            return render(request, 'index.html')

class OrganizerDashboardEventListView(View):
        def get(self, request):
            return render(request, 'organizerDashboard_eventList.html')

        def post(self, request):       
	        form = EventForm(request.POST)

	        if form.is_valid():
	            #try
	            ename = request.POST.get("eventName")
	            loc = request.POST.get("location")
	            etype = request.POST.get("type")
	            sTime = request.POST.get("startTime")
	            eTime = request.POST.get("endTime")
	            sDate = request.POST.get("startDate")
	            eDate = request.POST.get("endDate")
	            desc = request.POST.get("description")

	            form = User(eventName = ename, location = loc, type = etype, startTime = sTime, endTime = eTime, startDate = sDate, endDate = eDate, description = desc )

	            form.save()

	            return redirect('metroevents:organizerDashboardEventList')
	          
	            # except:
	            #   raise Http404
	            
	        else:
	            print(form.errors)
	            return HttpResponse('not valid')
class OrganizerMyEvents(View):
        def get(self, request):
            return render(request, 'organizerMyEvents.html')

class EventsView(View):
        def get(self, request):
            return render(request, 'index.html')

class ParticipantsView(View):
        def get(self, request):
            return render(request, 'index.html')

class UserDashboard_eventListsView(View):
        def get(self, request):
            return render(request, 'userdashboard_eventList.html')

class UserDashboardNotificationsView(View):
        def get(self, request):
            return render(request, 'userdashboard_notifications.html')