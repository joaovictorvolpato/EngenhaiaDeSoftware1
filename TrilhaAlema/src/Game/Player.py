
class Player:
	def __init__(self, id: int, name: str, turn: bool, team: str) -> None:
		self.__player_id: int = id
		self.__name: str = name
		self.__winner: bool = False
		self.__pieces_in_hand: int = 12
		self.__pieces_on_board: int = 0
		self.__removed_pieces: int = 0
		self.__turn: bool = turn
		self.team: str = team

	@property
	def player_id(self) -> int:
		return self.__player_id

	@player_id.setter
	def player_id(self, id: int) -> None:
		self.__player_id = id

	@property
	def name(self) -> str:
		return self.__name

	@name.setter
	def name(self, new_name: str) -> None:
		self.__name = new_name

	@property
	def winner(self) -> bool:
		return self.__winner

	@winner.setter
	def winner(self, is_winner: bool) -> None:
		self.__winner = is_winner

	@property
	def pieces_in_hand(self) -> int:
		return self.__pieces_in_hand
	
	@pieces_in_hand.setter
	def pieces_in_hand(self, pieces_number: int) -> None:
		self.__pieces_in_hand = pieces_number
	
	@property
	def pieces_on_board(self) -> int:
		return self.__pieces_on_board
	
	@pieces_on_board.setter
	def pieces_on_board(self, pieces_number: int) -> None:
		self.__pieces_on_board = pieces_number

	@property
	def removed_pieces(self) -> int:
		return self.__removed_pieces

	@removed_pieces.setter
	def removed_pieces(self, pieces_removed_number: int) -> None:
		self.__removed_pieces = pieces_removed_number
	
	@property
	def turn(self) -> bool:
		return self.__turn

	@turn.setter
	def turn(self, new_turn) -> None:
		self.__turn = new_turn

	@property
	def style(self) -> str:
		return self.team

	def change_turn(self) -> None:
		self.__turn = not self.__turn

	def reset(self) -> None:
		self.__player_id: int = None
		self.__name: str = None
		self.__winner: bool = None
		self.__pieces_in_hand: int = None
		self.__pieces_on_board: int = None
		self.__removed_pieces: int = None
		self.__turn: bool = None
		self.team: str = None

	def initialize(self, id: int, name: str, style: str) -> None:
		self.__init__(self, id, name, style)

	def increment_pieces_on_board(self) -> None:
		self.__pieces_on_board += 1

	def decrement_pieces_on_board(self) -> None:
		self.__pieces_on_board -= 1

	def decrement_pieces_in_hand(self) -> None: # Alterar modelagem
		self.__pieces_in_hand -= 1

	def increment_removed_pieces(self) -> None:
		self.__removed_pieces += 1

	def can_do_fly(self) -> bool:
		pieces_number = self.__pieces_on_board
		return (pieces_number == 3)

	def verify_sufficient_pieces_number(self) -> bool:
		pieces_number = self.__pieces_on_board + self.__pieces_in_hand
		if pieces_number <= 2:
			print('WIN BY INSUFFICIENTE PIECES.')
		return (pieces_number > 2)
