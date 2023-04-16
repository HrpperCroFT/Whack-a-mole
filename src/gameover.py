from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_file("src/gameover.kv")

class GameOver(BoxLayout):
    def close_window(self):
        pass