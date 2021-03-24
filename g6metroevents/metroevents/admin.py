from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Administrator)
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Request)
admin.site.register(Notification)
admin.site.register(Upvote)
admin.site.register(Review)