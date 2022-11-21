#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Player import Player
import Position
import Move
import Piece
import InterfaceUpdater
import PlayerInterface

class Board(object):
	def __init__(self):
		self.__total_positions = None
		"""@AttributeType int"""
		self.__occupied_positions = None
		"""@AttributeType int"""
		self.__board_design = None
		"""@AttributeType void"""
		self.__local_player = None
		"""@AttributeType Player"""
		self.__remote_player = None
		"""@AttributeType Player"""
		self.__selected_position = None
		"""@AttributeType Position"""
		self.__position_matrix = None
		"""@AttributeType Position*"""
		self.__move_type = None
		"""@AttributeType Move"""
		self.__selected_piece = None
		"""@AttributeType Piece"""
		self.__gamePhase = None
		"""@AttributeType string"""
		self.__withdrawed = None
		"""@AttributeType boolean"""
		self.__draw = None
		"""@AttributeType boolean"""
		self.__Player = []
		"""@AttributeType Player*
		# @AssociationType Player[]
		# @AssociationMultiplicity 2"""
		self.__InterfaceUpdater_ = None
		"""@AttributeType InterfaceUpdater
		# @AssociationType InterfaceUpdater"""
		self.__Move = None
		"""@AttributeType Move
		# @AssociationType Move"""
		self.__Position_ = []
		"""@AttributeType Position*
		# @AssociationType Position[]
		# @AssociationMultiplicity 32
		# @AssociationKind Composition"""
		self.__PlayerInterface_ = None
		"""@AttributeType PlayerInterface
		# @AssociationType PlayerInterface"""

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

	def executeMove(self, aMove):
		"""@ParamType aMove Move"""
		pass

	def endGame(self):
		pass

	def restartMove(self):
		pass

	def setBoardPositionMatrix(self):
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

	@property
	def Game_phase(self) -> str:
		return self.__gamePhase

	@Game_phase.setter
	def Game_phase(self, phase : str):
		self.__gamePhase = phase

			
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
		return self.__draw

	def clickedProposeDraw(self):
		pass



