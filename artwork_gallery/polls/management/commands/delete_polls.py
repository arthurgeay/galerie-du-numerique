import requests
from django.core.management.base import BaseCommand

from artworks.models import Artwork
from datetime import datetime


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **kwargs):
        if datetime.now().weekday() == 6:
            Artwork.votes.through.objects.all().delete()
            print("All votes are deleted")
