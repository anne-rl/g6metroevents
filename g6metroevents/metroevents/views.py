from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class LandingIndexView(View):
        def get(self, request):
            return render(request, 'index.html')

class UserRegistrationView(View):
        def get(self, request):
            return render(request, 'index.html')

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