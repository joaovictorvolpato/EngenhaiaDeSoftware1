from Interface.ProposeDrawButton import ProposeDrawButton
from Interface.PositionButton import PositionButton
from Interface.GameImageHandler import GameImageHandler
from Game.Board import Board
from Interface.BoardCanvas import BoardCanvas

class InterfaceGameBoard:
    def __init__(self, board:Board) -> None:
        self.__canvas = BoardCanvas(bg = "#327421", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.__canvas.place(x = 0, y = 0)
        self.__board = board
        self.__canvas.draw_team_images() #Remove later, drawn in start or receive
        self.__setup_propose_draw_button(self.__board)
        self.__position_buttons_list = self.__setup_position_buttons(self.__board) 

    @property
    def canvas(self) -> BoardCanvas:
        return self.__canvas

    @property
    def position_buttons_list(self) -> list[PositionButton]:
        return self.__position_buttons_list

    def __setup_propose_draw_button(self, board:Board) -> None: #ADD TO MODELLING
        propose_draw_button = ProposeDrawButton(
            image=GameImageHandler.button_image,  borderwidth=0, highlightthickness=0, command=propose_draw_button.on_click(), relief="flat", board=board
            )
        propose_draw_button.place(x=287.0, y=832.0, width=60.0, height=60.0)

    def __setup_position_buttons(self, board:Board) -> None: #Change piece switches names to match the board places sequence. Code on click to return the button number
        position_button_32 = PositionButton(
            id = 32, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_32.on_click(), relief="flat",board=board
            )
        position_button_32.place(x=662.0, y=691.0, width=50.0, height=50.0)

        position_button_20 = PositionButton(
            id = 20, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_20.on_click(), relief="flat",board=board
            )
        position_button_20.place(x=162.0, y=491.0, width=50.0, height=50.0)

        position_button_26 = PositionButton(
            id = 26, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_26.on_click(), relief="flat",board=board
            )
        position_button_26.place(x=162.0, y=591.0, width=50.0, height=50.0)

        position_button_9 = PositionButton(
             id = 9, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_9.on_click(), relief="flat",board=board
             )
        position_button_9.place(x=362.0, y=291.0, width=50.0, height=50.0)

        position_button_4 = PositionButton(
             id = 4, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_4.on_click(), relief="flat",board=board
             )
        position_button_4.place(x=362.0, y=191.0, width=50.0, height=50.0)

        position_button_1 = PositionButton(
             id = 1, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,   command=position_button_1.on_click(), relief="flat",board=board
             )
        position_button_1.place(x=262.0, y=100.0, width=50.0, height=50.0)

        position_button_8 = PositionButton(
             id = 8, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_8.on_click(), relief="flat",board=board
             )
        position_button_8.place(x=262.0, y=291.0, width=50.0, height=50.0)

        position_button_15 = PositionButton(
            id = 15, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_15.on_click(), relief="flat",board=board
            )
        position_button_15.place(x=262.0, y=391.0, width=50.0, height=50.0)

        position_button_21 = PositionButton(
            id = 21, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_21.on_click(), relief="flat",board=board
            )
        position_button_21.place(x=262.0, y=491.0, width=50.0, height=50.0)

        position_button_31 = PositionButton(
            id = 31, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_31.on_click(), relief="flat",board=board
            )
        position_button_31.place(x=562.0, y=691.0, width=50.0, height=50.0)

        position_button_14 = PositionButton(
            id = 14, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_14.on_click(), relief="flat",board=board
            )
        position_button_14.place(x=162.0, y=391.0, width=50.0, height=50.0)

        position_button_30 = PositionButton(
            id = 30, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_30.on_click(), relief="flat",board=board
            )
        position_button_30.place(x=462.0, y=691.0, width=50.0, height=50.0)

        position_button_16 = PositionButton(
            id = 16, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_16.on_click(), relief="flat",board=board
            )
        position_button_16.place(x=362.0, y=391.0, width=50.0, height=50.0)

        position_button_23 = PositionButton(
            id = 23, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_23.on_click(), relief="flat",board=board
            )
        position_button_23.place(x=462.0, y=491.0, width=50.0, height=50.0)

        position_button_29 = PositionButton(
            id = 29, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_29.on_click(), relief="flat",board=board
            )
        position_button_29.place(x=562.0, y=591.0, width=50.0, height=50.0)

        position_button_12 = PositionButton(
            id = 12, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_12.on_click(), relief="flat",board=board
            )
        position_button_12.place(x=662.0, y=291.0, width=50.0, height=50.0)

        position_button_13 = PositionButton(
            id = 13, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_13.on_click(), relief="flat",board=board
            )
        position_button_13.place(x=762.0, y=291.0, width=50.0, height=50.0)

        position_button_7 = PositionButton(
             id = 7, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_7.on_click(), relief="flat",board=board
             )
        position_button_7.place(x=762.0, y=191.0, width=50.0, height=50.0)

        position_button_19 = PositionButton(
            id = 19, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_19.on_click(), relief="flat",board=board
            )
        position_button_19.place(x=762.0, y=391.0, width=50.0, height=50.0)

        position_button_28 = PositionButton(
            id = 28, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_28.on_click(), relief="flat",board=board
            )
        position_button_28.place(x=462.0, y=591.0, width=50.0, height=50.0)

        position_button_25= PositionButton(
            id = 25, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_25.on_click(), relief="flat",board=board
            )
        position_button_25.place(x=662.0, y=491.0, width=50.0, height=50.0)

        position_button_18 = PositionButton(
            id = 18, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_18.on_click(), relief="flat",board=board
            )
        position_button_18.place(x=662.0, y=391.0, width=50.0, height=50.0)

        position_button_24 = PositionButton(
            id = 24, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_24.on_click(), relief="flat",board=board
            )
        position_button_24.place(x=562.0, y=491.0, width=50.0, height=50.0)

        position_button_10 = PositionButton(
            id = 10, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_10.on_click(), relief="flat",board=board
            )
        position_button_10.place(x=462.0, y=291.0, width=50.0, height=50.0)

        position_button_5 = PositionButton(
             id = 5, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_5.on_click(), relief="flat",board=board
             )
        position_button_5.place(x=462.0, y=191.0, width=50.0, height=50.0)

        position_button_3 = PositionButton(
             id = 3, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_3.on_click(), relief="flat",board=board
             )
        position_button_3.place(x=461.0, y=100.0, width=50.0, height=50.0)

        position_button_2 = PositionButton(
             id = 2, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_2.on_click(), relief="flat",board=board
             )
        position_button_2.place(x=362.0, y=100.0, width=50.0, height=50.0)

        position_button_11 = PositionButton(
            id = 11, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_11.on_click(), relief="flat",board=board
            )
        position_button_11.place(x=562.0, y=291.0, width=50.0, height=50.0)

        position_button_6 = PositionButton(
             id = 6, image=GameImageHandler.button_image,borderwidth=0, highlightthickness=0,  command=position_button_6.on_click(), relief="flat",board=board
             )
        position_button_6.place(x=562.0, y=191.0, width=50.0, height=50.0)

        position_button_17 = PositionButton(
            id = 17, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_17.on_click(), relief="flat",board=board
            )
        position_button_17.place(x=562.0, y=391.0, width=50.0, height=50.0)

        position_button_22 = PositionButton(
            id = 22, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_22.on_click(), relief="flat",board=board
            )
        position_button_22.place(x=362.0, y=491.0, width=50.0, height=50.0)

        position_button_27 = PositionButton(
            id = 27, image=GameImageHandler.button_image, borderwidth=0, highlightthickness=0, command=position_button_27.on_click(), relief="flat",board=board
            )
        position_button_27.place(x=362.0, y=591.0, width=50.0, height=50.0)
        
        position_buttons_list = [position_button_1, position_button_2, position_button_3, position_button_4, 
                                 position_button_5, position_button_6, position_button_7, position_button_8, 
                                 position_button_9, position_button_10, position_button_11, position_button_12, 
                                 position_button_13, position_button_14, position_button_15, position_button_16, 
                                 position_button_17, position_button_18, position_button_19, position_button_20, 
                                 position_button_21, position_button_22, position_button_23, position_button_24, 
                                 position_button_25, position_button_26, position_button_27, position_button_28, 
                                 position_button_29, position_button_30, position_button_31, position_button_32]
        
        return position_buttons_list
