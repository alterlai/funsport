from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def profile_view(request):
    return render(
        request,
        'profile.html',
        {'user': request.user}
    )

def group_index(request):
    """
    Geef een overzicht van alle groepen en bijbehorende leden.
    Args:
        request:

    Returns: HTTPResponse
    """
    groups = Group.objects.all()
    return render(
        request,
        'groups/index.html',
        {'groups': groups}
    )