from Pieces.piece import Piece

class Queen(Piece):

    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = "Queen"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []
        i = row
        while i < 8:
            i += 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (column, i) and piece.white != self.white:
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
        while i > 1:
            i -= 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (column, i) and piece.white != self.white:
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
        while i < 8:
            i += 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (i, row) and piece.white != self.white:
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
        while i > 1:
            i -= 1
            addPiece = True
            repeat = True
            for piece in self.board:
                if piece.location == (i, row) and piece.white != self.white:
                    break
                elif piece.location == (i, row) and piece.white == self.white:
                    addPiece = False
                    repeat = False
                    break
            if addPiece:
                possibleLocations.append((i, row))
            if not repeat:
                break
            # Add all possible moves in the same diagonal
        # Check all pieces in the same diagonal
        i = row
        j = column
        while i < 8 and j < 8:
            i += 1
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
        while i > 1 and j < 8:
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
        while i < 8 and j > 1:
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
        while i > 1 and j > 1:
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