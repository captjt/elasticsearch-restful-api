from flask_restful import (
    reqparse,
    Resource
)

from app.api import api
from app.extensions import elasticsearch_url
from app.helpers import api_response

import requests


parser = reqparse.RequestParser()


class Player(Resource):
    """Player Class to query player data based on search parameters in the URL
    sent through a get request

    :extends Resource
    :returns: a JSON response
    """

    @api_response
    def get(self):
        parser.add_argument('q')
        query_string = parser.parse_args()
        query = {
            "query": {
                "multi_match": {
                    "fields": ["player", "team"],
                    "query": query_string['q'],
                    "type": "cross_fields",
                    "use_dis_max": False
                }
            },
            "size": 15
        }
        resp = requests.post(elasticsearch_url + 'nba_players/player/_search', json=query)
        data = resp.json()
        teams = []
        for hit in data['hits']['hits']:
            team = hit['_source']
            team['id'] = hit['_id']
            teams.append(team)

        return {'success': teams}


class AllPlayers(Resource):
    """AllPlayers Class is the Resource for fetching all players in the elastic
    search index

    :extends Resource
    :returns: a JSON response
    """

    @api_response
    def get(self):
        query = {
            "query": {
                "match_all": {}
            }
        }
        resp = requests.post(elasticsearch_url + 'nba_players/_search', json=query)
        data = resp.json()
        teams = []
        for hit in data['hits']['hits']:
            team = hit['_source']
            team['id'] = hit['_id']
            teams.append(team)

        return {'success': teams}


# Add resource endpoints here =================================================
api.add_resource(Player, '/player/search')
api.add_resource(AllPlayers, '/players')
