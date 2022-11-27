from tkinter import Button
from Abstractions.AbstractBoard import AbstractBoard

class ProposeDrawButton(Button):
    def __init__(self, image, borderwidth, highlightthickness, command, relief, board:AbstractBoard) -> None:
        Button.__init__(self, image = image, borderwidth = borderwidth, highlightthickness = highlightthickness, command = command, relief = relief)
        self.__board = board

    def on_click(self) -> None:
        self.__board.propose_draw()
