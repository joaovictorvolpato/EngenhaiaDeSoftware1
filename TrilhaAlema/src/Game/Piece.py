from Abstractions.AbstractMove import AbstractMove
from Abstractions.AbstractPlayer import AbstractPlayer
from Abstractions.AbstractPosition import AbstractPosition

class Piece():
	def __init__(self, owner_player: AbstractPlayer, position: AbstractPosition) -> None:
		self.__owner_player: AbstractPlayer = owner_player
		self.__style = self.__owner_player.style
		self.__position: AbstractPosition = position
		self.__captured: bool = False
		self.__in_moinho: bool = False
		self.__move: AbstractMove = None

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
	def in_moinho(self, in_moinho: bool):
		self.__in_moinho = in_moinho

	def set_in_moinho_when_piece_changes_pos(self, moinho: bool, player: AbstractPlayer = None) -> None:
		print("IN CLASSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
		print(self.__position)
		print(self.__position.connections)
		print("IN CLASSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")

		if not moinho:
			self.__in_moinho = False
			owner_player = self.__owner_player
			self.__owner_player = 0
			for connection in self.__position.connections:
				for position in connection.positions_list:
					if position.get_num_of_moinhos_is_in() == 0:
						position.piece.in_moinho = False
					else:
						connection.set_positions_in_moinho(True)
			self.__owner_player = owner_player

		elif moinho and player != None:
			for connection in self.__position.connections:
				_is_moinho = connection.is_moinho(player)
				if _is_moinho:
					connection.set_positions_in_moinho(True)

	@property
	def move(self) -> AbstractMove:
		return self.__move

	@move.setter
	def move(self, new_move: AbstractMove):
		self.__move = new_move

	def set_piece_captured(self) -> None:
		self.__captured = True
