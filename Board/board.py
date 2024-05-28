from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.bishop import Bishop
from Pieces.knight import Knight
from Pieces.queen import Queen
from Pieces.king import King

class Board:
    def __init__(self):
        self.board = []

        # -----Add all pieces-----

        # Add pawns
        for column in range(1, 9):
            pawnwhite = Pawn((column, 7), True, self.board)
            self.board.append(pawnwhite)

            pawnblack = Pawn((column, 2), False, self.board)
            self.board.append(pawnblack)

        # Add rooks
        rookwhiteleft = Rook((1, 8), True, self.board)
        self.board.append(rookwhiteleft)
        rookwhiteright = Rook((8, 8), True, self.board)
        self.board.append(rookwhiteright)

        rookblackleft = Rook((1, 1), False, self.board)
        self.board.append(rookblackleft)
        rookblackright = Rook((8, 1), False, self.board)
        self.board.append(rookblackright)

        # Add Bishops
        bishopwhiteleft = Bishop((3, 8), True, self.board)
        self.board.append(bishopwhiteleft)
        bishopwhiteright = Bishop((6, 8), True, self.board)
        self.board.append(bishopwhiteright)

        bishopblackleft = Bishop((3, 1), False, self.board)
        self.board.append(bishopblackleft)
        bishopblackright = Bishop((6, 1), False, self.board)
        self.board.append(bishopblackright)

        # Add Knights
        knightwhiteleft = Knight((2, 8), True, self.board)
        self.board.append(knightwhiteleft)
        knightwhiteright = Knight((7, 8), True, self.board)
        self.board.append(knightwhiteright)

        knightblackleft = Knight((2, 1), False, self.board)
        self.board.append(knightblackleft)
        knightblackright = Knight((7, 1), False, self.board)
        self.board.append(knightblackright)

        # Add Queens
        queenwhite = Queen((5, 8), True, self.board)
        self.board.append(queenwhite)
        queenblack = Queen((4, 1), False, self.board)
        self.board.append(queenblack)

        # Add Kings
        kingwhite = King((4, 8), True, self.board)
        self.board.append(kingwhite)
        kingblack = King((5, 1), False, self.board)
        self.board.append(kingblack)



    def place_piece(self, piece, location):
        pass

    def remove_piece(self, piece):
        pass