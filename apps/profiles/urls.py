from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('', profile_view, name="profile"),
    path('groups', group_index, name="group_index")
]