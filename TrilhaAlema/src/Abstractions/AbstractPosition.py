from abc import ABC, abstractmethod
from Abstractions.AbstractPiece import AbstractPiece
from TrilhaAlema.src.Abstractions.AbstractPlayer import AbstractPlayer


class AbstractPosition(ABC):
    @property
    @abstractmethod
    def matrix_position(self) -> None:
        pass

    @property
    @abstractmethod
    def neighborhood(self) -> None:
        pass

    @property
    @abstractmethod
    def is_occupied(self) -> None:
        pass

    @property
    @abstractmethod
    def line(self) -> int:
        pass

    @property
    @abstractmethod
    def column(self) -> None:
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
    def connections(self) -> None:
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

    @abstractmethod
    def operation(self):
        pass
