import requests
import urllib.parse


class ApiClient:
    def __init__(self, api_host):
        self.api_host = api_host

    def generate_uri(self, uri, query_params=None):
        try:
            url = urllib.parse.urljoin(self.api_host, uri)

            if query_params:
                query_params = urllib.parse.urlencode(query_params)
                return url + "?" + query_params

            return url
        except Exception as e:
            raise ApiClientException(e)

    def get_resource(self, resource_uri):
        try:
            response = requests.get(resource_uri)
            return response.json()
        except Exception as e:
            raise ApiClientException(e)


class ApiClientException(Exception):
    pass
