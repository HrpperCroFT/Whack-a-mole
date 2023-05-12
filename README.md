# Whack-a-mole
>Whack-a-mole is one of the most famous games, your purpose is to whack moles that appear on the field.

# How to run application
>Windows — run Whack-a-mole.bat

>Linux or MacOS — execute Whack-a-mole.sh

# How to play
After starting the application, the program creates a screen manager, that contains several screens of game. First screen is "Menu"

# Menu screen
This screen contains ther buttons: "New game", "Best scores" and "Settings"

* `"New game" button` creates new game screen and switches to it

* '"Best scores" button` swithes to screen with best ten scores

* `"Settings" button` switches to screen with options

# Game screen
This screen contains field with moles (inherritors of class Image), a counter on the top right showing current score and progress bar on the top left showing time until the end of the game. You could click on moles, when they appear, then you get point, mole disappears and time until the end slightly increases. When there is no time left, the game screen closes and there appears gameover screen.

# Gameover screen
This screen contains text input field, where you could write your name, your score and button "Save result". If you write your name and push the button, this score will be saved and screen switches to menu.

# Best scores screen
This screen contains table with 10 best results and button "Back". Pushing this button will return you to menu.

# Setings screen
This screen contains three buttons: "Current difficulty: 'difficulty'", "Delete all scores" and "Back".

* `"Current difficulty: 'difficulty'" button` changes difficulty of game. There are three variants: "Easy", "Normal" and "Hard". They means size of game field, 3*3, 4*4 and 5*5.

* `"Delete all scores" button` clears saved best results.

* `"Back" button ` switches to menu screen.
