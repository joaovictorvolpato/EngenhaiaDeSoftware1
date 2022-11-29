from abc import ABC, abstractmethod


class AbstractConnection(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @property
    @abstractmethod
    def positions_list(self) -> list:
        pass

    @abstractmethod
    def set_is_moinho(self) -> None:
        pass
    @abstractmethod
    def set_is_not_moinho(self) -> None:
        pass
