from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.constants import Data

Builder.load_file("src/settings.kv") 

class Settings(Screen):
    """ This is class of settings screen """
    
    background_image = Data.BACKGROUND_SOURCE
    
    def change_difficulty(self):
        """ This function changes difficulty of the game """
        
        NotImplemented
    
    def saves_delete(self):
        """ This function deletes saved scores """
        
        NotImplemented