from django.contrib import admin
from apps.profiles.models import Role
from .models import User



# Register your models here.
admin.site.register(Role)
admin.site.register(User)