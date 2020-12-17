import requests
from typing import Dict
from database_creation.create_app import db, create_app
from .errors import ApiError, DatabaseSaveError
from database_creation.models import Artists

"""
# Example URLs
JSON: /2.0/?method=chart.gettopartists&api_key=YOUR_API_KEY&format=json
XML: /2.0/?method=chart.gettopartists&api_key=YOUR_API_KEY

# Params
limit (Optional) : The number of results to fetch per page. page (Optional) : T,he page number to fetch. Defaults to first page.
Defaults to 50.
api_key (Required) : A Last.fm API key.

# Auth
This service does not require authentication.
"""


class ApiCollector:
    def __init__(self, url: str, parameters: Dict) -> None:
        """
        params
        :param url: url for  downloading data
        :param parameters: the params for requests in dictionary, include keys as: page, limit - max limit according to
        api documentation 1000, and api_key
        """
        self.url = url
        self.parameters = parameters

    def get_data_from_api(self) -> Dict:
        try:
            response = requests.get(self.url, params = self.parameters)

            return response.json()
        except ApiError:

            return f'Api not available'

    def save_to_database(self) -> str:
        try:
            data = self.get_data_from_api()
            for element in data['artists']['artist']:
                artist = Artists(
                    name=element['name'],
                    playcount=int(element['playcount']),
                    listeners=int(element['listeners']),
                    mbid=element['mbid']
                )
                app = create_app()
                with app.app_context():
                    db.session.add(artist)
                    db.session.commit()

            return f'Record inserted successfully into Artists table'

        except DatabaseSaveError:

            return f'Data saving is not available'


if __name__ == '__main__':
    params = {'limit': 1000, 'api_key': 'a7104e7863632a51eadf755c012005f2', 'format': 'json'}
    url = 'http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists'
    ApiCollector(url, params).save_to_database()

















