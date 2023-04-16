from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
import menu
import src.board as board
import src.gameover as gameover
from kivy.clock import Clock

class WhackGame(Widget):
    pass

class WhackApp(App):
    def build(self):
        self.window = Screen()
        self.menu = menu.Menu()
        self.menu.start_game = self.start_decorator(self.menu.start_game)
        self.window.add_widget(self.menu)
        return self.window
    def start_decorator(self, func):
        def wrapper(*args, **kwargs):
            self.window.clear_widgets()
            self.game = board.Board()
            Clock.schedule_interval(self.game.progress, 1.0 / 60.0)
            Clock.schedule_interval(self.game.update, 1.0)
            self.game.end_game = self.end_decorator(self.game.end_game)
            self.window.add_widget(self.game);
            func(*args, **kwargs)
        return wrapper
    def end_decorator(self, func):
        def wrapper(*args, **kwargs):
            Clock.unschedule(self.game.update)
            Clock.unschedule(self.game.progress)
            result = func(*args, **kwargs)
            self.window.clear_widgets()
            self.menu = menu.Menu()
            self.menu.start_game = self.start_decorator(self.menu.start_game)
            self.gameover = gameover.GameOver()
            self.gameover.result_button.text = str(result)
            self.gameover.close_window = self.close_decorator(self.gameover.close_window)
            self.window.add_widget(self.menu)
            self.window.add_widget(self.gameover)
        return wrapper
    def close_decorator(self, func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            self.window.remove_widget(self.gameover)
        return wrapper

if __name__ == '__main__':
    WhackApp().run()