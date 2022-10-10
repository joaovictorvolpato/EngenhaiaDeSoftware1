from tkinter import Tk
from InterfaceGameBoardSetter import InterfaceGameBoardSetter
from GameImageHandler import GameImageHandler
from tkinter import messagebox
from tkinter import simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

class GameInterface(DogPlayerInterface):
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
        self.__connect_to_dog()
        self.__window.mainloop()

    def __connect_to_dog(self) -> None:
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)
