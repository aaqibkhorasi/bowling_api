"""
This file contain core functionality of Bowling game such as:
 - Initialize object with None/0 values.
 - Updating per frame score
 - Getting Updated Score

"""

from common import constants
from models import Frame

class GameService(object):
    """Game service to manage bowling scoring system"""
    def __init__(self):
        """Initialises GameService."""
        self.frame_tracker = 0  #  0 to 9 since we have 10 frames in total 
        self.throw = 0  # 0 or 1, 2 in case last frame is knocked with strike.
        self.frames = None # Hold list of Frame objects which holds per frame score and throw

    def start_game(self):
        """Initialises all object variables to starts a new game.

        Returns: json with success message string.
        """
        self.frame_tracker = 0
        self.throw = 0
        self.frames = [Frame(frame_id) for frame_id in range(constants.MAX_FRAMES)] # holds frames for a game
        return {'info': constants.NEW_GAME_MESSAGE}
    
    def get_score(self):
        """Returns total score and per frame score if game has started.

        Returns: json with error message if game is not started or
        total frame scores and running scores

        """
        if self.frames is None:
            return {'info': constants.GAME_NOT_STARTED}
        total_score = 0
        for frame in self.frames:
            if frame.get_frame_score() != -1:
                total_score += frame.get_frame_score()

        frame_scores = {
          id: {
            'throw': {
              constants.FIRST_THROW: frame.get_first_throw_score(),        # First Throw
              constants.SECOND_THROW: frame.get_second_throw_score(),       # Second Throw
              constants.THIRD_THROW: frame.get_third_throw_score()
            },
            'score': frame.get_frame_score()
          }
          for id, frame in enumerate(self.frames) 
        }
        return {'frame_scores': frame_scores, 'running_score': total_score}

    def validate_knocked_pins(self, knocked_pins):
        """Validates knocked_pin supplied to the function.

        This also validates number of throws.

        Args:
          knocked_pins: Number of pins that were knocked down

        Returns: True, if pinks knocked is valid else False with error message.
        """
        if not knocked_pins.isdigit():
            return False, constants.INVALID_KNOCKED_PINS

        knocked_pins = int(knocked_pins)  
        if knocked_pins < 0 or knocked_pins > constants.MAX_PINS:  # knocked_pins should be in range[0,11)
            return False, constants.INVALID_KNOCKED_PINS

        current_frame = self.frames[self.frame_tracker]
        if self.frame_tracker == constants.MAX_FRAMES - 1: # Last frame
            if not current_frame.is_strike() and (
               self.throw == 1 and current_frame.get_first_throw_score() + knocked_pins > constants.MAX_PINS): # Checking if its second throw and total is not greater than MaxPins
                return False, constants.INVALID_SECOND_THROW.format(
                  first_throw=current_frame.get_first_throw_score())
            else:
                return True, ''

        if self.throw and (current_frame.get_first_throw_score() + knocked_pins) > constants.MAX_PINS: # If total face value of knocked_pins is greater than max pin, then throw error
            return False, constants.INVALID_SECOND_THROW.format(
              first_throw=current_frame.get_first_throw_score())

        return True, ''

    def _update_score(self, current_frame, throw):
        """Updates score for current frame.

        Also updates score for previous frames based on current frame if previous frame had strike/spare.

        Args:
          current_frame: Current frame, frame for which throw is made.
          roll: Throw count, 0 or 1. Can be 2 also but only when current_frame is last (i.e 9).
        """

        frame_data = self.frames[current_frame] 
        # Update score for current frame if both rolls are done and its not a
        # spare.
        is_strike1 = frame_data.is_strike() # Object approach


        is_spare1 = frame_data.is_spare() # Object approach

        if throw and not (is_spare1 or is_strike1):
            # Just update the frame with face value of current two throws
            # frame_data['score'] = frame_data['throw'][constants.FIRST_THROW] + frame_data['throw'][constants.SECOND_THROW] 
            frame_data.add_firstwo_throws() # Object approach 
        # If this is the first frame, no need to check for previous frames.
        if current_frame < 1:
            return None

        # If previous frame scores are not updated as they were strike or spare,
        #  then update previous frame using current frame knocked pin.
        previous_frame = self.frames[current_frame-1]
        
        if previous_frame.get_frame_score() == -1:
            current_frame_firsthrow = frame_data.get_first_throw_score()  # Current Frame First throw
            current_frame_secondthrow = frame_data.get_second_throw_score() # Current Frame Second throw
            if previous_frame.is_spare():
                # if previous frame value has spare, then we will add first throw value of current frame into previous frame score
                previous_frame.set_frame_score(constants.MAX_PINS + current_frame_firsthrow)
            else:
                # If last two previous frames were double strike
                if current_frame > 1:  # Double strike from previous 2 frames 
                    previous_to_previous_frame = self.frames[current_frame - 2]
                    if previous_to_previous_frame.get_frame_score() == -1:
                        previous_to_previous_frame.set_frame_score(20 + current_frame_firsthrow)  # Double strike case.

                # Update previous frame's score.
                if throw: # Case to handle previous 1 strike in previous frame
                    previous_frame.set_frame_score((constants.MAX_PINS + current_frame_firsthrow +
                                              current_frame_secondthrow))

        # If its last frame and all roles are made, we just have to add
        # pins knocked in all (3 throws value for strike and spare and 2 throws for normal)
        if current_frame == constants.MAX_FRAMES - 1 and (throw == constants.THIRD_THROW):
            frame_data.add_all_throws()

    def _update_pins_and_score(self, knocked_pins):
        """Updates knocked pins and score for a current frame.

        Also tracks next throw will be in same frame or next frame (in case
        there is strike in this frame).

        Args:
          knocked_pins: Number of knocked pins.
        """
        current_frame = self.frame_tracker
        roll = self.throw
        if self.throw == constants.FIRST_THROW:
            self.frames[self.frame_tracker].set_first_throw_score(knocked_pins)
        if self.throw == constants.SECOND_THROW:
            self.frames[self.frame_tracker].set_second_throw_score(knocked_pins)
        if self.throw == constants.THIRD_THROW:
            self.frames[self.frame_tracker].set_third_throw_score(knocked_pins)

        if self.frame_tracker == constants.MAX_FRAMES - 1: # Handling last frame
            # If strike or spare in last frame, 3 throws would be allowed.
            if not self.throw or (self.throw < 2 and (
               self.frames[self.frame_tracker].is_strike() or
               self.frames[self.frame_tracker].is_spare())):
                self.throw += 1
            else:
                self.throw = 0
                self.frame_tracker += 1
        elif not (self.throw or self.frames[self.frame_tracker].is_strike()):
            self.throw += 1
        else:
            self.throw = 0
            self.frame_tracker += 1

        self._update_score(current_frame, roll)

    def knocked_pins(self, knocked_pins):
        """Updates score when a new pin is knocked.

        Args:
          knocked_pins: Number of pins knocked down in a current frame/throw.

        Returns: Json with success/error message
        """
        if self.frames is None:
            return {'error': constants.PINS_KNOCKED_BEFORE_GAME_STARTED}, constants.HTTP_STATUS["BAD_REQUEST"]

        if self.frame_tracker == constants.MAX_FRAMES:
            return {'info': constants.GAME_ENDED_MESSAGE}

        # Checks if given parameter for knocked_pins is valid or not
        valid, error_message = self.validate_knocked_pins(knocked_pins)
        if not valid:
            return {'error': error_message}, constants.HTTP_STATUS["BAD_REQUEST"]
        current_frame = self.frame_tracker
        self._update_pins_and_score(int(knocked_pins))
        return {
            'info': constants.SCORES_UPDATED_MESSAGE,
            'current_frame': current_frame,
            'current_frame_score': self.frames[current_frame].get_frame_score()
        }