from abc import ABC, abstractmethod

class AbstractInterfaceUpdater(ABC):
    @abstractmethod
    def set_message(self, aMessage):
        pass

    @abstractmethod
    def set_player1_pieces(self, *aPlayer1_pieces):
        pass

    @abstractmethod
    def set_player2_pieces(self, *aPlayer2_pieces):
        pass

    @abstractmethod
    def get_message(self):
        pass

    @abstractmethod
    def get_player1_pieces(self):
        pass

    @abstractmethod
    def get_player2_pieces(self):
        """@ReturnType Piece*"""
        pass

    @abstractmethod
    def updateInterfaceImage(self, aPlayer_interface):
        """@ParamType aPlayer_interface PlayerInterface"""
        pass

    @abstractmethod
    def displayPiecesOnPositions(self, aPlayer_interface, aPositions_to_update):
        """@ParamType aPlayer_interface PlayerInterface
        @ParamType aPositions_to_update list"""
        pass

    @abstractmethod
    def displayPiecesInLocalPlayerHand(self, aPlayer_interface, aPieces_in_local_player_hand):
        """@ParamType aPlayer_interface PlayerInterface
        @ParamType aPieces_in_local_player_hand int"""
        pass

    @abstractmethod
    def displayPiecesInRemoteplayerHand(self, aPlayer_interface, aPieces_in_remote_player_hand):
        pass

    @abstractmethod
    def displayWinner(self, aPlayer_interface, aWinner_to_display):
        pass

    @abstractmethod
    def notifyAbandonedMatch(self, aPlayer_interface, aMatch_was_abandoned):
        pass

    @abstractmethod
    def notifyDraw(self, aPlayer_interface):
        pass
