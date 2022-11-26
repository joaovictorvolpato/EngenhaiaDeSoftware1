#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Position
from Position import Position
from Piece import Piece
from Board import Board
from enum import Enum

#Change numbers to strings
class MoveType(Enum):
	PLACE_PIECE = 1
	MOVE_PIECE = 2
	PLACE_AND_REMOVE_PIECE = 3
	MOVE_AND_REMOVE_PIECE = 4
	DRAW_PROPOSE = 5
	ACCEPT_DRAW_PROPOSE = 6
	DECLINE_DRAW_PROPOSE = 7


class Move():
	class_move_type = MoveType()

	def __init__(self, class_move_type: MoveType):
		self.__type = class_move_type
		self.__moinhos = 0
		self.__final_position: Position = None
		self.__start_position: Position = None
		self.__piece: Piece = None

	@property
	def type(self) -> MoveType:
		return self.__type

	@type.setter
	def type(self, move_type: MoveType) -> None:
		self.__type = move_type

	@property
	def moinhos(self) -> int:
		return self.__moinhos

	@moinhos.setter
	def moinhos(self, num_of_moinhos: int) -> None:
		self.__moinhos = num_of_moinhos

	@property
	def final_position(self) -> Position:
		return self.__final_position

	@final_position.setter
	def final_position(self, final_position: Position) -> None:
		self.__final_position = final_position

	@property
	def start_position(self) -> Position:
		return self.__start_position

	@start_position.setter
	def start_position(self, start_position: Position) -> None:
		self.__start_position = start_position

	@property
	def piece(self) -> Piece:
		return self.__piece

	@piece.setter
	def piece(self, piece : Piece) -> None:
		self.__piece = piece

	def set_move_none(self):
		self.__type = None
		self.__moinhos = 0
		self.__final_position = None
		self.__start_position = None
		self.__piece = None
