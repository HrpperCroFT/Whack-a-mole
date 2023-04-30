import enum

class Difficulty(enum.IntEnum):
    """ It enumerates difficulties """
    
    easy = 0
    normal = 1
    hard = 2

class Data():
    """ This is the class of global constants """
    
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 600
    
    PREFIX_DIFFICULTY = "Current difficulty: "
    
    POSITION_SOURCES = ["img/state-0.png", "img/state-1.png",
                                          "img/state-2.png", "img/state-3.png"]
    BACKGROUND_SOURCE = "img/background.png"
    
    SCORE_SHOW_PREFIX = "Your score "
    SCORE_SHOW_SUFFIX = "! Please, write your name here."
    
    def __init__(self):
        pass