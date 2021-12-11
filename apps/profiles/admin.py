from django.contrib import admin
from apps.profiles.models import Profile, Role
from django.contrib.auth.models import Group



# Register your models here.
admin.site.register(Profile)
admin.site.register(Role)