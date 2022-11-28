from Interface.PlayerInterface import PlayerInterface
from Game.Player import Player
import os, signal
from Game.Board import Board

class Game:
    def __init__(self) -> None:
        self.__player_interface = PlayerInterface(self)
        self.__local_player, self.__remote_player = self.__create_players()
        self.__board: Board = Board(self.__local_player, self.__remote_player, self.__player_interface)

    @property
    def player_interface(self) -> PlayerInterface:
        return self.__player_interface

    @property
    def local_player(self) -> Player:
        return self.__local_player

    @property
    def remote_player(self) -> Player:
        return self.__remote_player
    
    @property
    def board(self) -> Board:
        return self.__board

    def __create_players(self) -> tuple[Player, Player]:
        local_player = Player(0, "", False, "") 
        remote_player = Player(0, "", False, "")

        return local_player, remote_player

    def start_game(self) -> None:
        self.player_interface.window.mainloop()
        
    def end_program(self) -> None:
        os.kill(os.getpid(), signal.SIGINT)
