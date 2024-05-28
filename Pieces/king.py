from Pieces.piece import Piece
class King(Piece):
    def __init__(self, location, board, white):
        super().__init__(location, board, white)
        self.name = "King"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if column + x < 0 or column + x > 7 or row + y < 0 or row + y > 7:
                    continue
                possible = True
                for piece in self.board:
                    if piece.location == (column + x, row + y) and piece.white == self.white:
                        possible = False
                if possible:
                    possibleLocations.append((column + x, row + y))
        return possibleLocations