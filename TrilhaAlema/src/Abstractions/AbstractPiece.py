from abc import ABC, abstractmethod
from Abstractions.AbstractPlayer import AbstractPlayer
from Abstractions.AbstractMove import AbstractMove


class AbstractPiece(ABC):
    @property
    @abstractmethod
    def owner_player(self) -> AbstractPlayer:
        pass

    @property
    @abstractmethod
    def styles(self):
        pass

    @property
    @abstractmethod
    def position(self) -> None: 
        pass

    @property
    @abstractmethod
    def captured(self) -> bool:
        pass

    @property
    @abstractmethod
    def in_moinho(self) -> bool:
        pass

    @property
    @abstractmethod
    def move(self) -> AbstractMove:
        pass

    @abstractmethod
    def set_piece_captured(self) -> None:
        pass
