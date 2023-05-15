from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar as KivyProgressBar
from kivy.uix.label import Label
import src.mole as mole
import random as rnd

class Board(BoxLayout):
    """ This is the main class of game itself """
    countx = 3
    county = 3
    def __init__(self, cntx = 3, cnty = 3, **kwargs):
        if cntx <= 0 or cnty <= 0:
            raise Exception()
        super(Board, self).__init__(**kwargs)
        
        # settting general variables' values 
        self.moles = []
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10
        self.countx = cntx
        self.county = cnty
        
        # possibility to watch your current game state
        box = BoxLayout(orientation = "horizontal")
        
        self.progressbar = KivyProgressBar(max=20.0, value=20.0,
                                                          size_hint=(0.5, 0.2))
        self.counter = 0
        self.counter_label = Label(text = "0", color = (0, 0, 0, 1))
        box.add_widget(self.progressbar)
        box.add_widget(self.counter_label)
        
        self.add_widget(box)
        
        # creating game action field
        self.game_board = GridLayout(cols = cntx, rows = cnty)
        
        for _ in range(cnty):
            for i in range(cntx):
                lastmole = mole.Mole()
                lastmole.on_touch_down = self.whack_decorator(
                                                        lastmole.on_touch_down)
                self.game_board.add_widget(lastmole)
                self.moles.append(lastmole)
        
        self.add_widget(self.game_board)
        
    def whack_decorator(self, func):
        """ This decorator is for function of whacking one more mole """
        
        def wrapper(*args, **kwargs):
            if func(*args, *kwargs):
                self.counter += 1
                self.counter_label.text = str(self.counter)
                self.progressbar.value = min(self.progressbar.value + 1.0
                                                             + 1.0 / 7.0, 20.0)
                return True
            return False
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
    
    def update(self, dt):
        """ This function makes one random mole appear """
        
        currentid = rnd.randint(0, self.countx * self.county - 1)
        if self.moles[currentid].position == 0:
            self.moles[currentid].appear()
            
    def progress(self, dt):
        """ This function decreeses time until the end of the game """
        
        self.progressbar.value -= 1.0 / 60.0
        if self.progressbar.value <= 0:
            self.end_game()
            
    def end_game(self):
        """ This function means that the game is over """
        
        return self.counter