import requests
from django.core.management.base import BaseCommand

from artworks.models import Artwork
import environ
import bbcode
from django.db.models import Q


class Command(BaseCommand):
    help = ''
    env = None

    def __init__(self):
        self.env = environ.Env()
        environ.Env.read_env()

    def handle(self, *args, **kwargs):
        artworks = Artwork.objects.filter(api_fetched=False)

        for artwork in artworks:
            data = self.getData(artwork.title)

            artwork.description = bbcode.render_html(data['artwork_details']['description']) or None
            artwork.image = data['artwork_details']['image'] or None
            artwork.released_at = data['artwork_details']['completitionYear'] or None
            artwork.width = data['artwork_details']['width'] or None
            artwork.height = data['artwork_details']['height'] or None
            artwork.location = data['artwork_details']['location'] or None
            artwork.api_fetched = True

            artwork.artist.birthday = data['artist_details']['birthDayAsString'] or None
            artwork.artist.deathday = data['artist_details']['deathDayAsString'] or None
            artwork.artist.image = data['artist_details']['image'] or None

            artwork.artist.save()
            artwork.save()

        print("{} artworks fetched with missing data".format(artworks.count()))


    def getData(self, artwork_name):

        # Find artwork id
        search_result = requests.get(
            'https://www.wikiart.org/fr/Api/2/PaintingSearch?term={}&accessCode={}&secretCode={}'.format(
                artwork_name, self.env('MEDIAWIKI_ACCESS_CODE'), self.env('MEDIAWIKI_SECRET_CODE')))
        artwork_id = search_result.json()['data'][-1]['id']
        artist_url = search_result.json()['data'][-1]['artistUrl']

        # Fetch artwork details
        artwork_details = requests.get(
            'https://www.wikiart.org/fr/Api/2/Painting?id={}&accessCode={}&secretCode={}'.format(
                artwork_id, self.env('MEDIAWIKI_ACCESS_CODE'), self.env('MEDIAWIKI_SECRET_CODE')))

        # Fetch artist details
        artist_details = requests.get('https://www.wikiart.org/fr/{}?json=2'.format(artist_url))

        return {"artwork_details": artwork_details.json(), "artist_details": artist_details.json()}