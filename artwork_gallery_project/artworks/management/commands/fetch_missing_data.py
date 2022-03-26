import requests
from django.core.management.base import BaseCommand

from artworks.models import Artwork
import environ
import bbcode

from artworks.services.wikiart_client import WikiArtClient


class Command(BaseCommand):
    help = "Fetch missing data for artworks and artists"

    def __init__(self):
        self.env = environ.Env()
        environ.Env.read_env()
        self.wiki_art_client = WikiArtClient(
            access_code=self.env("MEDIAWIKI_ACCESS_CODE"),
            secret_code=self.env("MEDIAWIKI_SECRET_CODE"),
        )

    def handle(self, *args, **kwargs):

        artworks = Artwork.objects.filter(api_fetched=False)
        artwork_updated = 0

        for artwork in artworks:
            data = self.getData(artwork.title)

            if data is not None:
                artwork.description = (
                    bbcode.render_html(data["artwork_details"]["description"]) or ""
                )
                artwork.image = data["artwork_details"]["image"] or None
                artwork.released_at = (
                    data["artwork_details"]["completitionYear"] or None
                )
                artwork.width = data["artwork_details"]["width"] or None
                artwork.height = data["artwork_details"]["height"] or None
                artwork.location = data["artwork_details"]["location"] or None
                artwork.api_fetched = True

                artwork.artist.birthday = (
                    data["artist_details"]["birthDayAsString"] or None
                )
                artwork.artist.deathday = (
                    data["artist_details"]["deathDayAsString"] or None
                )
                artwork.artist.image = data["artist_details"]["image"] or None

                artwork.artist.save()
                artwork.save()

                artwork_updated += 1

        print("{} artworks fetched with missing data".format(artwork_updated))

    def getData(self, artwork_name):
        # Find artwork by name
        search_result = self.wiki_art_client.search_artwork(artwork_name)

        if len(search_result["data"]) > 0:
            artwork_id = search_result["data"][-1]["id"]
            artist_url = search_result["data"][-1]["artistUrl"]

            return {
                "artwork_details": self.wiki_art_client.get_artwork(artwork_id),
                "artist_details": self.wiki_art_client.get_artist(artist_url),
            }

        return None
