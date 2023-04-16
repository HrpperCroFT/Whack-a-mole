from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar as KivyProgressBar
from kivy.uix.label import Label
import src.mole as mole
import random as rnd

class Board(BoxLayout):
    countx = 3
    county = 3
    def __init__(self, cntx = 3, cnty = 3, **kwargs):
        if cntx <= 0 or cnty <= 0:
            raise Exception()
        super(Board, self).__init__(**kwargs)
        self.moles = []
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10
        self.countx = cntx
        self.county = cnty
        self.progressbar = KivyProgressBar(max=20.0, value=20.0, size_hint=(0.5, 0.2))
        self.counter = 0
        self.counter_label = Label(text = "0")
        box = BoxLayout(orientation = "horizontal")
        box.add_widget(self.progressbar)
        box.add_widget(self.counter_label)
        self.add_widget(box)
        for _ in range(cnty):
            nbox = BoxLayout(orientation = "horizontal", spacing = 10)
            for i in range(cntx):
                lastmole = mole.Mole()
                lastmole.on_press = self.decorator(lastmole.on_press)
                nbox.add_widget(lastmole)
                self.moles.append(lastmole)
            self.add_widget(nbox)
    def decorator(self, func):
        def wrapper(*args, **kwargs):
            if func(*args, *kwargs):
                self.counter += 1
                self.counter_label.text = str(self.counter)
                self.progressbar.value = min(self.progressbar.value + 1.0 / 5.0, 20.0)
                return True
            return False
        return wrapper
    def update(self, dt):
        currentid = rnd.randint(0, self.countx * self.county - 1)
        self.moles[currentid].appear()
    def progress(self, dt):
        self.progressbar.value -= 1.0 / 60.0
        if self.progressbar.value <= 0:
            self.end_game()
    def end_game(self):
        return self.counter