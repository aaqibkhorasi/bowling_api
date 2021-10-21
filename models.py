from common import constants

class Frame(object):
    """
    Frame object which will hold score per frame
    """
    def __init__(self, frame_id):
        self.frame_id = frame_id,
        self.first_throw_score = -1
        self.second_throw_score = -1 
        self.third_throw_score = -1 
        self.frame_score = -1 
    def __repr__(self):
        return "<Frame: %r %r %r >" % (self.first_throw_score, self.second_throw_score, self.third_throw_score)

    def __str__(self): # string representation of a object
        return "<FrameStr: %r %r %r >" % (self.first_throw_score, self.second_throw_score, self.third_throw_score)

    def get_frame_id(self):
        return self.frame_id

    def get_first_throw_score(self):
        return self.first_throw_score
    
    def get_second_throw_score(self):
        return self.second_throw_score
    
    def get_third_throw_score(self):
        return self.third_throw_score
    
    def get_frame_score(self):
        return self.frame_score

    def set_first_throw_score(self, score):
        self.first_throw_score = score

    def set_second_throw_score(self, score):
        self.second_throw_score = score
    
    def set_third_throw_score(self, score):
        self.third_throw_score = score

    def set_frame_score(self, score):
        self.frame_score = score

    def add_firstwo_throws(self):
        self.frame_score = self.first_throw_score + self.second_throw_score

    def add_all_throws(self):
        self.frame_score = self.first_throw_score + self.second_throw_score + self.third_throw_score

    def is_strike(self):
        """Checks if given frame counter was strike or not.

        Args:
          frame_counter: Frame counter, 0 to 9.

        Returns: True or False.
        """
        return self.get_first_throw_score() == constants.MAX_PINS
    
    def is_spare(self):
        """Checks if given frame counter was spare or not.

        Args:
          frame_counter: Frame counter, 0 to 9.

        Returns: True or False.
        """
        return self.get_first_throw_score() + self.get_second_throw_score() == constants.MAX_PINS
