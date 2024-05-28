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
        addPiece = True
        repeat = True
        while i < 7 and j < 7:
            i += 1
            j += 1
            for piece in self.board:
                if piece.location == (j, i) and piece.white != self.white:
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((j, i))
            if not repeat:
                break
        i = row
        j = column
        while i > 0 and j < 7:
            i -= 1
            j += 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (j, i) and piece.white != self.white:
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((j, i))
            if not repeat:
                break
                    
        i = row
        j = column
        while i < 7 and j > 0:
            i += 1
            j -= 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (j, i) and piece.white != self.white:
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((j, i))
            if not repeat:
                break

            
        i = row
        j = column
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (j, i) and piece.white != self.white:
                    break
                elif piece.location == (j, i) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((j, i))
            if not repeat:
                break


        return possibleLocations

    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)