# Assuming piece.py contains the Piece class
from Pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = "Pawn"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        # Add all possible moves in the same column
        if self.board[row + 1][column] == 0:
            possibleLocations.append((column, row + 1))

        if row == 2:
            empty = True
            for piece in self.board:
                if piece.location == (column, row + 2):
                    empty = False
            if empty:
                possibleLocations.append((column, row + 2))

        # Add all possible moves with kill
        for piece in self.board:
            if piece.location == (column - 1, row + 1) and piece.white != self.white:
                possibleLocations.append((column - 1, row + 1))
            if piece.location == (column + 1, row + 1) and piece.white != self.white:
                possibleLocations.append((column + 1, row + 1))

        return possibleLocations
    
    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)
        else:
            print(f"Invalid move for Rook to {location}")
