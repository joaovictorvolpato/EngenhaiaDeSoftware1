from Interface.InterfaceGameBoardSetter import InterfaceGameBoardSetter
from Interface.GameImageHandler import GameImageHandler
from Interface.InterfaceUpdater import InterfaceUpdater
from tkinter import  Tk, Menu, FALSE
from tkinter import messagebox
from tkinter import simpledialog
from Dog.dog_interface import DogPlayerInterface
from Dog.dog_actor import DogActor
from Game.Move import Move
from Game.Board import Board
from Game.Player import Player

class PlayerInterface(DogPlayerInterface):
    def __init__(self) -> None:
        self.__window = self.__create_window()
        GameImageHandler.set_game_images()
        self.__local_player, self.__remote_player = self.__create_players()
        self.__interface_updater: InterfaceUpdater = InterfaceUpdater() #Implement.
        self.__board: Board = Board(self.__local_player, self.__remote_player, self) #Start program in modelling
        self.__interface_game_board_setter = InterfaceGameBoardSetter(self.__board)
        self.__interface_game_board_setter.set_game_board()
        self.__window.resizable(False, False)
        self.__menubar, self.__menu_file = self.__create_menu()
        self.__dog_server_interface: DogActor = self.__connect_to_dog()
        self.__window.mainloop()

    @property
    def window(self) -> Tk:
        return self.__window

    @property
    def interface_updater(self) -> InterfaceUpdater:
        return self.__interface_updater

    @property
    def local_player(self) -> Player:
        return self.__local_player

    @property
    def remote_player(self) -> Player:
        return self.__remote_player

    @property
    def dog_server_interface(self) -> DogActor:
        return self.__dog_server_interface

    def __create_window(self) -> Tk:
        window = Tk()
        window.title("Trilha Alemã")
        window.geometry("1440x1024")
        window.configure(bg = "#327421")
        
        return window

    def __create_players(self) -> tuple[Player, Player]:
        local_player = Player(1, "", False, "VASCO")
        remote_player = Player(2, "", False, "AVAI")

        return local_player, remote_player

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
        #menu_file.add_command(label='restaurar estado inicial', command=self.start_game) #May be useless if game is gonna close

    def __connect_to_dog(self) -> DogActor:
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.__local_player.name = player_name
        dog_server_interface = DogActor()
        message = dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        return dog_server_interface

    def start_match(self) -> None:
            start_status = self.dog_server_interface.start_match(2)
            message = start_status.get_message()
            messagebox.showinfo(message=message)

    # def start_game(self) -> None: #Possibly useless if game is gonna close.
    #         print('start_game')

    def receive_start(self, start_status) -> None:
            message = start_status.get_message()   
            messagebox.showinfo(message=message)

    def receive_withdrawal_notification(self) -> None:
        self.notify_player("Your opponent has withdrawn from the match.")
        self.__board.receive_withdrawal_notification()

    def send_move(self, move: Move) -> None:
        self.__dog_server_interface.send_move(move)

    def receive_move(self, move: Move) -> None:
        pass

    def notify_player(self, message: str) -> None:
        messagebox.showinfo(message=message)

    def update_interface_image(self) -> None:
        self.__interface_updater.update_interface_image()
    
    def ask_user_accepts_draw(self) -> bool:
        return messagebox.askyesno(message="Do you accept to end the match in a draw?")
