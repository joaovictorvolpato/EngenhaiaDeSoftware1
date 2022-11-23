#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Player import Player
from Position import Position
from Connection import Connection
from Move import Move
from Piece import Piece
from InterfaceUpdater import InterfaceUpdater
from PlayerInterface import PlayerInterface

class Board(object):
	def __init__(self):
		self.__total_positions = None
		self.__occupied_positions = None
		self.__board_design = None
		self.__local_player = None
		self.__remote_player = None
		self.__selected_position = None
		self.__position_matrix = None
		self.__move_type = None
		self.__selected_piece = None
		self.__gamePhase = None
		self.__withdrawed = None
		self.__draw = None
		self.__Player = []
		self.__InterfaceUpdater_ = None
		self.__Move = None
		self.__Position_ = []
		self.__PlayerInterface_ = None

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

	def set_board_position_matrix(self):
		#Instatiating the positions of the board, based on 7x7 matrix
		position_1 = Position((0, 1))
		position_2 = Position((0, 2))
		position_3 = Position((0, 3))
		position_4 = Position((1, 2))
		position_5 = Position((1, 3))
		position_6 = Position((1, 4))
		position_7 = Position((1, 6))
		position_8 = Position((2, 1))
		position_9 = Position((2, 2))
		position_10 = Position((2, 3))
		position_11 = Position((2, 4))
		position_12 = Position((2, 5))
		position_13 = Position((2, 6))
		position_14 = Position((3, 0))
		position_15 = Position((3, 1))
		position_16 = Position((3, 2))
		position_17 = Position((3, 4))
		position_18 = Position((3, 5))
		position_19 = Position((3, 6))
		position_20 = Position((4, 0))
		position_21 = Position((4, 1))
		position_22 = Position((4, 2))
		position_23 = Position((4, 3))
		position_24 = Position((4, 4))
		position_25 = Position((4, 5))
		position_26 = Position((5, 0))
		position_27 = Position((5, 2))
		position_28 = Position((5, 3))
		position_29 = Position((5, 4))
		position_30 = Position((6, 3))
		position_31 = Position((6, 4))
		position_32 = Position((6, 5))

		#Sets the neighbors of each position
		position_1.neighborhood = [position_2, position_4]
		position_2.neighborhood = [position_1, position_3, position_5]
		position_3.neighborhood = [position_2, position_6]
		position_4.neighborhood = [position_1, position_5, position_8, position_10]
		position_5.neighborhood = [position_2, position_4, position_6, position_11]
		position_6.neighborhood = [position_3, position_5, position_12]
		position_7.neighborhood = [position_12, position_13]
		position_8.neighborhood = [position_4, position_14, position_15]
		position_9.neighborhood = [position_10, position_15, position_16]
		position_10.neighborhood = [position_4, position_9, position_11]
		position_11.neighborhood = [position_5, position_10, position_17]
		position_12.neighborhood = [position_6, position_7, position_17, position_18]
		position_13.neighborhood = [position_7, position_18, position_19]
		position_14.neighborhood = [position_8, position_20]
		position_15.neighborhood = [position_8, position_9, position_20, position_21]
		position_16.neighborhood = [position_9, position_21, position_22]
		position_17.neighborhood = [position_11, position_12, position_24]
		position_18.neighborhood = [position_12, position_13, position_24, position_25]
		position_19.neighborhood = [position_13, position_25]
		position_20.neighborhood = [position_14, position_15, position_26]
		position_21.neighborhood = [position_15, position_16, position_26, position_27]
		position_22.neighborhood = [position_16, position_2, position_28]
		position_23.neighborhood = [position_22, position_24, position_29]
		position_24.neighborhood = [position_17, position_18, position_23]
		position_25.neighborhood = [position_18, position_19, position_29]
		position_26.neighborhood = [position_20, position_21]
		position_27.neighborhood = [position_21, position_28, position_30]
		position_28.neighborhood = [position_22, position_27, position_29, position_31]
		position_29.neighborhood = [position_23, position_25, position_28, position_32]
		position_30.neighborhood = [position_27, position_31]
		position_31.neighborhood = [position_28, position_30, position_32]
		position_32.neighborhood = [position_29, position_31]
  
		#Instantiating all the connections (moinhos)
		connection_1 = Connection(1, [position_1, position_2, position_3])
		connection_2 = Connection(2, [position_4, position_5, position_6])
		connection_3 = Connection(3, [position_9, position_10, position_11])
		connection_4 = Connection(4, [position_22, position_23, position_24])
		connection_5 = Connection(5, [position_27, position_28, position_29])
		connection_6 = Connection(6, [position_30, position_31, position_32])
		connection_7 = Connection(7, [position_1, position_4, position_10])
		connection_8 = Connection(8, [position_2, position_5, position_11])
		connection_9 = Connection(9, [position_3, position_6, position_12])
		connection_10 = Connection(10, [position_21, position_27, position_30])
		connection_11 = Connection(11, [position_22, position_28, position_31])
		connection_12 = Connection(12, [position_23, position_29, position_32])
		connection_13 = Connection(13, [position_4, position_8, position_14])
		connection_14 = Connection(14, [position_9, position_15, position_20])
		connection_15 = Connection(15, [position_16, position_21, position_26])
		connection_16 = Connection(16, [position_7, position_12, position_17])
		connection_17 = Connection(17, [position_13, position_18, position_24])
		connection_18 = Connection(18, [position_19, position_25, position_29])
		connection_19 = Connection(19, [position_14, position_20, position_26])
		connection_20 = Connection(20, [position_8, position_15, position_21])
		connection_21 = Connection(21, [position_9, position_16, position_22])
		connection_22 = Connection(22, [position_11, position_17, position_24])
		connection_23 = Connection(23, [position_12, position_18, position_25])
		connection_24 = Connection(24, [position_7, position_13, position_19])

		#Sets the connections of each position
		position_1.connections = [connection_1, connection_7]
		position_2.connections = [connection_1, connection_8]
		position_3.connections = [connection_1, connection_9]
		position_4.connections = [connection_2, connection_7, connection_13]
		position_5.connections = [connection_2, connection_8]
		position_6.connections = [connection_2, connection_9]
		position_7.connections = [connection_16, connection_24]
		position_8.connections = [connection_13, connection_20]
		position_9.connections = [connection_3, connection_14, connection_21]
		position_10.connections = [connection_3, connection_7]
		position_11.connections = [connection_3, connection_8, connection_22]
		position_12.connections = [connection_9, connection_16, connection_23]
		position_13.connections = [connection_17, connection_24]
		position_14.connections = [connection_13, connection_19]
		position_15.connections = [connection_14, connection_20]
		position_16.connections = [connection_15, connection_21]
		position_17.connections = [connection_16, connection_22]
		position_18.connections = [connection_17, connection_23]
		position_19.connections = [connection_18, connection_24]
		position_20.connections = [connection_14, connection_19]
		position_21.connections = [connection_10, connection_15, connection_20]
		position_22.connections = [connection_4, connection_11, connection_21]
		position_23.connections = [connection_4, connection_12]
		position_24.connections = [connection_4, connection_17, connection_22]
		position_25.connections = [connection_18, connection_23]
		position_26.connections = [connection_15, connection_19]
		position_27.connections = [connection_5, connection_10]
		position_28.connections = [connection_5, connection_11]
		position_29.connections = [connection_5, connection_12, connection_18]
		position_30.connections = [connection_6, connection_10]
		position_31.connections = [connection_6, connection_11]
		position_32.connections = [connection_6, connection_12]
  
		position_matrix = [
			[None, position_1, position_2, position_3, None, None, None],
   			[None, None, position_4, position_5, position_6, None, position_7],
			[None, position_8, position_9, position_10, position_11, position_12, position_13],
			[position_14, position_15, position_16, None, position_17, position_18, position_19],
			[position_20, position_21, position_22, position_23, position_24, position_25, None],
			[position_26, None, position_27, position_28, position_29, None, None],
			[None, None, None, position_30, position_31, position_32, None]
		]

		self.__position_matrix = position_matrix
  
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
