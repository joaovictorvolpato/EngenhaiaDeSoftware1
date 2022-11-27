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
    def removed_pieces_positions(self) -> None:
        pass

    @property
    @abstractmethod
    def player_who_does_the_move(self) -> None:
        pass

    @abstractmethod
    def get_move_dict(self) -> None:
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
                removed_piece_position: tuple[int, int] = None):
        pass
