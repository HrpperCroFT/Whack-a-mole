from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from src.constants import Data
from kivy.uix.image import Image

class Scores(Screen):
    """ This is the screen contains best scores of this game """
    
    def __init__(self, **kwargs):
        super(Scores, self).__init__(**kwargs)
        
        self.add_widget(Image(source = Data.BACKGROUND_SOURCE))
        
        self.back_button = Button(text = "Back", size_hint = [.3, .2])
        
        self.scores_show = GridLayout(rows = 10, cols = 1, padding = [200, 0,
                                                                     200, 150])
        self.add_widget(self.scores_show)
        
        self.getback_show = AnchorLayout(anchor_x = "center",
                                                           anchor_y = "bottom")
        self.getback_show.add_widget(self.back_button)
        self.add_widget(self.getback_show)
        
    def update_scores(self, scores):
        """ This function updates scores on the screen """
        
        self.scores_show.clear_widgets()
        for score in scores:
            if score[0] < 0:
                break
            self.scores_show.add_widget(Label(text = str(score[0])
                           + ", player: " + score[1], size_hint = [None, None],
                                       size = [200, 50], color = [0, 0, 0, 1]))