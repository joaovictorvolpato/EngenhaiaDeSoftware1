#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Menu
import Board
import InterfaceUpdater
import InGameInterface
import TK
import EndInterface
import InterfaceGamaBoardSetter
import GameImageHandler
import DrawButton
import Move
import StartStatus
import DogPlayerInterface

class PlayerInterface(DogPlayerInterface):
	def __init__(self):
		self.___menu = None
		"""@AttributeType Menu"""
		self.___interface_game_board_setter = None
		"""@AttributeType InterfaceGameBoardSetter"""
		self.___window = None
		"""@AttributeType Tk"""
		self.___menubar = None
		"""@AttributeType Menu"""
		self.___menu_file = None
		"""@AttributeType Menu"""
		self._unnamed_Board_ = None
		"""@AttributeType Board
		# @AssociationType Board"""
		self._unnamed_InterfaceUpdater_ = None
		"""@AttributeType InterfaceUpdater
		# @AssociationType InterfaceUpdater"""
		self._unnamed_Menu_ = []
		"""@AttributeType Menu*
		# @AssociationType Menu[]
		# @AssociationMultiplicity 2
		# @AssociationKind Aggregation"""
		self._unnamed_InGameInterface_ = None
		"""@AttributeType InGameInterface
		# @AssociationType InGameInterface
		# @AssociationKind Aggregation"""
		self._unnamed_TK_ = None
		"""@AttributeType TK
		# @AssociationType TK
		# @AssociationKind Aggregation"""
		self._unnamed_EndInterface_ = None
		"""@AttributeType EndInterface
		# @AssociationType EndInterface
		# @AssociationKind Aggregation"""
		self._unnamed_InterfaceGamaBoardSetter_ = None
		"""@AttributeType InterfaceGamaBoardSetter
		# @AssociationType InterfaceGamaBoardSetter
		# @AssociationKind Composition"""
		self._unnamed_GameImageHandler_ = None
		"""@AttributeType GameImageHandler
		# @AssociationType GameImageHandler"""
		self._unnamed_DrawButton_ = None
		"""@AttributeType DrawButton
		# @AssociationType DrawButton
		# @AssociationKind Composition"""

	def start_game(self):
		pass

	def update_gui(self):
		pass

	def clickedProposeDraw(self):
		pass

	def sendMove(self, aMove):
		"""@ParamType aMove Move"""
		pass

	def recieve_start(self, aStart_status):
		"""@ParamType aStart_status StartStatus"""
		pass

	def notiffyMoinho(self):
		pass

	def receiveMove(self, aMove):
		"""@ParamType aMove Move"""
		pass

	def askUserIfWantsDraw(self):
		"""@ReturnType boolean"""
		pass

	def endGame(self):
		pass

	def notifyInvalidMove(self):
		pass

	def sendMove(self):
		pass

	def clickedPositionButton(self):
		pass

	def clicedDrawButton(self):
		pass

	def updateInterfaceImage(self):
		pass

