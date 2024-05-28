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
        for column in range(0, 1):
            pawnwhite = Pawn((column, 1), True, self.board)
            self.board.append(pawnwhite)

            pawnblack = Pawn((column, 6), False, self.board)
            self.board.append(pawnblack)

        # Add rooks
        rookwhiteleft = Rook((0, 0), True, self.board)
        self.board.append(rookwhiteleft)
        rookwhiteright = Rook((7, 0), True, self.board)
        self.board.append(rookwhiteright)

        rookblackleft = Rook((0, 7), False, self.board)
        self.board.append(rookblackleft)
        rookblackright = Rook((7, 7), False, self.board)
        self.board.append(rookblackright)

        # Add Bishops
        bishopwhiteleft = Bishop((2, 0), True, self.board)
        self.board.append(bishopwhiteleft)
        bishopwhiteright = Bishop((5, 0), True, self.board)
        self.board.append(bishopwhiteright)

        bishopblackleft = Bishop((2, 7), False, self.board)
        self.board.append(bishopblackleft)
        bishopblackright = Bishop((5, 7), False, self.board)
        self.board.append(bishopblackright)

        # Add Knights
        knightwhiteleft = Knight((1, 0), True, self.board)
        self.board.append(knightwhiteleft)
        knightwhiteright = Knight((6, 0), True, self.board)
        self.board.append(knightwhiteright)

        knightblackleft = Knight((1, 7), False, self.board)
        self.board.append(knightblackleft)
        knightblackright = Knight((6, 7), False, self.board)
        self.board.append(knightblackright)

        # Add Queens
        queenwhite = Queen((3, 0), True, self.board)
        self.board.append(queenwhite)
        queenblack = Queen((4, 7), False, self.board)
        self.board.append(queenblack)

        # Add Kings
        kingwhite = King((4, 0), True, self.board)
        self.board.append(kingwhite)
        kingblack = King((3, 7), False, self.board)
        self.board.append(kingblack)



    def place_piece(self, piece, location):
        pass

    def remove_piece(self, piece):
        pass