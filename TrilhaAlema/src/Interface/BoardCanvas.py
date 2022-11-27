from tkinter import Canvas, Tk, PhotoImage
from Interface.GameImageHandler import GameImageHandler

class BoardCanvas(Canvas):
    def __init__(self, bg:str, height:int, width:int, bd:int, highlightthickness:int, relief:str) -> None:
        Canvas.__init__(self, width = width, height = height, bg = bg, highlightthickness = highlightthickness, bd = bd, relief = relief)
        self.__draw_image_on_canvas(492.0, 428.0, GameImageHandler.canvas_image)
        self.__draw_button_text = self.__write_on_canvas(203.0, 781.0, anchor="nw", text="Click to Propose Draw", fill="#FFFFFF", font=("Inter", 32 * -1))
        self.__local_player_info, self.__remote_player_info = self.__create_players_info()
        self.__local_player_text, self.__remote_player_text = self.__write_player_texts()
        self.__local_player_pieces_in_hand, self.__remote_player_pieces_in_hand = self.__write_players_pieces_in_hand()
        self.__local_player_captured_pieces, self.__remote_player_captured_pieces = self.__write_players_captured_pieces()

    @property
    def local_player_pieces_in_hand(self):
        return self.__local_player_pieces_in_hand

    @local_player_pieces_in_hand.setter
    def local_player_pieces_in_hand(self, pieces_in_hand:int) -> None:
        self.change_text(f"Pieces In Hand: {pieces_in_hand}", self.__local_player_pieces_in_hand)

    @property
    def remote_player_pieces_in_hand(self):
        return self.__remote_player_pieces_in_hand

    @remote_player_pieces_in_hand.setter
    def remote_player_pieces_in_hand(self, pieces_in_hand:int) -> None:
        self.__change_text(f"Pieces In Hand: {pieces_in_hand}", self.__local_player_pieces_in_hand)

    @property
    def local_player_captured_pieces(self):
        return self.__local_player_captured_pieces

    @local_player_captured_pieces.setter
    def local_player_captured_pieces(self, captured_pieces:int) -> None:
        self.__change_text(f"Captured Pieces: {captured_pieces}", self.__local_player_captured_pieces)
    
    @property
    def remote_player_captured_pieces(self):
        return self.__remote_player_captured_pieces

    @remote_player_captured_pieces.setter
    def remote_player_captured_pieces(self, captured_pieces:int) -> None:
        self.__change_text(f"Captured Pieces: {captured_pieces}", self.__remote_player_captured_pieces)

    def __draw_image_on_canvas(self, width:float, height:float, image:PhotoImage):
        image_drawn = self.create_image(width, height, image = image)
        
        return image_drawn

    def __create_players_info(self) -> tuple:
        local_player_info = self.create_rectangle(989.0, 80.0, 1194.0, 756.0, fill="#FFFFFF", outline="")
        remote_player_info = self.create_rectangle(1214.0, 80.0, 1419.0, 756.0, fill="#FFFFFF", outline="")

        return local_player_info, remote_player_info

    def __write_player_texts(self) -> tuple:
        local_player_text = self.__write_on_canvas(1007.0, 105.0, anchor="nw", text="You", fill="#000000", font=("Inter", 32 * -1))
        remote_player_text = self.__write_on_canvas(1238.0, 104.0, anchor="nw", text="Opponent", fill="#000000", font=("Inter", 32 * -1))
        
        return local_player_text, remote_player_text

    def __write_players_pieces_in_hand(self) -> tuple:
        local_player_pieces_in_hand = self.__write_on_canvas(1007.0, 241.0, anchor="nw", text="Pieces In Hand: 12", fill="#000000", font=("Inter", 20 * -1))
        remote_player_pieces_in_hand = self.__write_on_canvas(1238.0, 241.0, anchor="nw", text="Pieces In Hand: 12", fill="#000000", font=("Inter", 20 * -1))

        return local_player_pieces_in_hand, remote_player_pieces_in_hand
    
    def __write_players_captured_pieces(self) -> tuple:
        local_player_captured_pieces = self.__write_on_canvas(1007.0, 385.0, anchor="nw", text="Captured Pieces: 0", fill="#000000", font=("Inter", 20 * -1))
        remote_player_captured_pieces = self.__write_on_canvas(1238.0, 385.0, anchor="nw", text="Captured Pieces: 0", fill="#000000", font=("Inter", 20 * -1))

        return local_player_captured_pieces, remote_player_captured_pieces

    def __write_on_canvas(self, width:float, height:int, anchor:str, text:str, fill:str, font:tuple[str, int]) -> None:
        written_text = self.create_text(width, height, anchor = anchor, text = text, fill = fill, font = font)

        return written_text

    def __change_text(self, text:str, written_text) -> None:
        self.itemconfig(written_text, text = text)

    def draw_team_images(self, local_image:PhotoImage, remote_image:PhotoImage) -> None: #Called after start match for starter and receive start for receiver.
        self.draw_image_on_canvas(1050.0, 591.0, local_image = GameImageHandler.VASCO_piece_image) #Change later
        self.draw_image_on_canvas(1275.0, 591.0, remote_image = GameImageHandler.AVAI_piece_image) #Change later
