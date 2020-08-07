# Generated by Django 3.0.6 on 2020-07-20 17:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Cadmin',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='Cusers',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]