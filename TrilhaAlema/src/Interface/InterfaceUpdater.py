# from Game.Position import Position
# from Game.Piece import Piece
from Abstractions.AbstractBoard import AbstractBoard
from Abstractions.AbstractPlayerInterface import AbstractPlayerInterface 
from Interface.PositionButton import PositionButton

class InterfaceUpdater:
	@staticmethod
	def update_interface_image(player_interface: AbstractPlayerInterface):
		board = player_interface.board
    
		(positions_to_update, pieces_in_local_player_hand_to_uptdade, pieces_in_remote_player_hand_to_update, 
   		pieces_that_local_player_captured, pieces_that_remote_player_captured) = board.get_interface_changes(board)

		InterfaceUpdater.display_pieces_on_positions(player_interface, positions_to_update)
		InterfaceUpdater.display_pieces_in_local_player_hand(player_interface, pieces_in_local_player_hand_to_uptdade)
		InterfaceUpdater.display_pieces_in_remote_player_hand(player_interface, pieces_in_remote_player_hand_to_update)
		InterfaceUpdater.display_local_player_captured_pieces(player_interface, pieces_that_local_player_captured)
		InterfaceUpdater.display_remote_player_captured_pieces(player_interface, pieces_that_remote_player_captured)
		InterfaceUpdater.change_is_turn_message_to_local_player(player_interface, board.local_player.turn)
		InterfaceUpdater.change_game_phase_message(player_interface)

	@staticmethod
	def display_pieces_on_positions(player_interface: AbstractPlayerInterface, positions_to_update: list[tuple[bool, int]]):
		positions_buttons_list = player_interface.interface_game_board.position_buttons_list
		for position_index, position in enumerate(positions_to_update):
			occupied, owner_id = position
			if occupied:
				position_id = position_index + 1
				position_button = positions_buttons_list[position_id]
				

	@staticmethod
	def display_pieces_in_local_player_hand(player_interface: AbstractPlayerInterface, pieces_in_local_player_hand: int):
		board_canvas = player_interface.interface_game_board.canvas
		board_canvas.local_player_pieces_in_hand = pieces_in_local_player_hand

	@staticmethod
	def display_pieces_in_remote_player_hand(player_interface: AbstractPlayerInterface, pieces_in_remote_player_hand: int):
		board_canvas = player_interface.interface_game_board.canvas
		board_canvas.remote_player_pieces_in_hand = pieces_in_remote_player_hand

	@staticmethod
	def display_local_player_captured_pieces(player_interface: AbstractPlayerInterface, local_player_captured_pieces: int):
		board_canvas = player_interface.interface_game_board.canvas
		board_canvas.local_player_captured_pieces = local_player_captured_pieces

	@staticmethod
	def display_remote_player_captured_pieces(player_interface: AbstractPlayerInterface, remote_player_captured_pieces: int):
		board_canvas = player_interface.interface_game_board.canvas
		board_canvas.remote_player_captured_pieces = remote_player_captured_pieces

	@staticmethod
	def change_is_turn_message_to_local_player(player_interface: AbstractPlayerInterface, is_local_player_turn: bool):
		board_canvas = player_interface.interface_game_board.canvas
		if is_local_player_turn:
			board_canvas.is_turn_text = "It's your turn!"
		else:
			board_canvas.is_turn_text = "It's not your turn!"

	@staticmethod
	def change_game_phase_message(player_interface: AbstractPlayerInterface):
		board_canvas = player_interface.interface_game_board.canvas
		game_phase = player_interface.board.game_phase

		if game_phase == "placing":
			board_canvas.game_phase_text = "Place your pieces on the board!"
		elif game_phase == "moving":
			board_canvas.game_phase_text = "Move your pieces across the board!"
