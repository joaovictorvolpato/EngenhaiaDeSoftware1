from Abstractions.AbstractPiece import AbstractPiece
from Abstractions.AbstractPosition import AbstractPosition


class Move():
	def __init__(self):
		self.__type: str = None
		self.__moinhos = 0
		self.__final_position: AbstractPosition = None
		self.__start_position: AbstractPosition = None
		self.__piece: AbstractPiece = None

	@property
	def type(self) -> str:
		return self.__type

	@type.setter
	def type(self, move_type: str) -> None:
		self.__type = move_type

	@property
	def moinhos(self) -> int:
		return self.__moinhos

	@moinhos.setter
	def moinhos(self, num_of_moinhos: int) -> None:
		self.__moinhos = num_of_moinhos

	@property
	def final_position(self) -> AbstractPosition:
		return self.__final_position

	@final_position.setter
	def final_position(self, final_position: AbstractPosition) -> None:
		self.__final_position = final_position

	@property
	def start_position(self) -> AbstractPosition:
		return self.__start_position

	@start_position.setter
	def start_position(self, start_position: AbstractPosition) -> None:
		self.__start_position = start_position

	@property
	def piece(self) -> AbstractPiece:
		return self.__piece

	@piece.setter
	def piece(self, piece : AbstractPiece) -> None:
		self.__piece = piece

	def get_move_dict(self):
		move_dict = {}
		move_dict['type'] = self.__type
		move_dict['moinhos'] = self.__moinhos
		move_dict['final_position'] = self.__final_position.__dict__()
		move_dict['start_position'] = self.__start_position.__dict__()
		move_dict['piece'] = self.__piece.__dict__()
		return move_dict

	def set_move_none(self):
		self.__type = None
		self.__moinhos = 0
		self.__final_position = None
		self.__start_position = None
		self.__piece = None
