from Pieces.piece import Piece

class Queen(Piece):

    def __init__(self, location, white, board, boardObject):
        super().__init__(location, white, board, boardObject)
        self.name = "Queen"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []
        
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

        i = row
        j = column
        addPiece = True
        repeat = True
        while i < 7 and j < 7:
            i += 1
            j += 1
            for piece in self.board:
                if piece.location == (j, i) and piece.white != self.white:
                    repeat = False
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
                    repeat = False
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
                    repeat = False
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
                    repeat = False
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
