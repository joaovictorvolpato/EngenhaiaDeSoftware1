from tkinter import Canvas, Tk

class BoardCanvas(Canvas):
    def __init__(self, window:Tk, bg:str, height:int, width:int, bd:int, highlightthickness:int, relief:str) -> None:
        Canvas.__init__(self, master, width = width, height = height, bg = bg, highlightthickness = highlightthickness, bd = bd, relief = relief)

    def draw_rectangle(self, position:tuple, position2:tuple, fill:str, width:int) -> None:
        self.create_rectangle(position, position2, fill = fill, width = width)

        def __setup_canvas(self) -> None:
        canvas = Canvas(
            self.__window,
            bg = "#327421",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)

        board_image = canvas.create_image(
            492.0,
            428.0,
            image=GameImageHandler.canvas_image
        )

        canvas.create_rectangle(
            989.0,
            80.0,
            1194.0,
            756.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            1214.0,
            80.0,
            1419.0,
            756.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            1238.0,
            104.0,
            anchor="nw",
            text="Opponent",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        canvas.create_text(
            1007.0,
            105.0,
            anchor="nw",
            text="You",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        canvas.create_text(
            203.0,
            781.0,
            anchor="nw",
            text="Click to Propose Draw",
            fill="#FFFFFF",
            font=("Inter", 32 * -1)
        )

        canvas.create_rectangle(
            479.0,
            862.0,
            612.0,
            967.0,
            fill="#327421",
            outline="")
        
    def draw_piece(self, position:tuple, piece_image) -> None:
        self.create_image(position, image = piece_image)

    def draw_button(self, position:tuple, button_image) -> None:
        self.create_image(position, image = button_image)

    def draw_text(self, position:tuple, text:str, font:str, fill:str) -> None:
        self.create_text(position, text = text, font = font, fill = fill)

    def draw_line(self, position:tuple, position2:tuple, fill:str, width:int) -> None:
        self.create_line(position, position2, fill = fill, width = width)