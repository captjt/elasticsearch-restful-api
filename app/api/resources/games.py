from flask_restful import (
    reqparse,
    Resource
)

from app.api import api
from app.extensions import elasticsearch_url
from app.helpers import api_response

import requests


parser = reqparse.RequestParser()


class Game(Resource):
    """Game Class is the Resource for a searching game data in an elasticsearch
    instance

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
                    "fields": ["date", "home_team", "home_team_score", "visit_team", "visit_team_score"],
                    "query": query_string['q'],
                    "type": "cross_fields",
                    "use_dis_max": False
                }
            },
            "size": 100
        }
        resp = requests.post(elasticsearch_url + 'nba_games/game/_search', json=query)
        data = resp.json()
        teams = []
        for hit in data['hits']['hits']:
            team = hit['_source']
            team['id'] = hit['_id']
            teams.append(team)

        return {'success': teams}


class AllGames(Resource):
    """AllGames Class is the Resource for fetching all of the game data limited
    to 100 response hits from an elasticsearch instance

    :extends Resource
    :returns: a JSON response
    """
    @api_response
    def get(self):
        query = {
            "query": {
                "match_all": {}
            },
            "size": 100
        }
        resp = requests.post(elasticsearch_url + 'nba_games/_search', json=query)
        data = resp.json()
        teams = []
        for hit in data['hits']['hits']:
            team = hit['_source']
            team['id'] = hit['_id']
            teams.append(team)

        return {'success': teams}


# Add resource endpoints here =================================================
api.add_resource(Game, '/game/search')
api.add_resource(AllGames, '/games')
