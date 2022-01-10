from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import User
from django.db.models import Count

@login_required
def profile_view(request, profile_id):
    user = User.objects.filter(id=profile_id).first()

    return render(
        request,
        'profile.html',
        {'user': user}
    )


def group_index(request):
    """
    Geef een overzicht van alle groepen en bijbehorende leden.
    Args:
        request:

    Returns: HTTPResponse
    """
    groups = Group.objects.annotate(c=Count('user')).filter(c__gt=0)
    return render(
        request,
        'groups/index.html',
        {
            'groups': groups
        }
    )