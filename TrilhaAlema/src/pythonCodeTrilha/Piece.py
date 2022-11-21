#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Player
import Position
import Move

class Piece(object):
	def __init__(self):
		self.__number_in_board = None
		"""@AttributeType int"""
		self.__number_in_player_hand = None
		"""@AttributeType int"""
		self.__owner_player = None
		"""@AttributeType Player"""
		self.__styles = None
		"""@AttributeType void"""
		self.__position = None
		"""@AttributeType Position"""
		self.__captured = None
		"""@AttributeType boolean"""
		self.__in_moinho = None
		"""@AttributeType boolean"""
		self.__Move = None
		"""@AttributeType Move
		# @AssociationType Move"""
		self.__Player = None
		"""@AttributeType Player
		# @AssociationType Player"""
		self.__Position = None
		"""@AttributeType Position
		# @AssociationType Position"""

	@property
	def in_moinho(self):
		return self.__in_moinho

	@in_moinho.setter
	def in_moinho(self, bool):
		self.__in_moinho = bool

	@property
	def Position(self) -> Position: 
		return self.__Position

	@property
	def Player(self) -> Player:
		return self.__Player

	@property
	def Position(self) -> Position:
		return self.__Position

	@property
	def captured(self):
		return self.__captured

	@captured.setter
	def captured(self, bool):
		self.__captured = bool
	


