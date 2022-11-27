#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Game.Position import Position
from Game.Piece import Piece
from Game.Board import Board
from Interface.PlayerInterface import PlayerInterface
from Game.Player import Player

class InterfaceUpdater(object):
	def set_message(self, aMessage):
		"""@ParamType aMessage string"""
		pass

	def set_player1_pieces(self, *aPlayer1_pieces):
		"""@ParamType aPlayer1_pieces Piece*"""
		pass

	def set_player2_pieces(self, *aPlayer2_pieces):
		"""@ParamType aPlayer2_pieces Piece*"""
		pass

	def get_message(self):
		"""@ReturnType string"""
		pass

	def get_player1_pieces(self):
		"""@ReturnType Piece*"""
		pass

	def get_player2_pieces(self):
		"""@ReturnType Piece*"""
		pass

	def updateInterfaceImage(self, aPlayer_interface):
		"""@ParamType aPlayer_interface PlayerInterface"""
		pass

	def displayPiecesOnPositions(self, aPlayer_interface, aPositions_to_update):
		"""@ParamType aPlayer_interface PlayerInterface
		@ParamType aPositions_to_update list"""
		pass

	def displayPiecesInLocalPlayerHand(self, aPlayer_interface, aPieces_in_local_player_hand):
		"""@ParamType aPlayer_interface PlayerInterface
		@ParamType aPieces_in_local_player_hand int"""
		pass

	def displayPiecesInRemoteplayerHand(self, aPlayer_interface, aPieces_in_remote_player_hand):
		"""@ParamType aPlayer_interface PlayerInterface
		@ParamType aPieces_in_remote_player_hand int"""
		pass

	def displayWinner(self, aPlayer_interface, aWinner_to_display):
		"""@ParamType aPlayer_interface PlayerInterface
		@ParamType aWinner_to_display Player"""
		pass

	def notifyAbandonedMatch(self, aPlayer_interface, aMatch_was_abandoned):
		"""@ParamType aPlayer_interface PlayerInterface
		@ParamType aMatch_was_abandoned boolean"""
		pass

	def notifyDraw(self, aPlayer_interface):
		"""@ParamType aPlayer_interface PlayerInterface"""
		pass

	def __init__(self):
		self.___message = None
		"""@AttributeType string"""
		self.___map = None
		"""@AttributeType int*"""
		self.___selected_position = None
		"""@AttributeType Position"""
		self.___player1_pieces = None
		"""@AttributeType Piece*"""
		self.___player2_pieces = None
		"""@AttributeType Piece*"""
		self._unnamed_Board_ = None
		"""@AttributeType Board
		# @AssociationType Board"""
		self._unnamed_PlayerInterface_ = None
		"""@AttributeType PlayerInterface
		# @AssociationType PlayerInterface"""

