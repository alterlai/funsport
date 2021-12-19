from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    """
    Profile is een extended user account. Elke dude heeft een profile.
    """
    first_name = models.CharField(max_length=50, verbose_name="Voornaam", null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name="Achternaam", null=True, blank=True)
    dude_name = models.CharField(max_length=50, verbose_name="Dude naam", null=True, unique=True, blank=True)
    avatar = models.ImageField(verbose_name="Avatar", null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    current_role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=False, related_name="active_dude")

    def __str__(self):
        return self.username
