from abc import ABC, abstractmethod
from tkinter import Tk, Menu, FALSE
from Dog.dog_actor import DogActor
from Game.Move import Move
from Game.Player import Player
from Abstractions.AbstractGame import AbstractGame

class AbstractPlayerInterface(ABC):
    @property
    @abstractmethod
    def game(self) -> AbstractGame:
        pass
    
    @property
    @abstractmethod
    def window(self) -> Tk:
        return self.__window

    @property
    @abstractmethod
    def interface_game_board(self) -> None:
        pass

    @property
    @abstractmethod
    def dog_server_interface(self) -> DogActor:
        pass
    
    @abstractmethod
    def __create_window(self) -> Tk:
        pass
    
    @abstractmethod
    def __create_menubar(self) -> Menu:
        pass

    @abstractmethod
    def __create_menu_file(self) -> Menu:
        pass

    @abstractmethod
    def __add_menu_commands(self) -> None:
        pass

    @abstractmethod
    def __connect_to_dog(self) -> DogActor:
        pass

    @abstractmethod
    def start_match(self) -> None:
        pass

    @abstractmethod
    def start_game(self) -> None:
        pass

    @abstractmethod
    def receive_start(self, start_status) -> None:
        pass

    @abstractmethod
    def send_move(self, move: Move) -> None:
        pass
    
    @abstractmethod
    def receive_move(self, move: Move) -> None:
        pass
    
    @abstractmethod
    def notify_player(self, message: str) -> None:
        pass

    @abstractmethod
    def end_program(self) -> None:
        pass

    @abstractmethod
    def update_interface_image(self) -> None:
        pass
