#!/usr/bin/python
# -*- coding: UTF-8 -*-
import DogActor
import StartStatus

class DogPlayerInterface(object):
	def __init__(self):
		self._dog_server_interface = None
		"""@AttributeType DogActor"""
		self._unnamed_StartStatus_ = None
		"""@AttributeType StartStatus
		# @AssociationType StartStatus"""
		self._unnamed_DogActor_ = None
		"""@AttributeType DogActor
		# @AssociationType DogActor"""

