from django import template
from django.conf import settings

register = template.Library()

# Dit is gewoon een example. Dit was niet nodig.

# @register.simple_tag
# def mediaurl(filename):
#     return filename