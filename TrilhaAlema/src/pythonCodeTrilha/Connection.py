#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Position

class Connection(object):
	def getId(self):
		pass

	def getPositionsList(self):
		pass

	def getIsMoinho(self):
		"""@ReturnType boolean"""
		pass

	def setIsMoinho(self, aIs_moinho):
		"""@ParamType aIs_moinho boolean
		@ReturnType void"""
		pass

	def __init__(self):
		self.___id = None
		"""@AttributeType int"""
		self.___positions_list = None
		"""@AttributeType list"""
		self.___is_moinho = None
		"""@AttributeType boolean"""
		self._unnamed_Position_ = None
		"""@AttributeType Position
		# @AssociationType Position
		# @AssociationKind Composition"""

