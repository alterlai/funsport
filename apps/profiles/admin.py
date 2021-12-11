from django.contrib import admin
from apps.profiles.models import Profile, Role


# Register your models here.
admin.site.register(Profile)
admin.site.register(Role)