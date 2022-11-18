#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PhotoImage
import InterfaceGamaBoardSetter
import GameImageHandler
import Button

class PieceSwitch(Button):
	def __init__(self):
		self.___button_image = None
		"""@AttributeType PhotoImage"""
		self.___button_pressed = None
		"""@AttributeType Boolean"""
		self._unnamed_InterfaceGamaBoardSetter_ = None
		"""@AttributeType InterfaceGamaBoardSetter
		# @AssociationType InterfaceGamaBoardSetter"""
		self._unnamed_GameImageHandler_ = None
		"""@AttributeType GameImageHandler
		# @AssociationType GameImageHandler"""
		self._unnamed_PhotoImage_ = None
		"""@AttributeType PhotoImage
		# @AssociationType PhotoImage
		# @AssociationKind Aggregation"""

