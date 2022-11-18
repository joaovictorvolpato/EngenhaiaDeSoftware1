#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Player
import Position
import Move
import Piece
import InterfaceUpdater
import PlayerInterface

class Board(object):
	def colocarPeca(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def doPlacePiece(self):
		pass

	def evaluateMoinho(self):
		pass

	def executeMovePiece(self, aPiece, aDestination):
		"""@ParamType aPiece Piece
		@ParamType aDestination Position"""
		pass

	def ProposeDraw(self):
		pass

	def start_match(self, *aPlayers, aLocal_player_id):
		"""@ParamType aPlayers string*
		@ParamType aLocal_player_id string"""
		pass

	def get_status(self):
		"""@ReturnType InterfaceImage"""
		pass

	def executeMove(self, aMove):
		"""@ParamType aMove Move"""
		pass

	def endGame(self):
		pass

	def restartMove(self):
		pass

	def setBoardPositionMatrix(self):
		pass

	def getMatchStatus(self):
		pass

	def registerInvalidMove(self):
		pass

	def notifyPlayerNotTurn(self):
		pass

	def receiveWithdrawalNotification(self):
		pass

	def set_winner(self, aLocal_player):
		"""@ParamType aLocal_player Player"""
		pass

	def finishTurn(self):
		pass

	def reset_match(self):
		pass

	def executeRemovePiece(self):
		pass

	def getSelectedPiece(self):
		"""@ReturnType Piece"""
		pass

	def getSelectedPosition(self):
		"""@ReturnType Position"""
		pass

	def operation(self):
		pass

	def getGamePhase(self):
		"""@ReturnType string"""
		return self.___gamePhase

	def setSelectedPosition(self, aPosition):
		"""@ParamType aPosition Position"""
		pass

	def clickedPosition(self, aLine, aColumn):
		"""@ParamType aLine int
		@ParamType aColumn int"""
		pass

	def setSelectedPiece(self):
		pass

	def verify_blocked(self, aRemote_player):
		"""@ParamType aRemote_player Player
		@ReturnType boolean"""
		pass

	def setGamePhase(self, aPhase = "colocação"):
		"""@ParamType aPhase string"""
		pass

	def getNumOfMoinhos(self):
		"""@ReturnType int"""
		pass

	def getInterfaceChanges(self):
		"""@ReturnType tuple"""
		pass

	def getPositionsOnBoard(self):
		"""@ReturnType list"""
		pass

	def getPiecesInHand(self):
		"""@ReturnType int"""
		pass

	def getWinner(self):
		"""@ReturnType Player"""
		pass

	def checkIfMatchWasAbandoned(self):
		"""@ReturnType boolean"""
		pass

	def setAbandoned(self):
		pass

	def setDraw(self):
		pass

	def getDraw(self):
		"""@ReturnType boolean"""
		return self.___draw

	def clickedProposeDraw(self):
		pass

	def __init__(self):
		self.___total_positions = None
		"""@AttributeType int"""
		self.___occupied_positions = None
		"""@AttributeType int"""
		self.___board_design = None
		"""@AttributeType void"""
		self.___local_player = None
		"""@AttributeType Player"""
		self.___remote_player = None
		"""@AttributeType Player"""
		self.___selected_position = None
		"""@AttributeType Position"""
		self.___position_matrix = None
		"""@AttributeType Position*"""
		self.___move_type = None
		"""@AttributeType Move"""
		self.___selected_piece = None
		"""@AttributeType Piece"""
		self.___gamePhase = None
		"""@AttributeType string"""
		self.___withdrawed = None
		"""@AttributeType boolean"""
		self.___draw = None
		"""@AttributeType boolean"""
		self._unnamed_Player_ = []
		"""@AttributeType Player*
		# @AssociationType Player[]
		# @AssociationMultiplicity 2"""
		self._unnamed_InterfaceUpdater_ = None
		"""@AttributeType InterfaceUpdater
		# @AssociationType InterfaceUpdater"""
		self._unnamed_Move_ = None
		"""@AttributeType Move
		# @AssociationType Move"""
		self._unnamed_Position_ = []
		"""@AttributeType Position*
		# @AssociationType Position[]
		# @AssociationMultiplicity 32
		# @AssociationKind Composition"""
		self._unnamed_PlayerInterface_ = None
		"""@AttributeType PlayerInterface
		# @AssociationType PlayerInterface"""

