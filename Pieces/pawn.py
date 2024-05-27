from Pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = "Pawn"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        if self.white:
            # Check one square ahead
            if row - 1 > 0:
                has_piece = False
                for piece in self.board:
                    if piece.location == (column, row - 1):
                        has_piece = True
                        break
                if not has_piece:
                    possibleLocations.append((column, row - 1))

            # Check two squares ahead from starting position
            if row == 7:
                empty = True
                for piece in self.board:
                    if piece.location == (column, row - 2) or piece.location == (column, row - 1):
                        empty = False
                        break
                if empty:
                    possibleLocations.append((column, row - 2))

            # Check for kill moves
            for offset in [-1, 1]:
                target_row = row - 1
                target_column = column + offset
                for piece in self.board:
                    if piece.location == (target_column, target_row) and piece.white != self.white:
                        possibleLocations.append((target_column, target_row))
                        break
        if not self.white:
            # Check one square ahead
            if row + 1 <= 8:
                has_piece = False
                for piece in self.board:
                    if piece.location == (column, row + 1):
                        has_piece = True
                        break
                if not has_piece:
                    possibleLocations.append((column, row + 1))

            # Check two squares ahead from starting position
            if row == 2:
                empty = True
                for piece in self.board:
                    if piece.location == (column, row + 2) or piece.location == (column, row + 1):
                        empty = False
                        break
                if empty:
                    possibleLocations.append((column, row + 2))

            # Check for kill moves
            for offset in [-1, 1]:
                target_row = row + 1
                target_column = column + offset
                for piece in self.board:
                    if piece.location == (target_column, target_row) and piece.white != self.white:
                        possibleLocations.append((target_column, target_row))
                        break

        return possibleLocations

    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)
        else:
            print(f"Invalid move for Pawn to {location}")
