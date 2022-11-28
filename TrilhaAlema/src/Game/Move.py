from Abstractions.AbstractPiece import AbstractPiece
from Abstractions.AbstractPosition import AbstractPosition


class Move:
	def __init__(self):
		self.__type: str = None
		self.__moinhos = 0
		self.__final_position: AbstractPosition = None
		self.__start_position: AbstractPosition = None
		self.__removed_pieces_positions: list[tuple[int, int]] = []
		self.__player_who_does_the_move: int = None

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
	def final_position(self) -> tuple[int, int]:
		return self.__final_position

	@final_position.setter
	def final_position(self, final_position: tuple[int, int]) -> None:
		self.__final_position = final_position

	@property
	def start_position(self) -> tuple[int, int]:
		return self.__start_position

	@start_position.setter
	def start_position(self, start_position: tuple[int, int]) -> None:
		self.__start_position = start_position

	@property
	def removed_pieces_positions(self) -> list[tuple[int, int]]:
		return self.__removed_pieces_positions

	@removed_pieces_positions.setter
	def removed_pieces_positions(self, positions : list[tuple[int, int]]) -> None:
		self.__removed_pieces_positions = positions

	@property
	def player_who_does_the_move(self) -> int:
		return self.__player_who_does_the_move

	def get_move_dict(self) -> dict:
		move_dict = {}
		move_dict['type'] = self.__type
		move_dict['moinhos'] = self.__moinhos
		move_dict['final_position'] = self.__final_position.matrix_position
		move_dict['start_position'] = self.__start_position.matrix_position
		move_dict['removed_pieces_positions_list'] = [position.matrix_position for position in self.__removed_pieces_positions]
		move_dict['player_who_does_the_move'] = self.__player_who_does_the_move

		return move_dict

	def set_move_none(self):
		self.__type = None
		self.__moinhos = None
		self.__final_position = None
		self.__start_position = None
		self.__removed_pieces_positions = []
		self.__player_who_does_the_move = None

	def set_move(self, type_of_move: str, player_who_does_the_move: int, moinhos: int = 0,
				final_position: tuple[int, int] = None, start_position: tuple[int, int] = None,
				removed_piece_position: tuple[int, int] = None):
		self.__type = type_of_move
		self.__moinhos = moinhos
		self.__final_position = final_position
		self.__start_position = start_position
		self.__removed_pieces_positions.append(removed_piece_position)
		self.__player_who_does_the_move = player_who_does_the_move
