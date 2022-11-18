#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Position
import Piece
import Board

class Move(object):
	def setMoinho(self, aNumOfMoinhos):
		"""@ParamType aNumOfMoinhos int"""
		pass

	def setFInalPosition(self, aDestination):
		"""@ParamType aDestination Position"""
		pass

	def setMove(self, aSelectedPosition):
		"""@ParamType aSelectedPosition Position"""
		pass

	def setMoveNone(self):
		pass

	def setMovedPiece(self, aPiece):
		"""@ParamType aPiece Piece"""
		pass

	def getMoveType(self, aMove):
		"""@ParamType aMove Move
		@ReturnType string"""
		pass

	def setMoveType(self, aMovetype):
		"""@ParamType aMovetype string"""
		pass

	def sendMove(self):
		pass

	def __init__(self):
		self.___type = None
		"""@AttributeType string"""
		self.___moinho = None
		"""@AttributeType bool"""
		self.___final_position = None
		"""@AttributeType Position"""
		self.___start_position = None
		"""@AttributeType Position"""
		self.___piece = None
		"""@AttributeType Piece"""
		self._unnamed_Position_ = None
		"""@AttributeType Position
		# @AssociationType Position"""
		self._unnamed_Piece_ = None
		"""@AttributeType Piece
		# @AssociationType Piece"""
		self._unnamed_Board_ = None
		"""@AttributeType Board
		# @AssociationType Board"""

