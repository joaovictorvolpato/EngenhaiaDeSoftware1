from abc import ABC, abstractmethod

class AbstractBoard(ABC):
    @property
    @abstractmethod
    def player_interface(self) -> None:
        pass
	
    @property
    @abstractmethod
    def interface_updater(self) -> None:
        pass
	
    @property
    @abstractmethod
    def position_matrix(self) -> None:
        pass
	
    @property
    @abstractmethod
    def occupied_positions(self) -> None:
        pass

    @property
    @abstractmethod
    def total_positions(self) -> int:
        pass

    @property
    @abstractmethod
    def selected_position(self) -> None:
        pass

    @property
    @abstractmethod
    def selected_piece(self) -> None:
        pass

    @property
    @abstractmethod
    def local_player(self) -> None:
        pass

    @property
    @abstractmethod
    def remote_player(self) -> None:
        pass

    @property
    @abstractmethod
    def draw(self) -> None:
        pass

    @property
    @abstractmethod
    def withdrawed(self) -> None:
        pass

    @property
    @abstractmethod
    def game_phase(self) -> None:
        pass

    @property
    @abstractmethod
    def move_type(self) -> None:
        pass

    @property
    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def set_board_position_matrix(self) -> None:
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
    def execute_place_piece(self, piece_put: Piece) -> None:
        pass

    @abstractmethod
    def execute_move_piece(self) -> None:
        pass

    @abstractmethod
    def execute_remove_piece(self, position_to_remove_piece: Position, player_who_removed_piece: Player) -> None:
        pass

    @abstractmethod
    def notify_player_to_remove_piece(number_of_moinhos: int) -> None:
        pass

    @abstractmethod
    def evaluate_moinho(self) -> None:
        pass

    @abstractmethod
    def get_num_of_moinhos(self, selected_position: Position) -> None:
        pass

    @abstractmethod
    def propose_draw(self) -> None:
        pass

    @abstractmethod
    def start_match(self, local_player: Player, remote_player: Player, local_player_id: int) -> None:
        pass

    @abstractmethod
    def execute_move(self, move) -> None:
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
    def clicked_position(self, line:int, column:int) -> None:
        pass

    @abstractmethod
    def get_interface_changes(self) -> None:
        pass

    @abstractmethod
    def check_if_match_was_abandoned(self) -> None:
        pass

    @abstractmethod
    def set_abandoned(self) -> None:
        pass

    @abstractmethod
    def clicked_propose_draw(self) -> None:
        pass

    @abstractmethod
    def set_winner(self, winner_player: Player) -> None:
        pass

    @abstractmethod
    def verify_blocked(self, player: Player) -> None:
        pass

    @abstractmethod
    def evaluate_winner(self) -> None:
        pass
