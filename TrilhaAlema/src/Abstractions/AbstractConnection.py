from abc import ABC, abstractmethod


class AbstractConnection(ABC):
    @property
    @abstractmethod
    def id(self) -> None:
        pass

    @property
    @abstractmethod
    def positions_list(self) -> None:
        pass

    @property
    @abstractmethod
    def is_moinho(self) -> None:
        pass

    @abstractmethod
    def set_is_moinho(self) -> None:
        pass
    @abstractmethod
    def set_is_not_moinho(self) -> None:
        pass
