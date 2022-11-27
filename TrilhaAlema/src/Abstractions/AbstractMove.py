from abc import ABC, abstractmethod

class AbstractMove(ABC):
    @property
    @abstractmethod
    def type(self) -> None:
        pass

    @property
    @abstractmethod
    def moinhos(self) -> None:
        pass

    @property
    @abstractmethod
    def final_position(self) -> None:
        pass

    @property
    @abstractmethod
    def start_position(self) -> None:
        pass

    @property
    @abstractmethod
    def piece(self) -> None:
        pass

    @abstractmethod
    def get_move_dict(self) -> None:
        pass

    @abstractmethod
    def set_move_none(self) -> None:
        pass
