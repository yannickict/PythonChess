from Pieces.piece import Piece

class Queen(Piece):

    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = "Queen"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        # Add all possible moves in the same column
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

        # Add all possible moves in the same diagonal
        i = row
        j = column
        while i < 8 and j < 8:
            i += 1
            j += 1
            for piece in self.board:
                if piece.location == (j, i) and piece.white != self.white:
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
                if piece.location == (j, i) and piece.white != self.white:
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
                if piece.location == (j, i) and piece.white != self.white:
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