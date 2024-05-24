# Assuming piece.py contains the Piece class
from Pieces.piece import Piece

class Rook(Piece):
    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = 'Rook'

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        # Add all possible moves in the same column
        # Check all pieces in the same column
        i = row
        while i < 8:
            i += 1
            for piece in self.board:
                if piece.location == (column, i) and piece.white != self.white:
                    possibleLocations.append((column, i))
                    break
                elif piece.location == (column, i) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((column, i))
                
        i = row
        while i > 1:
            i -= 1
            for piece in self.board:
                if piece.location == (column, i) and piece.white != self.white:
                    possibleLocations.append((column, i))
                    break
                elif piece.location == (column, i) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((column, i))

        # Add all possible moves in the same row
        # Check all pieces in the same row
        i = column
        while i < 8:
            i += 1
            for piece in self.board:
                if piece.location == (i, row) and piece.white != self.white:
                    possibleLocations.append((i, row))
                    break
                elif piece.location == (i, row) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((i, row))
        i = column
        while i > 1:
            i -= 1
            for piece in self.board:
                if piece.location == (i, row) and piece.white != self.white:
                    possibleLocations.append((i, row))
                    break
                elif piece.location == (i, row) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((i, row))

        return possibleLocations
    
    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)
        else:
            print(f"Invalid move for Rook to {location}")
