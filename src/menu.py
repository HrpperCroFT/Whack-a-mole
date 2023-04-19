from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("src/menu.kv") 

class Menu(Screen):
    def start_game(self):
        pass
    def open_scores(self):
        pass