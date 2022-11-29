from Abstractions.AbstractConnection import AbstractConnection
from Abstractions.AbstractPiece import AbstractPiece
from Abstractions.AbstractPlayer import AbstractPlayer
from Abstractions.AbstractPosition import AbstractPosition


class Position:
	def __init__(self, matrix: tuple, neighborhood: list[AbstractPosition] = [], connections: list[AbstractConnection] = []):
		self.__matrix_position: tuple = matrix
		self.__neighborhood: list[AbstractPosition] = neighborhood
		self.__is_occupied: bool = False
		self.__line: int = matrix[0]
		self.__column: int = matrix[1]
		self.__player_on_pos: AbstractPlayer = None
		self.__piece: AbstractPiece = None
		self.__connections: list[AbstractConnection] = connections

	@property
	def matrix_position(self) -> tuple:
		return self.__matrix_position
	
	@property
	def neighborhood(self) -> list[AbstractPosition]:
		return self.__neighborhood

	@neighborhood.setter
	def neighborhood(self, neighborhood: list[AbstractPosition]) -> None:
		self.__neighborhood = neighborhood
	
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
	def player_on_pos(self) -> AbstractPlayer:
		return self.__player_on_pos
	
	@player_on_pos.setter
	def player_on_pos(self, player: AbstractPlayer) -> None:
		self.__player_on_pos = player

	@property
	def piece(self) -> AbstractPiece:
		return self.__piece
	
	@piece.setter
	def piece(self, piece: AbstractPiece) -> None:
		self.__piece = piece

	@property
	def connections(self) -> list[AbstractConnection]:
		return self.__connections

	@connections.setter
	def connections(self, connections: list[AbstractConnection]) -> None:
		self.__connections = connections

	def place_piece(self, piece_put: AbstractPiece) -> None: # Arrumar parametros na modelagem
		self.__piece = piece_put
		self.set_is_occupied()
		self.__player_on_pos = piece_put.owner_player

	def remove_piece(self) -> None:
		self.set_position_free()
		self.__piece = None
		self.__player_on_pos = None

	def set_position_free(self) -> None:
		self.__is_occupied = False

	def set_is_occupied(self) -> None:
		self.__is_occupied = True

	def get_num_of_moinhos_is_in(self) -> int:
		position_connections: list[AbstractConnection] = self.connections
		player_on_selected_position: AbstractPlayer = self.player_on_pos

		moinhos_count = 0
		for connection in position_connections:
			is_moinho = connection.is_moinho(player_on_selected_position)
			if is_moinho:
				#connection.is_moinho = True
				moinhos_count += 1

		return moinhos_count
