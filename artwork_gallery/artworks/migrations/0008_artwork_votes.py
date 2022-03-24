# Generated by Django 4.0.3 on 2022-03-18 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("artworks", "0007_alter_artist_name_alter_artwork_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="artwork",
            name="votes",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
