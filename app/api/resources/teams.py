from flask_restful import (
    reqparse,
    Resource
)

from app.api import api
from app.extensions import elasticsearch_url
from app.helpers import api_response

import requests


parser = reqparse.RequestParser()


class Team(Resource):
    """Team Class is the Resource for a querying and searching the team data in
    an elasticsearch instance

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
                    "fields": ["name", "prefix_1", "prefix_2"],
                    "query": query_string['q'],
                    "type": "cross_fields",
                    "use_dis_max": False
                }
            },
            "size": 100
        }
        resp = requests.post(elasticsearch_url + 'nba_teams/team/_search', json=query)
        data = resp.json()
        teams = []
        for hit in data['hits']['hits']:
            team = hit['_source']
            team['id'] = hit['_id']
            teams.append(team)

        return {'success': teams}


class AllTeams(Resource):
    """AllTeams Class is the Resource for fetching all team data in an
    elasticsearch instance -- limited to 100 response hits

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
        resp = requests.post(elasticsearch_url + 'nba_teams/_search', json=query)
        data = resp.json()
        teams = []
        for hit in data['hits']['hits']:
            team = hit['_source']
            team['id'] = hit['_id']
            teams.append(team)

        return {'success': teams}


# Add resource endpoints here =================================================
api.add_resource(Team, '/team/search')
api.add_resource(AllTeams, '/teams')
