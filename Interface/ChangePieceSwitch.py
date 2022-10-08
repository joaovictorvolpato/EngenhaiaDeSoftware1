from tkinter import Button
from GameImageHandler import GameImageHandler

class ChangePieceSwitch(Button):
    def __init__(self, image, borderwidth, highlightthickness, command, relief):
        Button.__init__(self, image = image, borderwidth = borderwidth, highlightthickness = highlightthickness, command = command, relief = relief)

    def on_click(self) -> None:
        piece_image = GameImageHandler.current_piece_image
        VASCO_piece_image = GameImageHandler.VASCO_piece_image
        AVAI_piece_image = GameImageHandler.AVAI_piece_image

        if piece_image == VASCO_piece_image:
            GameImageHandler.set_current_piece_image(AVAI_piece_image)
            self.configure(image = GameImageHandler.current_piece_image)
        else:
            GameImageHandler.set_current_piece_image(VASCO_piece_image)
            self.configure(image = GameImageHandler.current_piece_image)
