from tkinter import  Tk, Menu, FALSE
from InterfaceGameBoardSetter import InterfaceGameBoardSetter
from GameImageHandler import GameImageHandler
from tkinter import messagebox
from tkinter import simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from Move import Move

class PlayerInterface(DogPlayerInterface):
    def __init__(self) -> None:
        self.__window = self.__create_window()
        GameImageHandler.set_game_images()
        self.__interface_game_board_setter = InterfaceGameBoardSetter(self.__window)
        self.__interface_game_board_setter.set_game_board()
        self.__window.resizable(False, False)
        self.__menubar = self.__create_menubar()
        self.__menu_file = self.__create_menu_file()
        self.__add_menu_commands()
        self.__dog_server_interface: DogActor = self.__connect_to_dog()
        self.__window.mainloop()

    def __create_window(self) -> Tk:
        window = Tk()
        window.title("Trilha Alemã")
        window.geometry("1440x1024")
        window.configure(bg = "#327421")
        
        return window
    
    def __create_menubar(self) -> Menu:
        menubar = Menu(self.__window)
        menubar.option_add('*tearOff', FALSE)
        self.__window['menu'] = menubar

        return menubar

    def __create_menu_file(self) -> Menu:
        menu_file = Menu(self.__menubar)
        self.__menubar.add_cascade(menu=menu_file, label='File')

        return menu_file

    def __add_menu_commands(self) -> None:
        self.__menu_file.add_command(label='Iniciar jogo', command=self.start_match)
        self.__menu_file.add_command(label='restaurar estado inicial', command=self.start_game)

    def __connect_to_dog(self) -> DogActor:
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        return dog_server_interface

    def start_match(self) -> None:
            start_status = self.dog_server_interface.start_match(2)
            message = start_status.get_message()
            messagebox.showinfo(message=message)

    def start_game(self) -> None:
            print('start_game')

    def receive_start(self, start_status) -> None:
            message = start_status.get_message()   
            messagebox.showinfo(message=message)

    def send_move(self, move: Move) -> None:
        self.__dog_server_interface.send_move(move)
    
    def receive_move(self, move: Move) -> None:
        pass
