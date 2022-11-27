import os
from Game.Game import Game
from Config.Path import Path

def get_src_path() -> str:
    return os.getcwd()

if __name__ == "__main__":
    src_path = get_src_path()
    Path.set_src_path(src_path)
    game = Game()
