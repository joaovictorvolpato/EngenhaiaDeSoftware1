from tkinter import Button, PhotoImage
from Interface.GameImageHandler import GameImageHandler
from Game.Board import Board

class PieceSwitch(Button):
    id_to_position: list[tuple] = [
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
        self.button_pressed:bool = False
        self.id = id

    def on_click(self) -> None:
        print(self.id)
        if not self.button_pressed:
            self.configure(image = GameImageHandler.VASCO_piece_image)
            self.toggle_switch()

        else:
            self.configure(image = GameImageHandler.button_image)
            self.toggle_switch()

    def toggle_switch(self) -> bool:
        self.button_pressed = not self.button_pressed

    def get_position_in_position_matrix_from_id(self, id: int) -> tuple:
        return self.id_to_position[id]
