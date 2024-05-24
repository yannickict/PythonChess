from Pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = "Bishop"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        # Add all possible moves in the same diagonal
        # Check all pieces in the same diagonal
        i = row
        j = column
        while i < 8 and j < 8:
            i += 1
            j += 1
            for piece in self.board:
                if piece.location == (j, i):
                    possibleLocations.append((j, i))
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((j, i))
        i = row
        j = column
        while i > 1 and j < 8:
            i -= 1
            j += 1
            for piece in self.board:
                if piece.location == (j, i):
                    possibleLocations.append((j, i))
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((j, i))
                    
        i = row
        j = column
        while i < 8 and j > 1:
            i += 1
            j -= 1
            for piece in self.board:
                if piece.location == (j, i):
                    possibleLocations.append((j, i))
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((j, i))
        i = row
        j = column
        while i > 1 and j > 1:
            i -= 1
            j -= 1
            for piece in self.board:
                if piece.location == (j, i) and piece.white != self.white:
                    possibleLocations.append((j, i))
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    break
                else:
                    possibleLocations.append((j, i))


        return possibleLocations

    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)