from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    """
    Role is een functie die een dude bekleed binnen het dispuut
    """
    name = models.CharField(max_length=30)


class Profile(models.Model):
    """
    Profile is een extended user account. Elke dude heeft een profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, verbose_name="Functie", null=True, blank=True)
    lichting = models.IntegerField(verbose_name="Lichting")
    first_name = models.CharField(max_length=50, verbose_name="Voornaam")
    last_name = models.CharField(max_length=50, verbose_name="Achternaam")
    dude_name = models.CharField(max_length=50, verbose_name="Dude naam")
    avatar = models.ImageField(verbose_name="Avatar")
    description = models.TextField(verbose_name="Description")