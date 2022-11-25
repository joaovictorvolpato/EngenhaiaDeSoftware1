#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Player import Player
from Position import Position
from Move import Move


class Piece():
	def __init__(self, owner_player: Player, styles):
		self.__owner_player: Player = owner_player
		self.__styles = styles
		self.__position: Position = None
		self.__captured: bool = False
		self.__in_moinho: bool = False
		self.__move: Move = None

	# GETTERS AND SETTERS
	@property
	def owner_player(self) -> Player:
		return self.__owner_player

	@property
	def styles(self):
		return self.__styles

	@property
	def position(self) -> Position: 
		return self.__position

	@position.setter
	def position(self, new_position):
		self.__position = new_position

	@property
	def captured(self) -> bool:
		return self.__captured

	@captured.setter
	def captured(self, captured: bool):
		self.__captured = captured

	@property
	def in_moinho(self) -> bool:
		return self.__in_moinho

	@in_moinho.setter
	def in_moinho(self, in_moinho_value):
		self.__in_moinho = in_moinho_value

	@property
	def move(self) -> Move:
		return self.__move

	@move.setter
	def move(self, new_move):
		self.__move = new_move
