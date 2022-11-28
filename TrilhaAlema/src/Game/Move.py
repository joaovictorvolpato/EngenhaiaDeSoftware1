from Abstractions.AbstractPiece import AbstractPiece
from Abstractions.AbstractPosition import AbstractPosition

class Move:
	def __init__(self):
		self.__type: str = None
		self.__final_position: AbstractPosition = None
		self.__start_position: AbstractPosition = None
		self.__removed_pieces_positions_list: list[tuple[int, int]] = []
		self.__player_who_does_the_move: int = None
		self.__match_status = None

	@property
	def type(self) -> str:
		return self.__type

	@type.setter
	def type(self, move_type: str) -> None:
		self.__type = move_type

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
	def removed_pieces_positions_list(self) -> list[AbstractPosition]:
		return self.__removed_pieces_positions_list

	@removed_pieces_positions_list.setter
	def removed_pieces_positions_list(self, removed_pieces_positions_list : list[AbstractPosition]) -> None:
		self.__removed_pieces_positions_list = removed_pieces_positions_list

	@property
	def player_who_does_the_move(self) -> int:
		return self.__player_who_does_the_move

	@player_who_does_the_move.setter
	def player_who_does_the_move(self, player_who_does_the_move: int) -> None:
		self.__player_who_does_the_move = player_who_does_the_move

	def get_move_dict(self) -> dict:
		move_dict = {}
		move_dict['type'] = self.__type
	
		if self.__final_position is not None:
			move_dict['final_position'] = self.__final_position.matrix_position
		else:
			move_dict['final_position'] = (0, 0)

		if self.__start_position is not None:
			move_dict['start_position'] = self.__start_position.matrix_position
		else:
			move_dict['start_position'] = (0, 0)

		move_dict['removed_pieces_positions_list'] = self.__removed_pieces_positions_list

		move_dict['player_who_does_the_move'] = self.__player_who_does_the_move
		move_dict["match_status"] = self.__match_status

		return move_dict

	def set_move_none(self):
		self.__type = None
		self.__final_position = None
		self.__start_position = None
		self.__removed_pieces_positions_list = []
		self.__player_who_does_the_move = None
		self.__match_status = None
  
	def set_move(self, type_of_move: str, player_who_does_the_move: int,
				final_position: tuple[int, int] = None, start_position: tuple[int, int] = None,
				removed_pieces_positions_list: list[tuple[int, int]] = [], match_status: str = "next") -> None:
		self.__type = type_of_move
		self.__final_position = final_position
		self.__start_position = start_position
		self.__removed_pieces_positions_list = removed_pieces_positions_list
		self.__player_who_does_the_move = player_who_does_the_move
		self.__match_status = match_status

	@staticmethod
	def rebuild_remote_move(move_dict: dict, position_matrix: list[AbstractPosition]) -> 'Move':
		move = Move()
		move.type = move_dict['type']
		move.final_position = position_matrix[move_dict['final_position'][0]][move_dict['final_position'][1]]
		move.start_position = position_matrix[move_dict['start_position'][0]][move_dict['start_position'][1]]

		move.removed_pieces_positions = []
		for position in move_dict['removed_pieces_positions_list']:
			removed_piece_position = position_matrix[position[0]][position[1]]
			move.removed_pieces_positions.append(removed_piece_position)

		move.player_who_does_the_move = move_dict['player_who_does_the_move']
		move.__match_status = move_dict["match_status"]

		return move
