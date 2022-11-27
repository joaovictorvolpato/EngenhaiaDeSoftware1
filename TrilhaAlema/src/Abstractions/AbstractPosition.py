from abc import ABC, abstractmethod
from Abstractions.AbstractPiece import AbstractPiece
from Abstractions.AbstractPlayer import AbstractPlayer
from TrilhaAlema.src.Abstractions.AbstractPlayer import AbstractPlayer


class AbstractPosition(ABC):
    @property
    @abstractmethod
    def matrix_position(self) -> tuple:
        pass

    @property
    @abstractmethod
    def neighborhood(self) -> list:
        pass

    @property
    @abstractmethod
    def is_occupied(self) -> bool:
        pass

    @property
    @abstractmethod
    def line(self) -> int:
        pass

    @property
    @abstractmethod
    def column(self) -> int:
        pass

    @property
    @abstractmethod
    def player_on_pos(self) -> AbstractPlayer:
        pass

    @property
    @abstractmethod
    def piece(self) -> AbstractPiece:
        pass

    @property
    @abstractmethod
    def connections(self) -> list:
        pass

    @abstractmethod
    def place_piece(self, piece_put: AbstractPiece) -> None:
        pass

    @abstractmethod
    def remove_piece(self) -> None:
        pass

    @abstractmethod
    def set_position_free(self) -> None:
        pass

    @abstractmethod
    def set_is_occupied(self) -> None:
        pass
