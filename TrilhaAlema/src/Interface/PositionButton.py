from tkinter import Button, PhotoImage
from Interface.GameImageHandler import GameImageHandler
from Game.Board import Board

class PositionButton(Button):
    id_to_position: list[tuple] = [
        (0, 0),
        (0, 1),(0, 2),(0, 3),
        (1, 2),(1, 3),(1, 4),(1, 6),
	    (2, 1),(2, 2),(2, 3),(2, 4),(2, 5),(2, 6),
	    (3, 0),(3, 1),(3, 2),(3, 4),(3, 5),(3, 6),
	    (4, 0),(4, 1),(4, 2),(4, 3),(4, 4),(4, 5),
	    (5, 0),(5, 2),(5, 3),(5, 4),
	    (6, 3),(6, 4),(6, 5)   
    ]

    def __init__(self, id:int, image:PhotoImage, borderwidth:int, highlightthickness:int, command, relief:str, board:Board) -> None:
        Button.__init__(self, image = image, borderwidth = borderwidth, highlightthickness = highlightthickness, command = command, relief = relief)
        self.button_image = GameImageHandler.button_image
        self.__id: int = id
        self.__team_on_position: str = ""
        self.__board: Board = board

    @property
    def id(self) -> int:
        return self.__id

    @property
    def team_on_position(self) -> str:
        return self.__team_on_position

    @team_on_position.setter
    def team_on_position(self, team: str) -> None:
        self.__team_on_position = team

    @property
    def board(self) -> Board:
        return self.__board

    def on_click(self) -> None:
        line, column = self.get_position_in_position_matrix_from_id(self.id)
        self.board.clicked_position(line, column)

    def draw_piece_on_position(self, team: str) -> None:
        if team == "VASCO":
            self.config(image = GameImageHandler.VASCO_piece_image)
        elif team == "AVAI":
            self.config(image = GameImageHandler.AVAI_piece_image)

        self.team_on_position = team

    def erase_piece_from_position(self) -> None:
        self.configure(image = self.button_image)

    def get_position_in_position_matrix_from_id(self, id: int) -> tuple:
        return self.id_to_position[id]
