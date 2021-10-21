"""
Place holder to save constants and success/error strings.
"""

FIRST_THROW = 0 

SECOND_THROW = 1

THIRD_THROW = 2

MAX_FRAMES = 10

MAX_PINS = 10


# Error messages
GAME_NOT_STARTED = 'Please start game before fetching score.'

PINS_KNOCKED_BEFORE_GAME_STARTED = 'Please start game before throwing ball.'

INVALID_KNOCKED_PINS = 'Pins knocked should be positive number and less than 11.'

INVALID_SECOND_THROW = ('Total knocked pins of first and second throw '
                       'cannot be more than 10, {first_throw} pins were '
                       'knocked down in first throw.')

INVALID_FRAME_TRACKER = 'Invalid frame tracker provided. Frame doesn\'t exist.'

# HTTP STATUS CODE 
HTTP_STATUS = {
    "OK": 200,         # default http code
    "BAD_REQUEST": 400,
}

# Info
GAME_ENDED_MESSAGE = ('Good Job!! Game is over now, Please check your score.')

SCORES_UPDATED_MESSAGE = 'Scores updated.'

NEW_GAME_MESSAGE = 'New Game has started now. Good Luck! :) '