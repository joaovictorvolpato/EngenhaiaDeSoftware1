from Interface.GameImageHandler import GameImageHandler
from Interface.InterfaceUpdater import InterfaceUpdater
from Interface.InterfaceGameBoard import InterfaceGameBoard
from Abstractions.AbstractGame import AbstractGame
from tkinter import  Tk, Menu, FALSE
from tkinter import messagebox
from tkinter import simpledialog
from Dog.dog_interface import DogPlayerInterface
from Dog.dog_actor import DogActor
from Game.Move import Move
from Game.Player import Player

class PlayerInterface(DogPlayerInterface):
    def __init__(self, game_ref) -> None:
        self.__game: AbstractGame = game_ref
        self.__window = self.__create_window()
        GameImageHandler.set_game_images()
        self.__interface_game_board = InterfaceGameBoard(self.__game.board)
        self.__window.resizable(False, False)
        self.__menubar, self.__menu_file = self.__create_menu()
        self.__dog_server_interface: DogActor = self.__connect_to_dog()

    @property
    def game(self):
        return self.__game

    @property
    def window(self) -> Tk:
        return self.__window

    @property
    def interface_updater(self) -> InterfaceUpdater:
        return self.__interface_updater

    @property
    def local_player(self) -> Player:
        return self.__game.local_player

    @property
    def remote_player(self) -> Player:
        return self.__game.remote_player

    @property
    def interface_game_board(self) -> InterfaceGameBoard:
        return self.__interface_game_board

    @property
    def dog_server_interface(self) -> DogActor:
        return self.__dog_server_interface

    def __create_window(self) -> Tk:
        window = Tk()
        window.title("Trilha Alemã")
        window.geometry("1440x1024")
        window.configure(bg = "#327421")
        
        return window

    def __create_menu(self) -> tuple[Menu, Menu]:
        menubar = self.__create_menubar()
        menu_file = self.__create_menu_file(menubar)
        self.__add_menu_commands(menu_file)

        return menubar, menu_file

    def __create_menubar(self) -> Menu:
        menubar = Menu(self.__window)
        menubar.option_add('*tearOff', FALSE)
        self.__window['menu'] = menubar

        return menubar

    def __create_menu_file(self, menubar) -> Menu:
        menu_file = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')

        return menu_file

    def __add_menu_commands(self, menu_file: Menu) -> None:
        menu_file.add_command(label='Iniciar jogo', command=self.start_match)

    def __connect_to_dog(self) -> DogActor:
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.__game.local_player.name = player_name
        dog_server_interface = DogActor()
        message = dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        return dog_server_interface

    def start_match(self) -> None:
            start_status = self.dog_server_interface.start_match(2)
            message = start_status.get_message()
            messagebox.showinfo(message=message)

    def receive_start(self, start_status) -> None:
            message = start_status.get_message()   
            messagebox.showinfo(message=message)

    def receive_withdrawal_notification(self) -> None:
        self.notify_player("Your opponent has withdrawn from the match.")
        self.__board.receive_withdrawal_notification()

    def send_move(self, move: Move) -> None:
        self.__dog_server_interface.send_move(move)

    def receive_move(self, move: Move) -> None:
       print(move)
       #  self.__board.execute_received_move(move)

    def notify_player(self, message: str) -> None:
        messagebox.showinfo(message=message)

    def update_interface_image(self) -> None:
        InterfaceUpdater.update_interface_image(self)
    
    def ask_user_accepts_draw(self) -> bool:
        return messagebox.askyesno(message="Do you accept to end the match in a draw?")

    def get_player_from_id(self, player_id: int) -> Player:
        try:
            if self.__game.local_player.id == player_id:
                return self.__game.local_player
            elif self.__game.remote_player.id == player_id:
                return self.__game.remote_player
        except ValueError:
            print("Invalid player id")
