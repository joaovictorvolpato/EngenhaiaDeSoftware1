from abc import ABC, abstractmethod


class AbstractPiece(ABC):
    @property
    @abstractmethod
    def owner_player(self) -> None:
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
    def captured(self) -> None:
        pass

    @property
    @abstractmethod
    def in_moinho(self) -> None:
        pass

    @property
    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def set_piece_captured(self) -> None:
        pass
