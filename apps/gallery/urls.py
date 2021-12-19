"""funsport URL Configuration

"""
from django.urls import path
from .views import index

app_name = 'gallery'

urlpatterns = [
    path('', index, name="index"),

]
