
from django.views.generic import View, TemplateView
from .forms import UserForm
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