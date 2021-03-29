from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = 'metroevents'

urlpatterns = [
    path('landing', views.Landing.as_view(), name="landing"),
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', views.LogoutView, name="logout"),
	path('eventlist', views.UserDashboard_EventList.as_view(), name="eventlist"),
    path('joinedevents', views.UserDashboard_JoinedEvents.as_view(), name="joinedevents"),
    path('notifications', views.UserDashboard_Notifications.as_view(), name="notifications"),
    path('o-eventlist', views.OrgDashboard_EventList.as_view(), name="o-eventlist"),
    path('o-concluded', views.OrgDashboard_ConcludedEvents.as_view(), name="o-concluded"),
    path('o-notifications', views.OrgDashboard_Notifications.as_view(), name="o-notifications"),
    path('a-eventlist', views.AdminDashboard_EventList.as_view(), name='a-eventlist'),
    path('ao-notifications', views.AdminDashboard_OrganizerNotifications.as_view(), name="ao-notifications"),
    path('a-notifications', views.AdminDashboard_AdminNotifications.as_view(), name="a-notifications"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


