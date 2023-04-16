from kivy.uix.button import Button

class Mole(Button):
    def __init__(self, **kwargs):
        super(Mole, self).__init__(**kwargs)
        self.text = "No mole"
        self.isout = False
        self.background_color = (0, 0, 0, 0)
    def appear(self):
        self.text = "I'm here, hello"
        self.isout = True
    def on_press(self):
        last_state = self.isout
        self.text = "No mole"
        self.isout = False
        return last_state