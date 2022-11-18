#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DogPlayerInterface
import DogActor

class StartStatus(object):
	def get_code(self):
		"""@ReturnType string"""
		pass

	def get_message(self):
		"""@ReturnType string"""
		pass

	def get_local_id(self):
		"""@ReturnType string"""
		pass

	def get_players(self):
		"""@ReturnType string*"""
		pass

	def __init__(self):
		self._unnamed_DogPlayerInterface_ = None
		"""@AttributeType DogPlayerInterface
		# @AssociationType DogPlayerInterface"""
		self._unnamed_DogActor_ = None
		"""@AttributeType DogActor
		# @AssociationType DogActor"""

