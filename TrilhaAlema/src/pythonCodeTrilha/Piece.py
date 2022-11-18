#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Player
import Position
import Move

class Piece(object):
	def getPiecePosition(self, aSelf):
		"""@ParamType aSelf Piece
		@ReturnType Position"""
		pass

	def getPiece(self):
		pass

	def getPieceOwner(self):
		"""@ReturnType Player"""
		pass

	def getPieceInMoinho(self):
		"""@ReturnType boolean"""
		pass

	def selectPiece(self):
		"""@ReturnType Piece"""
		pass

	def GetIsOccupied(self):
		"""@ReturnType boolean"""
		pass

	def setPieceNotInMoinho(self):
		pass

	def setPieceInMoinho(self):
		pass

	def setPieceCaptured(self):
		pass

	def __init__(self):
		self.___number_in_board = None
		"""@AttributeType int"""
		self.___number_in_player_hand = None
		"""@AttributeType int"""
		self.___owner_player = None
		"""@AttributeType Player"""
		self.___styles = None
		"""@AttributeType void"""
		self.___position = None
		"""@AttributeType Position"""
		self.___captured = None
		"""@AttributeType boolean"""
		self.___in_moinho = None
		"""@AttributeType boolean"""
		self._unnamed_Move_ = None
		"""@AttributeType Move
		# @AssociationType Move"""
		self._unnamed_Player_ = None
		"""@AttributeType Player
		# @AssociationType Player"""
		self._unnamed_Position_ = None
		"""@AttributeType Position
		# @AssociationType Position"""

