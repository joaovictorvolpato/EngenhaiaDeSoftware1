# from Game.Position import Position
# from Game.Piece import Piece
# from Game.Board import Board
from Interface.PlayerInterface import PlayerInterface
# from Game.Player import Player

class InterfaceUpdater:
	def update_interface_image(self, player_interface: PlayerInterface):
		pass

	def display_pieces_on_positions(self, aPlayer_interface, aPositions_to_update):
		pass

	def display_pieces_in_local_player_hand(self, aPlayer_interface, aPieces_in_local_player_hand):
		pass

	def display_pieces_in_remote_player_hand(self, aPlayer_interface, aPieces_in_remote_player_hand):
		pass

	def display_local_player_captured_pieces(self, aPlayer_interface, aLocal_player_captured_pieces):
		pass

	def change_is_turn_message_to_local_player(self, aPlayer_interface):
		pass
