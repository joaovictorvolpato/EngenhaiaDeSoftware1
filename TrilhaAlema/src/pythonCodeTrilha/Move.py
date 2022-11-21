#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Position
from Position import Position
from Piece import Piece
import Board
from enum import Enum

class MoveType(Enum):
	PLACE_PIECE = 1
	MOVE_PIECE = 2
	PLACE_AND_REMOVE_PIECE = 3
	MOVE_AND_REMOVE_PIECE = 4
	DRAW_PROPOSE = 5
	ACCEPT_DRAW_PROPOSE = 6
	DECLINE_DRAW_PROPOSE = 7


class Move(object):
	class_move_type = MoveType()

	def __init__(self):
		self.__type = None
		"""@AttributeType MoveType"""
		self.__moinho = None
		"""@AttributeType int"""
		self.__final_position = None
		"""@AttributeType Position"""
		self.__start_position = None
		"""@AttributeType Position"""
		self.__piece = None
		"""@AttributeType Piece"""

	@property
	def type(self) -> MoveType:
		return self.__type

	@type.setter
	def type(self, MoveType):
		self.__type = MoveType

	@property
	def moinho(self):
		return self.__moinho

	@moinho.setter
	def moinho(self, num_of_moinhos: int):
		self.__moinho = num_of_moinhos

	@property
	def final_position(self):
		return self.__final_position

	@final_position.setter
	def final_position(self, position: Position):
		self.__final_position = position

	@property
	def start_position(self):
		return self.__start_position

	@start_position.setter
	def start_position(self, position: Position):
		self.__start_position = position

	@property
	def piece(self):
		return self.__piece

	@piece.setter
	def piece(self, piece : Piece):
		self.__piece = piece

	def setMoveNone(self):
		self.__type = None
		self.__moinho = None
		self.__final_position = None
		self.__start_position = None
		self.__piece = None
