from tkinter import Tk
from InterfaceGameBoardSetter import InterfaceGameBoardSetter
from GameImageHandler import GameImageHandler

class GameInterface:
    def __init__(self) -> None:
        self.__window = Tk()
        self.__window.title("Trilha Alemã")
        self.__window.geometry("1440x1024")
        self.__window.configure(bg = "#327421")
        GameImageHandler.set_game_images()
        self.__interface_game_board_setter = InterfaceGameBoardSetter(self.__window)
        self.__interface_game_board_setter.set_game_board()
        self.__window.resizable(False, False)

    def start(self) -> None:
        self.__window.mainloop()
