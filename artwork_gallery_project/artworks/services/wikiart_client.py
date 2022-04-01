from artworks.services.client import ApiClient


class WikiArtClient(ApiClient):
    def __init__(self, access_code, secret_code):
        super().__init__(api_host="https://www.wikiart.org/fr/")
        self.access_code = access_code
        self.secret_code = secret_code

    def generate_uri(self, uri, query_params=None, add_secrets=True):
        secret_params = {"accessCode": self.access_code, "secretCode": self.secret_code}

        if query_params is not None and add_secrets is True:
            secret_params.update(query_params)
            return super().generate_uri(uri, secret_params)

        return super().generate_uri(uri, query_params)

    def search_artwork(self, artwork_name):
        uri = self.generate_uri(
            "Api/2/PaintingSearch",
            {
                "term": artwork_name,
            },
        )
        return super().get_resource(uri)

    def get_artwork(self, artwork_id):
        uri = self.generate_uri("Api/2/Painting", {"id": artwork_id})
        return super().get_resource(uri)

    def get_artist(self, artist_url):
        uri = self.generate_uri(artist_url, {"json": 2}, add_secrets=False)
        return super().get_resource(uri)
