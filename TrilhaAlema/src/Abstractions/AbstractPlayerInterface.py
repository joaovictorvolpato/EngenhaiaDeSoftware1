from abc import ABC, abstractmethod
from tkinter import Tk, Menu, FALSE
from Dog.dog_actor import DogActor
from Game.Move import Move

class AbstractPlayerInterface(ABC):
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
