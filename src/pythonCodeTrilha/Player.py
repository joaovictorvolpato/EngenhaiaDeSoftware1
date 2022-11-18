#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Team
import Piece
import Position
import Board

class Player(object):
	def getTurn(self):
		"""@ReturnType boolean"""
		return self.___turn

	def changeTurn(self):
		pass

	def reset(self):
		pass

	def initialize(self):
		pass

	def selectPosition(self):
		pass

	def getPiecesOnBoardNumber(self):
		pass

	def decrementPiecesInBoard(self):
		pass

	def incrementRemovedPieces(self):
		pass

	def verify_blocked(self):
		"""@ReturnType boolean"""
		pass

	def get_player_number(self):
		pass

	def decrementPiecesInHand(self):
		pass

	def incrementPiecesOnBoard(self):
		pass

	def getPiecesInHand(self):
		"""@ReturnType int"""
		pass

	def canDoFly(self):
		"""@ReturnType boolean"""
		pass

	def setWinner(self):
		pass

	def __init__(self):
		self.___player_number = None
		"""@AttributeType int"""
		self.___team = None
		"""@AttributeType Team"""
		self.___pieces_in_hand = None
		"""@AttributeType int"""
		self.___turn = None
		"""@AttributeType boolean"""
		self.___winner = None
		"""@AttributeType boolean"""
		self.___pieces_on_board = None
		"""@AttributeType int"""
		self._unnamed_Piece_ = []
		"""@AttributeType Piece*
		# @AssociationType Piece[]
		# @AssociationMultiplicity 12"""
		self._unnamed_Position_ = None
		"""@AttributeType Position
		# @AssociationType Position"""
		self._unnamed_Board_ = None
		"""@AttributeType Board
		# @AssociationType Board"""
		self._unnamed_Team_ = None
		"""@AttributeType Team
		# @AssociationType Team
		# @AssociationKind Aggregation"""

