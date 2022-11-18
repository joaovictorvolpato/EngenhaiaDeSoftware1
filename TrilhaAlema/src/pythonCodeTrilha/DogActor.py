#!/usr/bin/python
# -*- coding: UTF-8 -*-
import StartStatus
import DogPlayerInterface

class DogActor(object):
	def initialize(self, aPlayer_name, aPlayer_actor):
		"""@ParamType aPlayer_name string
		@ParamType aPlayer_actor DogPlayerInterface"""
		pass

	def start_match(self, aNumber_of_players = 2):
		"""@ParamType aNumber_of_players int"""
		pass

	def send_move(self, aMove_to_send):
		"""@ParamType aMove_to_send Dictionary"""
		pass

	def __init__(self):
		self._unnamed_StartStatus_ = None
		"""@AttributeType StartStatus
		# @AssociationType StartStatus"""
		self._unnamed_DogPlayerInterface_ = None
		"""@AttributeType DogPlayerInterface
		# @AssociationType DogPlayerInterface"""

