from tkinter import Button, PhotoImage
from GameImageHandler import GameImageHandler

class PieceSwitch(Button):
    def __init__(self, id:int, image:PhotoImage, borderwidth:int, highlightthickness:int, command, relief:str) -> None:
        Button.__init__(self, image = image, borderwidth = borderwidth, highlightthickness = highlightthickness, command = command, relief = relief)
        self.button_image = GameImageHandler.button_image
        self.button_pressed:bool = False
        self.id = id

    def on_click(self) -> None:
        print(self.id)
        if not self.button_pressed:
            self.configure(image = GameImageHandler.current_piece_image)
            self.set_button_pressed()

        else:
            self.configure(image = GameImageHandler.button_image)
            self.set_button_pressed()

    def set_button_pressed(self) -> bool:
        self.button_pressed = not self.button_pressed
