from tkinter import Button
from GameImageHandler import GameImageHandler

class PieceSwitch(Button):
    def __init__(self, id, image, borderwidth, highlightthickness, command, relief):
        Button.__init__(self, image = image, borderwidth = borderwidth, highlightthickness = highlightthickness, command = command, relief = relief)
        self.button_image = GameImageHandler.button_image
        self.button_pressed = False
        self.name = id

    def on_click(self) -> None:
        print(self.name)
        if not self.button_pressed:
            self.configure(image = GameImageHandler.current_piece_image)
            self.set_button_pressed()

        else:
            self.configure(image = GameImageHandler.button_image)
            self.set_button_pressed()

    def set_button_pressed(self) -> bool:
        self.button_pressed = not self.button_pressed
