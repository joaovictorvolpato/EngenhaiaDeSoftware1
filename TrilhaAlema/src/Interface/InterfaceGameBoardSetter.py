from Interface.ProposeDrawButton import ProposeDrawButton
from Interface.PositionButton import PositionButton
from Interface.GameImageHandler import GameImageHandler
from tkinter import Tk
from Game.Board import Board
from Interface.BoardCanvas import BoardCanvas

class InterfaceGameBoardSetter:
    def __init__(self, board:Board) -> None:
        self.__canvas = BoardCanvas(bg = "#327421", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.__canvas.place(x = 0, y = 0)
        self.__board = board

    @property
    def canvas(self) -> BoardCanvas:
        return self.__canvas

    def set_game_board(self) -> None:
        self.__setup_propose_draw_button(self.__board)
        self.__setup_piece_switches(self.__board)

    def __setup_propose_draw_button(self, board:Board) -> None: #ADD TO MODELLING
        propose_draw_button = ProposeDrawButton(
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: propose_draw_button.on_click(),
            relief="flat",
            board=board
        )
        propose_draw_button.place(
            x=287.0,
            y=832.0,
            width=60.0,
            height=60.0
        )

    def __setup_piece_switches(self, board:Board) -> None: #Change piece switches names to match the board places sequence. Code on click to return the button number
        piece_switch_32 = PositionButton(
            id = 32,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_32.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_32.place(
            x=662.0,
            y=691.0,
            width=50.0,
            height=50.0
        )

        piece_switch_20 = PositionButton(
            id = 20,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_20.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_20.place(
            x=162.0,
            y=491.0,
            width=50.0,
            height=50.0
        )

        piece_switch_26 = PositionButton(
            id = 26,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_26.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_26.place(
            x=162.0,
            y=591.0,
            width=50.0,
            height=50.0
        )

        piece_switch_9 = PositionButton(
            id = 9,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_9.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_9.place(
            x=362.0,
            y=291.0,
            width=50.0,
            height=50.0
        )

        piece_switch_4 = PositionButton(
            id = 4,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_4.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_4.place(
            x=362.0,
            y=191.0,
            width=50.0,
            height=50.0
        )

        piece_switch_1 = PositionButton(
            id = 1,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:piece_switch_1.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_1.place(
            x=262.0,
            y=100.0,
            width=50.0,
            height=50.0
        )

        piece_switch_8 = PositionButton(
            id = 8,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_8.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_8.place(
            x=262.0,
            y=291.0,
            width=50.0,
            height=50.0
        )

        piece_switch_15 = PositionButton(
            id = 15,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_15.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_15.place(
            x=262.0,
            y=391.0,
            width=50.0,
            height=50.0
        )

        piece_switch_21 = PositionButton(
            id = 21,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_21.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_21.place(
            x=262.0,
            y=491.0,
            width=50.0,
            height=50.0
        )

        piece_switch_31 = PositionButton(
            id = 31,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_31.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_31.place(
            x=562.0,
            y=691.0,
            width=50.0,
            height=50.0
        )

        piece_switch_14 = PositionButton(
            id = 14,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_14.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_14.place(
            x=162.0,
            y=391.0,
            width=50.0,
            height=50.0
        )

        piece_switch_30 = PositionButton(
            id = 30,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_30.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_30.place(
            x=462.0,
            y=691.0,
            width=50.0,
            height=50.0
        )

        piece_switch_16 = PositionButton(
            id = 16,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_16.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_16.place(
            x=362.0,
            y=391.0,
            width=50.0,
            height=50.0
        )

        piece_switch_23 = PositionButton(
            id = 23,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_23.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_23.place(
            x=462.0,
            y=491.0,
            width=50.0,
            height=50.0
        )

        piece_switch_29 = PositionButton(
            id = 29,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_29.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_29.place(
            x=562.0,
            y=591.0,
            width=50.0,
            height=50.0
        )

        piece_switch_12 = PositionButton(
            id = 12,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_12.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_12.place(
            x=662.0,
            y=291.0,
            width=50.0,
            height=50.0
        )

        piece_switch_13 = PositionButton(
            id = 13,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_13.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_13.place(
            x=762.0,
            y=291.0,
            width=50.0,
            height=50.0
        )

        piece_switch_7 = PositionButton(
            id = 7,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_7.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_7.place(
            x=762.0,
            y=191.0,
            width=50.0,
            height=50.0
        )

        piece_switch_19 = PositionButton(
            id = 19,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_19.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_19.place(
            x=762.0,
            y=391.0,
            width=50.0,
            height=50.0
        )

        piece_switch_28 = PositionButton(
            id = 28,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_28.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_28.place(
            x=462.0,
            y=591.0,
            width=50.0,
            height=50.0
        )

        piece_switch_25= PositionButton(
            id = 25,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_25.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_25.place(
            x=662.0,
            y=491.0,
            width=50.0,
            height=50.0
        )

        piece_switch_18 = PositionButton(
            id = 18,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_18.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_18.place(
            x=662.0,
            y=391.0,
            width=50.0,
            height=50.0
        )

        piece_switch_24 = PositionButton(
            id = 24,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_24.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_24.place(
            x=562.0,
            y=491.0,
            width=50.0,
            height=50.0
        )

        piece_switch_10 = PositionButton(
            id = 10,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_10.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_10.place(
            x=462.0,
            y=291.0,
            width=50.0,
            height=50.0
        )

        piece_switch_5 = PositionButton(
            id = 5,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_5.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_5.place(
            x=462.0,
            y=191.0,
            width=50.0,
            height=50.0
        )

        piece_switch_3 = PositionButton(
            id = 3,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_3.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_3.place(
            x=461.0,
            y=100.0,
            width=50.0,
            height=50.0
        )

        piece_switch_2 = PositionButton(
            id = 2,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_2.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_2.place(
            x=362.0,
            y=100.0,
            width=50.0,
            height=50.0
        )

        piece_switch_11 = PositionButton(
            id = 11,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_11.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_11.place(
            x=562.0,
            y=291.0,
            width=50.0,
            height=50.0
        )

        piece_switch_6 = PositionButton(
            id = 6,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_6.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_6.place(
            x=562.0,
            y=191.0,
            width=50.0,
            height=50.0
        )

        piece_switch_17 = PositionButton(
            id = 17,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_17.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_17.place(
            x=562.0,
            y=391.0,
            width=50.0,
            height=50.0
        )

        piece_switch_22 = PositionButton(
            id = 22,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_22.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_22.place(
            x=362.0,
            y=491.0,
            width=50.0,
            height=50.0
        )

        piece_switch_27 = PositionButton(
            id = 27,
            image=GameImageHandler.button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: piece_switch_27.on_click(),
            relief="flat",
            board=board
        )
        piece_switch_27.place(
            x=362.0,
            y=591.0,
            width=50.0,
            height=50.0
        )
