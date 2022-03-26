# Generated by Django 4.0.3 on 2022-03-11 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artworks", "0004_artwork"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artwork",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="artwork",
            name="height",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="artwork",
            name="image",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="artwork",
            name="location",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="artwork",
            name="released_at",
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="artwork",
            name="width",
            field=models.CharField(max_length=10, null=True),
        ),
    ]