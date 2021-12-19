from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """
    Index view van gallery.
    Args:
        request:

    Returns:

    """
    return render(request, 'gallery/index.html')
