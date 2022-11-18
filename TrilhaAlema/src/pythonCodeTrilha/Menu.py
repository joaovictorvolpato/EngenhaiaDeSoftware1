#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PlayerInterface
import HowToPlay
import Settings

class Menu(object):
	def option_add(self):
		pass

	def __init__(self):
		self._unnamed_PlayerInterface_ = None
		"""@AttributeType PlayerInterface
		# @AssociationType PlayerInterface"""
		self._unnamed_HowToPlay_ = None
		"""@AttributeType HowToPlay
		# @AssociationType HowToPlay
		# @AssociationKind Aggregation"""
		self._unnamed_Settings_ = None
		"""@AttributeType Settings
		# @AssociationType Settings
		# @AssociationKind Aggregation"""

