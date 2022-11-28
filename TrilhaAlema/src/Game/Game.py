from Interface.PlayerInterface import PlayerInterface
from Interface.InterfaceGameBoard import InterfaceGameBoard
from Game.Player import Player
import os, signal
from Game.Board import Board
from Game.Move import Move

class Game:
    def __init__(self) -> None:
        self.__player_interface = PlayerInterface(self)
        self.__local_player, self.__remote_player = self.__create_players()
        self.__board: Board = Board(self.__local_player, self.__remote_player, self.__player_interface, self)
        self.__connect_interface_to_game()
        self.__connect_game_to_dog_server()
        self.__move: Move = Move()

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

    @property
    def move(self) -> Move:
        return self.__move
    
    @move.setter
    def move(self, move: Move) -> None:
        self.__move = move

    def __create_players(self) -> tuple[Player, Player]:
        local_player = Player(0, "", False, "") 
        remote_player = Player(0, "Opponent", False, "")

        return local_player, remote_player
    
    def __connect_interface_to_game(self) -> None:
        self.__player_interface.interface_game_board = InterfaceGameBoard(self.__board)
        
    def __connect_game_to_dog_server(self) -> None:
        self.__player_interface.dog_server_interface = self.__player_interface.connect_to_dog()

    def start_game(self) -> None:
        self.player_interface.window.mainloop()

    def end_program(self) -> None:
        os.kill(os.getpid(), signal.SIGINT)

    def get_player_from_id(self, player_id: int) -> Player:
        try:
            if self.__local_player.player_id == player_id:
                return self.__local_player
            elif self.__remote_player.player_id == player_id:
                return self.__remote_player
        except ValueError:
            print("Invalid player id")
