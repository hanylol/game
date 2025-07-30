from ursina import *

class MainMenu(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)

        self.start_button = Button(
            parent=self,
            text='Start Game',
            scale=(0.2, 0.05),
            y=0.1,
            on_click=self.start_game
        )

        self.quit_button = Button(
            parent=self,
            text='Quit',
            scale=(0.2, 0.05),
            y=-0.1,
            on_click=application.quit
        )

    def start_game(self):
        self.disable()
        # This is where you would start the game
        # For now, we'll just print a message
        print("Starting game...")
