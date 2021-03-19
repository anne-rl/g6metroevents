from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = 'metroevents'

urlpatterns = [
    path('index', views.LandingIndexView.as_view(), name="index_view"),
    path('userRegistration', views.UserRegistrationView.as_view(), name="userRegistration_view"),
    path('administrator', views.AdministratorView.as_view(), name="administartor_view"),
    path('organizerDashboardEventList', views.OrganizerDashboardEventListView.as_view(), name="organizerDashboardEventList_view"),
    path('events', views.EventsView.as_view(), name="events_view"),
    path('participants', views.ParticipantsView.as_view(), name="participants_view"),
    path('userDashboard_eventList', views.UserDashboard_eventListsView.as_view(), name="userDashboard_eventLists_view"),
    path('userDashboard_notifications', views.UserDashboardNotificationsView.as_view(), name="userDashboardNotifications_view"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
