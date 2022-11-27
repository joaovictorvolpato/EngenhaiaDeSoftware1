from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
    @property
    @abstractmethod
    def player_id(self) -> int:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def winner(self) -> bool:
        pass

    @property
    @abstractmethod
    def pieces_in_hand(self) -> int:
        pass

    @property
    @abstractmethod
    def pieces_on_board(self) -> int:
        pass

    @property
    @abstractmethod
    def removed_pieces(self) -> int:
        pass

    @property
    @abstractmethod
    def turn(self) -> bool:
        pass

    @property
    @abstractmethod
    def style(self) -> str:
        pass

    @abstractmethod
    def get_turn(self) -> bool:
        pass

    @abstractmethod
    def change_turn(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def initialize(self, id: int, name: str, style: str) -> None:
        pass

    @abstractmethod
    def select_position(self) -> None:
        pass

    @abstractmethod
    def increment_pieces_on_board(self) -> None:
        pass

    @abstractmethod
    def decrement_pieces_on_board(self) -> None:
        pass

    @abstractmethod
    def decrement_pieces_in_hand(self) -> None:
        pass

    @abstractmethod
    def increment_removed_pieces(self) -> None:
        pass

    @abstractmethod
    def can_do_fly(self) -> bool:
        pass

    @abstractmethod
    def verify_sufficient_pieces_number(self) -> bool:
        pass
