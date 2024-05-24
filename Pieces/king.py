from Pieces.piece import Piece
class King(Piece):
    def __init__(self, location, board, white):
        super().__init__(location, board, white)
        self.name = "King"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if column + i < 1 or column + i > 8 or row + j < 1 or row + j > 8:
                    continue
                for piece in self.board:
                    if piece.location == (column + i, row + j) and piece.white != self.white:
                        possibleLocations.append((column + i, row + j))
                        break
                    elif piece.location == (column + i, row + j) and piece.white == self.white:
                        break
                    else:
                        possibleLocations.append((column + i, row + j))