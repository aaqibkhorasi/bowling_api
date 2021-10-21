"""Implements and maps each handler to respective class."""

from flask import Flask
from flask import request

from flask_restful import Api
from flask_restful import Resource

from game_service import GameService


app = Flask(__name__)
api = Api(app)

game_service = GameService()


class GetScore(Resource):
    """[Class to retrieve score of current game]

    """
    def get(self):
        """[GET method to retrieve current game score"]

        Returns:
            [Json]: [Current Game score including frame + total running score]
        """
        return game_service.get_score()


class StartGame(Resource):
    def post(self):
        """[Post method to start a new game ]

        Returns:
            [type]: [description]
        """
        return game_service.start_game()


class KnockedPins(Resource):
    """Implements POST method to input knocked pins in a throw."""
    def post(self):
        request_json = request.get_json()
        knocked_pins = request_json.get('knocked_pins', None)
        if knocked_pins is None:
            return {
              'info': 'Invalid request, parameter `pins-knocked` missing.'
            }, 400
        return game_service.knocked_pins(knocked_pins)


api.add_resource(StartGame, '/start_game')
api.add_resource(GetScore, '/', '/score')
api.add_resource(KnockedPins, '/knocked_pins')



if __name__ == '__main__':
    app.run(debug=True)