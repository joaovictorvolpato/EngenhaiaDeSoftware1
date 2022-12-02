from abc import ABC, abstractmethod
from Abstractions.AbstractPosition import AbstractPosition
from Abstractions.AbstractPlayer import AbstractPlayer


class AbstractMove(ABC):
    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def moinhos(self) -> int:
        pass

    @property
    @abstractmethod
    def final_position(self) -> AbstractPosition:
        pass

    @property
    @abstractmethod
    def start_position(self) -> AbstractPosition:
        pass

    @property
    @abstractmethod
    def removed_pieces_positions(self) -> list:
        pass

    @property
    @abstractmethod
    def player_who_does_the_move(self) -> AbstractPlayer:
        pass

    @abstractmethod
    def get_move_dict(self) -> dict:
        pass

    @abstractmethod
    def set_move_none(self) -> None:
        pass

    @abstractmethod
    def set_move(self, type_of_move: str,
                player_who_does_the_move: int,
                moinhos: int = 0,
                final_position: tuple[int, int] = None,
				start_position: tuple[int, int] = None,
                removed_piece_position: tuple[int, int] = None) -> None:
        pass

    @staticmethod
    @abstractmethod
    def rebuild_remote_move(self, move_dict: dict) -> None:
        pass
