from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
import src.menu as menu
import src.board as board
import src.gameover as gameover
import src.scores as scores
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.config import Config
from src.constants import Data, Difficulty
import src.settings as settings
from kivy.uix.image import Image


Config.set('graphics', 'width', str(Data.WINDOW_WIDTH))
Config.set('graphics', 'height', str(Data.WINDOW_HEIGHT))
Config.set('graphics', 'resizable', False)
Config.write()

class WhackGame(Widget):
    pass

class WhackApp(App):
    """ This is main class of application """
    
    def build(self):
        """ This function creates an application """
        
        self.score_storage = JsonStore('save\persistent.json')
        self.scores = []
        self.read_scores()
   
        self.manager = ScreenManager()
        self.setup_menu()
        self.setup_scores()
        self.setup_game_screen()
        self.setup_gameover_screen()
        self.setup_settings_screen()
        self.manager.current = "menu_screen"

        self.current_difficulty = Difficulty.easy

        return self.manager
    
    def write_scores(self):
        """ This function writes scores to .json storage """
        
        self.score_storage.put("scores", store = self.scores);
        
    def read_scores(self):
        """ This function reads scores from .json storage """
        
        self.scores.clear()
        
        if self.score_storage.exists("scores"):
            self.scores = self.score_storage.get("scores")["store"]
            
        while len(self.scores) < 10:
            self.scores.append([-1, ""])
    
    def add_result(self, result, name):
        """ This function saves current result """
        
        for i in range(10):
            if self.scores[i][0] < result:
                for j in range(9, i, -1):
                    self.scores[j][0] = self.scores[j - 1][0]
                    self.scores[j][1] = self.scores[j - 1][1]
                self.scores[i][0] = result
                self.scores[i][1] = name
                self.write_scores()
                break
    
    def setup_menu(self):
        """ This function creates main menu screen """
        
        self.menu = menu.Menu(name = "menu_screen")
        self.menu.start_game = self.start_decorator(self.menu.start_game)
        self.menu.open_scores = self.scores_decorator(self.menu.open_scores)
        self.manager.add_widget(self.menu)
        
    def setup_scores(self):
        """ This function creates scores screen """
        
        self.scores_screen = scores.Scores(name = "scores_screen")
        self.scores_screen.back_button.on_press = self.back_to_menu_decorator(
                                       self.scores_screen.back_button.on_press)
        self.manager.add_widget(self.scores_screen)
    
    def setup_game_screen(self):
        """ This function creates screen with game """
        
        self.game_screen = Screen(name = "game_screen")
        self.manager.add_widget(self.game_screen)
        
    def setup_gameover_screen(self):
        """ this function creates gameover screen """
        
        self.gameover_screen = gameover.GameOver(name = "gameover_screen")
        self.gameover_screen.get_name = self.get_name_decorator(
                                                 self.gameover_screen.get_name)
        self.manager.add_widget(self.gameover_screen)
    
    def setup_settings_screen(self):
        """ This function creates settings screen """
        
        self.settings_screen = settings.Settings(name = "settings_screen")
        self.settings_screen.change_difficulty = self.difficulty_decorator(
                                        self.settings_screen.change_difficulty)
        self.settings_screen.saves_delete = self.clear_saves_decorator(
                                             self.settings_screen.saves_delete)
        self.manager.add_widget(self.settings_screen)
        
    def start_decorator(self, func):
        """ Decorator for function of starting game """
        
        def wrapper(*args, **kwargs):
            self.__name__ = func.__name__
            self.__doc__ = func.__doc__ 
            self.game_screen.add_widget(Image(source = Data.BACKGROUND_SOURCE))
            self.game = board.Board(self.current_difficulty.value + 3,
                                             self.current_difficulty.value + 3)
            Clock.schedule_interval(self.game.progress, 1.0 / 60.0)
            Clock.schedule_interval(self.game.update, 1.0)
            self.game.end_game = self.end_decorator(self.game.end_game)
            self.game_screen.add_widget(self.game)
            self.manager.current = "game_screen"
            func(*args, **kwargs)
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
    
    def end_decorator(self, func):
        """ Decorator for function of ending game """
        
        def wrapper(*args, **kwargs):
            self.__name__ = func.__name__
            self.__doc__ = func.__doc__
            Clock.unschedule(self.game.update)
            Clock.unschedule(self.game.progress)
            self.current_result = func(*args, **kwargs)
            self.game_screen.clear_widgets()
            self.gameover_screen.showing_score.text = Data.SCORE_SHOW_PREFIX \
                            + str(self.current_result) + Data.SCORE_SHOW_SUFFIX
            self.gameover_screen.name_input.text = ""
            self.manager.current = "gameover_screen"
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
    
    def scores_decorator(self, func):
        """" Decorator for function of updating scores """
        
        def wrapper(*args, **kwargs):
            self.__name__ = func.__name__
            self.__doc__ = func.__doc__
            func(*args, **kwargs)
            self.scores_screen.update_scores(self.scores)
            self.manager.current = "scores_screen"
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
    
    def back_to_menu_decorator(self, func):
        """ Decorator for function of returning to menu """
        
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            self.manager.current = "menu_screen"
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
    
    def difficulty_decorator(self, func):
        """" Decorator for function of changing difficulty """
        
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            match self.current_difficult:
                case Difficulty.easy:
                    self.current_difficulty = Difficulty.normal
                    self.settings_screen.difficulty_button.text = \
                                              Data.PREFIX_DIFFICULTY + "Normal"
                case Difficulty.normal:
                    self.current_difficulty = Difficulty.hard
                    self.settings_screen.difficulty_button.text = \
                                                Data.PREFIX_DIFFICULTY + "Hard"
                case Difficulty.hard:
                    self.current_difficulty = Difficulty.easy
                    self.settings_screen.difficulty_button.text = \
                                                Data.PREFIX_DIFFICULTY + "Easy"
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
    
    def clear_saves_decorator(self, func):
        """ Decorator for clearing saves function """
        
        def wrapper(*args, **kwargs):
            self.__name__ = func.__name__
            self.__doc__ = func.__doc__
            func(*args, **kwargs)
            self.score_storage.clear()
            self.scores.clear()
            self.scores = [[-1, ""] for _ in range(10)]
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper
    
    def get_name_decorator(self, func):
        """ Decorator for getting name function """
        
        def wrapper(*args, **kwargs):
            self.__name__ = func.__name__
            self.__doc__ = func.__doc__
            func(*args, **kwargs)
            name = self.gameover_screen.name_input.text
            self.add_result(self.current_result, name)
            self.manager.current = "menu_screen"
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        
        return wrapper

if __name__ == '__main__':
    WhackApp().run()