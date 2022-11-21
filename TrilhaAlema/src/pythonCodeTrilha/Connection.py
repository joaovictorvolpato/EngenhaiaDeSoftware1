#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Position import Position

class Connection():
	def __init__(self, id: int, positions: list[Position], ):
		self.__id = id
		self.__positions_list = positions
		self.__is_moinho = False

	# START GETTERS AND SETTERS

	@property
	def id(self) -> int:
		return self.__id

	@property
	def positions_list(self) -> list[Position]:
		return self.__positions_list

	@property
	def is_moinho(self) -> bool:
		return self.__is_moinho

	@is_moinho.setter
	def is_moinho(self, moinho) -> None:
		self.__is_moinho = moinho

	# END GETTERS AND SETTERS

	def set_is_moinho(self) -> None:
		self.__is_moinho = True
	
	def set_is_not_moinho(self) -> None:
		self.__is_moinho = False
