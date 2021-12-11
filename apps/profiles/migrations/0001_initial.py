# Generated by Django 4.0 on 2021-12-11 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lichting', models.IntegerField(verbose_name='Lichting')),
                ('first_name', models.CharField(max_length=50, verbose_name='Voornaam')),
                ('last_name', models.CharField(max_length=50, verbose_name='Achternaam')),
                ('dude_name', models.CharField(max_length=50, verbose_name='Dude naam')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Avatar')),
                ('description', models.TextField(verbose_name='Description')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.role', verbose_name='Functie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user')),
            ],
        ),
    ]
