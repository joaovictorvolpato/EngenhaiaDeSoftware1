from Abstractions.AbstractPosition import AbstractPosition


class Connection():
	def __init__(self, id: int, positions: list[AbstractPosition]):
		self.__id = id
		self.__positions_list = positions
		self.__is_moinho = False

	@property
	def id(self) -> int:
		return self.__id

	@property
	def positions_list(self) -> list[AbstractPosition]:
		return self.__positions_list

	@property
	def is_moinho(self) -> bool:
		return self.__is_moinho

	@is_moinho.setter
	def is_moinho(self, moinho: bool) -> None:
		self.__is_moinho = moinho

	def set_is_moinho(self) -> None:
		self.__is_moinho = True
	
	def set_is_not_moinho(self) -> None:
		self.__is_moinho = False
