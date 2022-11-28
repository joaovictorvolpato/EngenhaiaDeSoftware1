from abc import ABC, abstractmethod
from Abstractions.AbstractPiece import AbstractPiece
from Abstractions.AbstractPlayer import AbstractPlayer
from Abstractions.AbstractPosition import AbstractPosition
from Abstractions.AbstractMove import AbstractMove
from Abstractions.AbstractPlayerInterface import AbstractPlayerInterface
from Abstractions.AbstractInterfaceUpdater import AbstractInterfaceUpdater


class AbstractBoard(ABC):
    @property
    @abstractmethod
    def player_interface(self) -> AbstractPlayerInterface:
        pass
	
    @property
    @abstractmethod
    def interface_updater(self) -> AbstractInterfaceUpdater:
        pass
	
    @property
    @abstractmethod
    def position_matrix(self) -> list:
        pass
	
    @property
    @abstractmethod
    def occupied_positions(self) -> list[AbstractPosition]:
        pass

    @property
    @abstractmethod
    def total_positions(self) -> int:
        pass

    @property
    @abstractmethod
    def selected_position(self) -> AbstractPosition:
        pass

    @property
    @abstractmethod
    def selected_piece(self) -> AbstractPiece:
        pass

    @property
    @abstractmethod
    def local_player(self) -> AbstractPlayer:
        pass

    @property
    @abstractmethod
    def remote_player(self) -> AbstractPlayer:
        pass

    @property
    @abstractmethod
    def draw(self) -> bool:
        pass

    @property
    @abstractmethod
    def game_phase(self) -> str:
        pass

    @property
    @abstractmethod
    def move(self) -> AbstractMove:
        pass

    @abstractmethod
    def set_board_position_matrix(self) -> list:
        pass

    @abstractmethod
    def verify_occupied_positions_in_matrix(self) -> list:
        pass

    @abstractmethod
    def get_interface_changes(self) -> tuple[list, int, int, int, int]:
        pass

    @abstractmethod
    def place_piece(self) -> None:
        pass

    @abstractmethod
    def move_piece(self) -> None:
        pass
    @abstractmethod
    def remove_piece(self) -> None:
        pass

    @abstractmethod
    def execute_place_piece(self, piece_put: AbstractPiece) -> None:
        pass

    @abstractmethod
    def execute_move_piece(self) -> None:
        pass

    @abstractmethod
    def execute_remove_piece(self, position_to_remove_piece: AbstractPosition, player_who_removed_piece: AbstractPlayer) -> None:
        pass

    @abstractmethod
    def notify_player_to_remove_piece(number_of_moinhos: int) -> None:
        pass

    @abstractmethod
    def evaluate_moinho(self) -> None:
        pass

    @abstractmethod
    def get_num_of_moinhos(self, selected_position: AbstractPosition) -> int:
        pass

    @abstractmethod
    def propose_draw(self) -> None:
        pass

    @abstractmethod
    def start_match(self, local_player: AbstractPlayer, remote_player: AbstractPlayer, local_player_id: int) -> None:
        pass

    @abstractmethod
    def execute_received_move(self, move) -> None:
        pass

    @abstractmethod
    def end_game(self) -> None:
        pass

    @abstractmethod
    def restart_move(self) -> None:
        pass

    @abstractmethod
    def register_invalid_move(self) -> None:
        pass

    @abstractmethod
    def notify_player_not_turn(self) -> None:
        pass

    @abstractmethod
    def receive_withdrawal_notification(self) -> None:
        pass

    @abstractmethod
    def finish_turn(self) -> None:
        pass

    @abstractmethod
    def reset_match(self) -> None:
        pass

    @abstractmethod    
    def clicked_position(self, line: int, column: int) -> None:
        pass

    @abstractmethod
    def get_interface_changes(self) -> None:
        pass

    @abstractmethod
    def clicked_propose_draw(self) -> None:
        pass

    @abstractmethod
    def set_winner(self, winner_player: AbstractPlayer) -> None:
        pass

    @abstractmethod
    def verify_blocked(self, player: AbstractPlayer) -> bool:
        pass

    @abstractmethod
    def evaluate_winner(self) -> None:
        pass
