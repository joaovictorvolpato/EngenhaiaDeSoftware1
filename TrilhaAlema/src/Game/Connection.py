from Abstractions.AbstractPosition import AbstractPosition
from Abstractions.AbstractPlayer import AbstractPlayer

class Connection():
	def __init__(self, id: int, positions: list[AbstractPosition]):
		self.__id = id
		self.__positions_list = positions

	@property
	def id(self) -> int:
		return self.__id

	@property
	def positions_list(self) -> list[AbstractPosition]:
		return self.__positions_list

	def is_moinho(self, player: AbstractPlayer):
		pieces_owned_by_player = 0
		for position in self.__positions_list:
			if position.player_on_pos == player:
				pieces_owned_by_player += 1

		moinho_occured = pieces_owned_by_player == 3

		return moinho_occured

	def set_positions_in_moinho(self, moinho: bool) -> None:
		for position in self.__positions_list:
			position.piece.in_moinho = moinho
