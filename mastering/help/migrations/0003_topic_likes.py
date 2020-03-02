# Generated by Django 3.0.3 on 2020-02-29 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help', '0002_auto_20200224_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]