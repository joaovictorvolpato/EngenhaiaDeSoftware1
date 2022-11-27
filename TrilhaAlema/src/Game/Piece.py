from Abstractions.AbstractMove import AbstractMove
from Abstractions.AbstractPlayer import AbstractPlayer
from Abstractions.AbstractPosition import AbstractPosition


class Piece():
	def __init__(self, owner_player: AbstractPlayer):
		self.__owner_player: AbstractPlayer = owner_player
		self.__style = self.__owner_player.style
		self.__position: AbstractPosition = None
		self.__captured: bool = False
		self.__in_moinho: bool = False
		self.__move: AbstractMove = None

	# GETTERS AND SETTERS
	@property
	def owner_player(self) -> AbstractPlayer:
		return self.__owner_player

	@property
	def styles(self) -> str:
		return self.__style

	@property
	def position(self) -> AbstractPosition: 
		return self.__position

	@position.setter
	def position(self, new_position: AbstractPosition):
		self.__position = new_position

	@property
	def captured(self) -> bool:
		return self.__captured

	@captured.setter
	def captured(self, captured: bool):
		self.__captured = captured

	@property
	def in_moinho(self) -> bool:
		return self.__in_moinho

	@in_moinho.setter
	def in_moinho(self, in_moinho_value: bool):
		self.__in_moinho = in_moinho_value

	@property
	def move(self) -> AbstractMove:
		return self.__move

	@move.setter
	def move(self, new_move: AbstractMove):
		self.__move = new_move

	def set_piece_captured(self) -> None:
		self.__captured = True
