from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class Scores(Screen):
    def __init__(self, **kwargs):
        super(Scores, self).__init__(**kwargs)
        self.back_button = Button(text = "Back", size_hint = [.3, .2])
        self.scores_show = BoxLayout(orientation = "vertical", padding = [200, 0, 200, 150])
        self.add_widget(self.scores_show)
        self.getback_show = AnchorLayout(anchor_x = "center", anchor_y = "bottom")
        self.getback_show.add_widget(self.back_button)
        self.add_widget(self.getback_show)
    def update_scores(self, scores):
        self.scores_show.clear_widgets()
        for score in scores:
            if score < 0:
                break
            self.scores_show.add_widget(Button(text = str(score), background_color = (1, 0.7, 0.5, 0.5)))