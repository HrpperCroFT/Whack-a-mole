from src.constants import Data
from kivy.uix.image import Image
from kivy.clock import Clock

class Mole(Image):
    """ This is the class of game object — mole """
    
    def __init__(self, **kwargs):
        super(Mole, self).__init__(**kwargs)
        
        self.set_position(0)
        self.background_color = (1, 1, 1, 0)
        
    def appear(self):
        """ This is what happens when new mole appeares """
        
        self.set_position(1)
        Clock.schedule_interval(self.update, 1.0 / 10.0)
        
    def set_position(self, position):
        """ This function sets position of current mole """
        
        # if wrong position was given
        if position > 3 or position < 0:
            return
        
        self.position = position
        self.source = Data.POSITION_SOURCES[self.position]
    
    def update(self, dt):
        """ This function repeates while new mole appears """
        
        self.set_position(self.position + 1)
        
        # if mole appeared
        if self.position >= 3:
            Clock.unschedule(self.update)
            
    def reverse_update(self, dt):
        """ This function repeates while mole returns back after being
                                                                     whacked"""
        
        self.set_position(self.position - 1)
        if self.position <= 0:
            Clock.unschedule(self.reverse_update)
        
    def on_touch_down(self, touch):
        """ This function returns mole back if it was whacked and returns True,
                                                  otherwise it returns False"""
        
        # if touch not to this mole
        if not self.collide_point(*touch.pos):
            return False
        
        # if this mole hasn't appeared yet
        if self.position != 3:
            return False
        
        self.set_position(2)
        Clock.schedule_interval(self.reverse_update, 1.0 / 10.0)
        return True