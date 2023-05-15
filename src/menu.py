from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from src.constants import Data

Builder.load_file("src/menu.kv") 

class Menu(Screen):
    """ This is class of main menu screen """
    
    background_image = Data.BACKGROUND_SOURCE
    
    def start_game(self):
        """ This function starts new game """
        
        NotImplemented
    
    def open_scores(self):
        """ This function opens best scores screen """ 
        
        NotImplemented