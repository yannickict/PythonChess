# Assuming piece.py contains the Piece class
from Pieces.piece import Piece

class Rook(Piece):
    def __init__(self, location, white, board, boardObject):
        super().__init__(location, white, board , boardObject)
        self.name = 'Rook'

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        # Add all possible moves in the same column
        # Check all pieces in the same column
        i = row
        while i < 7:
            i += 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (column, i) and piece.white != self.white:
                    repeat = False
                    break
                elif piece.location == (column, i) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((column, i))
            if not repeat:
                break
                
        i = row
        while i > 0:
            i -= 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (column, i) and piece.white != self.white:
                    repeat = False
                    break
                elif piece.location == (column, i) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((column, i))
            if not repeat:
                break

        # Add all possible moves in the same row
        # Check all pieces in the same row
        i = column
        while i < 7:
            i += 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (i, row) and piece.white != self.white:
                    repeat = False
                    break
                elif piece.location == (i, row) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((i, row))
            if not repeat:
                break

        i = column
        while i > 0:
            i -= 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (i, row) and piece.white != self.white:
                    repeat = False
                    break
                elif piece.location == (i, row) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((i, row))
            if not repeat:
                break

        return possibleLocations
    
    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)
        else:
            print(f"Invalid move for Rook to {location}")
