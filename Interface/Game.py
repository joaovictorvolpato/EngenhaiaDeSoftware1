from GameInterface import GameInterface

class Game:
    def __init__(self) -> None:
        self.game_interface = GameInterface()

    def start(self):
        self.game_interface.start()