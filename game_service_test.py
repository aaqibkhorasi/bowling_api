"""
Testing file which hold unit test for game_service
"""

import unittest

from game_service import GameService
from common import constants

class GameServiceTest(unittest.TestCase):
    def setUp(self):
        """Initialises all variables"""
        self.game = GameService()
        self.game.frame_tracker = 0
        self.game.frames = None
        self.game.throw = 0

    def test_get_score_game_not_started(self):
        """
        Check if get_score() handle error functionality works as expected when
        game not started 
        """
        # Case 1: Game is not started yet, should return error message.
        self.assertEqual(self.game.get_score(),
                         {'info': constants.GAME_NOT_STARTED})

    def test_get_score_game_started(self):
        """
        Check if get_score() functionality works as expected when game is just started
        """
        # Check if initial data points are fetched when game starts
        self.game.start_game()
        frame_scores = {
          frame_id: {
            'throw': {
              constants.FIRST_THROW: -1,
              constants.SECOND_THROW: -1,
              constants.THIRD_THROW: -1
            },
            'score': -1
          }
          for frame_id in range(constants.MAX_FRAMES)
        }
        expected_result = {'frame_scores': frame_scores, 'running_score': 0}
        self.assertEqual(self.game.get_score(), expected_result)
    
    def test_knocked_pin_openface(self):
        """test when there's normal knocked down where total value is less than 10
        basically no spare or strike
        ."""
        self.game.start_game()
        for _ in range(2*constants.MAX_FRAMES): # Just running a fake game where pinning 3 in each throw
            self.game.knocked_pins('3') 

        frame_scores = {}
        for frame in range(constants.MAX_FRAMES):
            frame_scores[frame] = {'throw': {0: 3, 1: 3, 2:-1}, 'score': 6}

        expected_result = {'frame_scores': frame_scores, 'running_score': 60}
        self.assertEqual(
            self.game.get_score(),
            expected_result
        )

    def test_pins_knocked_all_strikes(self):
        """Test to check all strikes in each turn"""
        self.game.start_game() # Starting game 
        for _ in range(constants.MAX_FRAMES + 2): # Last frame has 2 extra throw
            self.game.knocked_pins('10')

        frame_scores = {}
        for frame in range(constants.MAX_FRAMES - 1):
            frame_scores[frame] = {'throw': {0: 10, 1: -1, 2:-1}, 'score': 30}

        # Update score for last frame.
        frame_scores[constants.MAX_FRAMES - 1] = {
          'throw': {0: 10, 1: 10, 2: 10},
          'score': 30
        }
        expected_result = {'frame_scores': frame_scores, 'running_score': 300}
        self.assertEqual(
            self.game.get_score(),
            expected_result
        )
    
    def test_pins_knocked_all_spares(self):
        """Test to check all spares in each turn"""
        self.game.start_game()  # Starting game 
        # Last frame has 3 rolls so +1.
        for _ in range(2*constants.MAX_FRAMES + 1): # faking game with spare in each frame
            self.game.knocked_pins('5')

        # check score after all spares 
        scores = {}
        for frame in range(constants.MAX_FRAMES - 1):
            scores[frame] = {
                'throw': {
                    constants.FIRST_THROW: 5,
                    constants.SECOND_THROW: 5,
                    constants.THIRD_THROW: -1
                },
                'score': 15
            }

        scores[constants.MAX_FRAMES - 1] = { # Updating score for last frame
          'throw': {0: 5, 1: 5, 2: 5},
          'score': 15
        }
        expected_result = {'frame_scores': scores, 'running_score': 150}

        self.assertEqual(self.game.get_score(),
                         expected_result)