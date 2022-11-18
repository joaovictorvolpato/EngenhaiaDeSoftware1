#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Player
import Piece
import Board
import Move
import Connection

class Position(object):
	def placePiece(self, aSelectedPosition, aPlayer):
		"""@ParamType aSelectedPosition Position
		@ParamType aPlayer Player"""
		pass

	def getPositon(self, aLine, aColumn):
		"""@ParamType aLine int
		@ParamType aColumn int
		@ReturnType Position"""
		pass

	def removePiece(self, aPositiontoremove):
		"""@ParamType aPositiontoremove Position"""
		pass

	def getPositionType(self):
		pass

	def setPositionFree(self, aPosition):
		"""@ParamType aPosition Position"""
		pass

	def isOccupied(self, aPosition):
		"""@ParamType aPosition Position"""
		pass

	def operation(self):
		pass

	def getPieceOnPosition(self, aPosition):
		"""@ParamType aPosition Position
		@ReturnType Piece"""
		pass

	def setIsOccupied(self):
		pass

	def setPlayerOnPos(self, aPlayer):
		"""@ParamType aPlayer Player"""
		pass

	def get_conections(self):
		"""@ReturnType list"""
		pass

	def getPlayerOnPosition(self):
		"""@ReturnType Player"""
		pass

	def __init__(self):
		self.___matrix_position = None
		"""@AttributeType tuple"""
		self.___neighborhoods = None
		"""@AttributeType Postion"""
		self.___is_occupied = None
		"""@AttributeType boolean"""
		self.___line = None
		"""@AttributeType int"""
		self.___column = None
		"""@AttributeType int"""
		self.___player_on_pos = None
		"""@AttributeType Player"""
		self.___piece = None
		"""@AttributeType Piece"""
		self.___connections = None
		"""@AttributeType list"""
		self._unnamed_Board_ = None
		"""@AttributeType Board
		# @AssociationType Board"""
		self._unnamed_Piece_ = None
		"""@AttributeType Piece
		# @AssociationType Piece"""
		self._unnamed_Move_ = None
		"""@AttributeType Move
		# @AssociationType Move"""
		self._unnamed_Connection_1 = None
		"""@AttributeType Connection
		# @AssociationType Connection"""
		self._unnamed_Player_ = None
		"""@AttributeType Player
		# @AssociationType Player"""

