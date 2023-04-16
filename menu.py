from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import src.board as board
from kivy.clock import Clock

Builder.load_file("menu.kv") 

class Menu(BoxLayout):
    def start_game(self):
        pass