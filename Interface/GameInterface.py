from tkinter import Tk, Canvas

class GameInterface:
    def __init__(self) -> None:
        self.__window = Tk()
        self.__window.title("Trilha Alemã")
        self.__window.geometry("1440x1024")
        self.__window.configure(bg = "#327421")
        from GameBoardSetter import GameBoardSetter
        self.__game_board_setter = GameBoardSetter(self.__window)

        self.__window.resizable(False, False)

    def start(self) -> None:
        self.__window.mainloop()
