from Interface.PlayerInterface import PlayerInterface
from Game.Player import Player
from abc import ABC, abstractmethod
from Game.Board import Board

class AbstractGame:
    @property
    @abstractmethod
    def player_interface(self) -> PlayerInterface:
        pass

    @property
    @abstractmethod
    def local_player(self) -> Player:
        pass

    @property
    @abstractmethod
    def remote_player(self) -> Player:
        pass

    @property
    @abstractmethod
    def board(self) -> Board:
        pass

    @abstractmethod
    def __create_players(self) -> tuple[Player, Player]:
        pass

    @abstractmethod
    def start_game(self) -> None:
        pass
        
    def end_program(self) -> None:
        pass

 