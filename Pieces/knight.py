from Pieces.piece import Piece
class Knight(Piece):
    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = "Knight"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        # Add all possible moves
        if column + 2 < 9 and row + 1 < 9:
            empty = True
            for piece in self.board:
                if piece.location == (column + 2, row + 1) and piece.white == self.white:
                    empty = False
            if empty:
                possibleLocations.append((column + 2, row + 1))
        if column + 2 < 9 and row - 1 > 0:
            empty = True
            for piece in self.board:
                if piece.location == (column + 2, row - 1) and piece.white == self.white:
                    empty = False
            if empty:
                possibleLocations.append((column + 2, row - 1))
        if column - 2 > 0 and row + 1 < 9:
            empty = True
            for piece in self.board:
                if piece.location == (column - 2, row + 1) and piece.white == self.white:
                    empty = False
            if empty:
                possibleLocations.append((column - 2, row + 1))
        if column - 2 > 0 and row - 1 > 0:
            empty = True
            for piece in self.board:
                if piece.location == (column - 2, row - 1) and piece.white == self.white:
                    empty = False
            if empty:
                possibleLocations.append((column - 2, row - 1))
        if column + 1 < 9 and row + 2 < 9:
            empty = True
            for piece in self.board:
                if piece.location == (column + 1, row + 2) and piece.white == self.white:
                    empty = False
            if empty:
                possibleLocations.append((column + 1, row + 2))
        if column + 1 < 9 and row - 2 > 0:
            empty = True
            for piece in self.board:
                if piece.location == (column + 1, row - 2) and piece.white == self.white:
                    empty = False
            if empty:
                possibleLocations.append((column + 1, row - 2))
        if column - 1 > 0 and row + 2 < 9:
            empty = True
            for piece in self.board:
                if piece.location == (column - 1, row + 2) and piece.white == self.white:
                    empty = False
            if empty:
                possibleLocations.append((column - 1, row + 2))
        if column - 1 > 0 and row - 2 > 0:
            empty = True
            for piece in self.board:
                if piece.location == (column - 1, row - 2) and piece.white != self.white:
                    empty = False
            if empty:
                possibleLocations.append((column - 1, row - 2))

        return possibleLocations
    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)
        else:
            print(f"Invalid move for Knight to {location}")