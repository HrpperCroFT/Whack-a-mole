from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.constants import Data


Builder.load_file("src/gameover.kv")

class GameOver(Screen):
    """ This is class of gameover screen """ 
    
    background_image = Data.BACKGROUND_SOURCE
    
    def get_name(self):
        """ This function returns name of current player """
        
        return self.name_input.text
    