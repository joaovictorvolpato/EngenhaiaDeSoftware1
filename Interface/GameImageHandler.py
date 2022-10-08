from tkinter import PhotoImage
from GamePath import GamePath

class GameImageHandler:
    canvas_image = PhotoImage(
        file=GamePath.relative_to_assets("canvas_image.png")
        )

    button_image = PhotoImage(
        file = GamePath.relative_to_assets("button_image.png")
        )

    AVAI_piece_image = PhotoImage(
        file=GamePath.relative_to_assets("AVAI.png")
        )

    VASCO_piece_image = PhotoImage(
        file = GamePath.relative_to_assets("VASCO.png")
        )   

    current_piece_image = VASCO_piece_image

    @classmethod
    def set_current_piece_image(cls, piece_image:PhotoImage) -> None:
        GameImageHandler.current_piece_image = piece_image
