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
from src.constants import Data
import src.settings as settings


Config.set('graphics', 'width', str(Data.window_width))
Config.set('graphics', 'height', str(Data.window_height))
Config.set('graphics', 'resizable', False)
Config.write()

class WhackGame(Widget):
    pass

class WhackApp(App):
    def build(self):
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
        self.current_difficult = 0
        return self.manager
    
    def write_scores(self):
        self.score_storage.put("scores", store = self.scores);
        
    def read_scores(self):
        self.scores.clear()
        
        if self.score_storage.exists("scores"):
            self.scores = self.score_storage.get("scores")["store"]
            
        while len(self.scores) < 10:
            self.scores.append(-1)
    
    def add_result(self, result):
        for i in range(10):
            if self.scores[i] < result:
                for j in range(9, i, -1):
                    self.scores[j] = self.scores[j - 1] 
                self.scores[i] = result
                self.write_scores()
                break
    
    def setup_menu(self):
        self.menu = menu.Menu(name = "menu_screen")
        self.menu.start_game = self.start_decorator(self.menu.start_game)
        self.menu.open_scores = self.scores_decorator(self.menu.open_scores)
        self.manager.add_widget(self.menu)
        
    def setup_scores(self):
        self.scores_screen = scores.Scores(name = "scores_screen")
        self.scores_screen.back_button.on_press = self.back_to_menu_decorator(self.scores_screen.back_button.on_press)
        self.manager.add_widget(self.scores_screen)
    
    def setup_game_screen(self):
        self.game_screen = Screen(name = "game_screen")
        self.manager.add_widget(self.game_screen)
        
    def setup_gameover_screen(self):
        self.gameover_screen = gameover.GameOver(name = "gameover_screen")
        self.manager.add_widget(self.gameover_screen)
    
    def setup_settings_screen(self):
        self.settings_screen = settings.Settings(name = "settings_screen")
        self.settings_screen.change_difficulty = self.difficulty_decorator(self.settings_screen.change_difficulty)
        self.settings_screen.saves_delete = self.clear_saves_decorator(self.settings_screen.saves_delete)
        self.manager.add_widget(self.settings_screen)
        
    def start_decorator(self, func):
        def wrapper(*args, **kwargs):
            self.game = board.Board(self.current_difficult + 3, self.current_difficult + 3)
            Clock.schedule_interval(self.game.progress, 1.0 / 60.0)
            Clock.schedule_interval(self.game.update, 1.0)
            self.game.end_game = self.end_decorator(self.game.end_game)
            self.game_screen.add_widget(self.game)
            self.manager.current = "game_screen"
            func(*args, **kwargs)
        return wrapper
    
    def end_decorator(self, func):
        def wrapper(*args, **kwargs):
            Clock.unschedule(self.game.update)
            Clock.unschedule(self.game.progress)
            result = func(*args, **kwargs)
            self.game_screen.clear_widgets()
            self.gameover_screen.result_button.text = str(result)
            self.add_result(result)
            self.manager.current = "gameover_screen"
        return wrapper
    
    def scores_decorator(self, func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            self.scores_screen.update_scores(self.scores)
            self.manager.current = "scores_screen"
        return wrapper
    
    def back_to_menu_decorator(self, func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            self.manager.current = "menu_screen"
        return wrapper
    
    def difficulty_decorator(self, func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            self.current_difficult += 1
            self.current_difficult %= 3
            
            match self.current_difficult:
                case 0:
                    self.settings_screen.difficulty_button.text = Data.prefix_difficulty + "Easy"
                case 1:
                    self.settings_screen.difficulty_button.text = Data.prefix_difficulty + "Normal"
                case 2:
                    self.settings_screen.difficulty_button.text = Data.prefix_difficulty + "Hard"
        return wrapper
    
    def clear_saves_decorator(self, func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            self.score_storage.clear()
            self.scores.clear()
        return wrapper

if __name__ == '__main__':
    WhackApp().run()