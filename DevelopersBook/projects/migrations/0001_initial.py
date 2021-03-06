# Generated by Django 3.0.6 on 2020-07-18 18:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(choices=[('Web_Development', 'Web Development'), ('App_Development', 'App Development'), ('Game_Development', 'Game Development'), ('Software_development', 'Software Development'), ('Graphic_Design', 'Graphic Design'), ('Script', 'Script'), ('Other', 'Other')], default='Web_Development', max_length=20)),
                ('projectName', models.CharField(max_length=40)),
                ('Details', models.TextField(max_length=600)),
                ('Requirements', models.TextField(max_length=500)),
                ('github', models.URLField(default='https://github.com/404')),
                ('discord', models.URLField(default='https://discord.com/404')),
                ('facebook', models.URLField(default='https://www.facebook.com/error20%20404')),
                ('Cusers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
