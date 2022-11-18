from tkinter import PhotoImage
from GamePath import GamePath

class GameImageHandler:
    """Stores all images used in the game. Photoimages must be
    set only after the window is created, so the set method is only 
    called after the GameInterface instantiates TKinter's window."""
    canvas_image = None
    button_image = None
    AVAI_piece_image = None
    VASCO_piece_image = None
    current_piece_image = None

    @classmethod
    def set_game_images(cls) -> None:
        cls.canvas_image = PhotoImage(file=GamePath.relative_to_assets("canvas_image.png"))
        cls.button_image = PhotoImage(file = GamePath.relative_to_assets("button_image.png"))
        cls.AVAI_piece_image = PhotoImage(file=GamePath.relative_to_assets("AVAI.png"))
        cls.VASCO_piece_image = PhotoImage(file = GamePath.relative_to_assets("VASCO.png"))   
        cls.current_piece_image = cls.VASCO_piece_image

    @classmethod
    def set_current_piece_image(cls, piece_image:PhotoImage) -> None:
        cls.current_piece_image = piece_image
