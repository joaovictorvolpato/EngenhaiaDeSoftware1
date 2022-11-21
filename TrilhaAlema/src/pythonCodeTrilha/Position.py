#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Player import Player
import Piece
from Board import Board
from Move import Move
from Connection import Connection
from Position import Position

class Position():
	def __init__(self, matrix: tuple, neighborhoods: list[Position], connections: list[Connection]):
		self.__matrix_position: tuple = matrix
		self.__neighborhoods: list[Position] = neighborhoods
		self.__is_occupied: bool = False
		self.__line: int = matrix[0]
		self.__column: int = matrix[1]
		self.__player_on_pos: Player = None
		self.__piece = None
		self.__connections: list[Connection] = connections

	# START GETTERS AND SETTERS

	@property
	def matrix_position(self) -> tuple:
		return self.__matrix_position
	
	@property
	def neighborhoods(self) -> list[Position]:
		return self.__neighborhoods
	
	@property
	def is_occupied(self) -> bool:
		return self.__is_occupied
	
	@is_occupied.setter
	def is_occupied(self, occupied) -> None:
		self.__is_occupied = occupied
	
	@property
	def line(self) -> int:
		return self.__line
	
	@property
	def column(self) -> int:
		return self.__column
	
	@property
	def player_on_pos(self) -> Player:
		return self.__player_on_pos
	
	@player_on_pos.setter
	def player_on_pos(self, player: Player) -> None:
		self.__player_on_pos = player

	@property
	def piece(self) -> Piece:
		return self.__piece
	
	@piece.setter
	def piece(self, piece: Piece) -> None:
		self.__piece = piece
	
	@property
	def connections(self) -> list[Connection]:
		return self.__connections


	# END GETTERS AND SETTERS

	def place_piece(self, piece_put: Piece) -> None:
		self.__piece = piece_put
		self.set_is_occupied()
		self.set_player_on_pos(piece_put.owner_player)
		# LOGICA DE INCREMENTO E DECREMENTO FALTANDO

	def remove_piece(self) -> None:
		self.__piece = None


	def set_position_free(self) -> None:
		self.__is_occupied = False
		self.__player_on_pos = None

	def set_is_occupied(self) -> None:
		self.__is_occupied = True

	def set_player_on_pos(self, player: Player) -> None:
		self.__player_on_pos = player

	def operation(self):
		pass
