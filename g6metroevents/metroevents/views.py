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

class OrganizerView(View):
        def get(self, request):
            return render(request, 'index.html')

class EventsView(View):
        def get(self, request):
            return render(request, 'index.html')

class ParticipantsView(View):
        def get(self, request):
            return render(request, 'index.html')

