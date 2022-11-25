#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Piece
import Position
import Board


class Player(object):
	def __init__(self, number: int, pieces_start_number: int = 12, turn: bool = False) -> None:
		self.__player_number: int = number
		self.__winner: bool = False
		self.__pieces_in_hand: int = pieces_start_number
		self.__pieces_on_board: int = 0
		self.__removed_pieces: int = 0
		self.__turn: bool = turn

# START OF GETTERS AND SETTERS 

	@property
	def player_number(self) -> int:
		return self.__player_number

	@player_number.setter
	def player_number(self, number: int) -> None:
		self.__player_number = number

	@property
	def winner(self) -> bool:
		return self.__winner

	@winner.setter
	def winner(self, is_winner: bool) -> None:
		self.__winner = is_winner

	@property
	def pieces_in_hand(self) -> int:
		return self.__pieces_in_hand
	
	@pieces_in_hand.setter
	def pieces_in_hand(self, pieces_number) -> None:
		self.__pieces_in_hand = pieces_number
	
	@property
	def pieces_on_board(self) -> int:
		return self.__pieces_on_board
	
	@pieces_on_board.setter
	def pieces_on_board(self, pieces_number) -> None:
		self.__pieces_on_board = pieces_number

	@property
	def removed_pieces(self) -> int:
		return self.__removed_pieces
	
	@removed_pieces.setter
	def removed_pieces(self, pieces_removed_number) -> None:
		self.__removed_pieces = pieces_removed_number
	
	@property
	def turn(self) -> bool:
		return self.__turn

	@turn.setter
	def turn(self, new_turn) -> None:
		self.__turn = new_turn

# END OF GETTERS AND SETTERS

	def get_turn(self) -> bool:
		return self.__turn
	
	def change_turn(self) -> None:
		self.__turn = not self.__turn

	def reset(self) -> None:
		pass

	def initialize(self) -> None:
		pass

	def select_position(self):
		pass

	def increment_pieces_on_board(self) -> None:
		self.__pieces_on_board += 1

	def decrement_pieces_in_hand(self) -> None:
		self.__pieces_on_board -= 1

	def decrement_pieces_in_hand(self) -> None:
		self.__pieces_in_hand -= 1

	def increment_removed_pieces(self) -> None:
		self.__removed_pieces += 1

	def can_do_fly(self) -> bool:
		pieces_number: int = self.__pieces_on_board
		return (pieces_number == 3)
	
	def verify_suficient_pieces_number(self) -> bool:
		pieces_number: int = self.__pieces_on_board
		return (pieces_number > 2)
