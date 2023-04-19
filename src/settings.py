from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("src/settings.kv") 

class Settings(Screen):
    def change_difficulty(self):
        pass
    def saves_delete(self):
        pass