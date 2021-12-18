from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(models.Model):
    """
    Role is een functie die een dude bekleed binnen het dispuut
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Profile is een extended user account. Elke dude heeft een profile.
    """
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, verbose_name="Functie", null=True, blank=True)
    lichting = models.IntegerField(verbose_name="Lichting", null=True)
    first_name = models.CharField(max_length=50, verbose_name="Voornaam", null=True)
    last_name = models.CharField(max_length=50, verbose_name="Achternaam", null=True)
    dude_name = models.CharField(max_length=50, verbose_name="Dude naam", null=True, unique=True)
    avatar = models.ImageField(verbose_name="Avatar")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.username
