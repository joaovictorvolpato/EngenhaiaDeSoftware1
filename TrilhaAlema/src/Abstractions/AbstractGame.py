from Interface.PlayerInterface import PlayerInterface
from Game.Player import Player
from abc import ABC, abstractmethod
from Game.Board import Board
from Game.Move import Move

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
    
    @property
    @abstractmethod
    def move(self) -> Move:
        pass

    @abstractmethod
    def __create_players(self) -> tuple[Player, Player]:
        pass

    @abstractmethod
    def start_game(self) -> None:
        pass
    
    @abstractmethod
    def end_program(self) -> None:
        pass

    @abstractmethod
    def get_player_from_id(self, player_id: int) -> Player:
       pass
