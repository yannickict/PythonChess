from Pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, location, white, board):
        super().__init__(location, white, board)
        self.name = "Pawn"

    def showMoves(self):
        x, y = self.location
        possibleLocations = []

        if self.white:
            # Check one square ahead
            if y + 1 <= 7:
                has_piece = False
                for piece in self.board:
                    if piece.location == (x, y + 1):
                        has_piece = True
                        break
                if not has_piece:
                    possibleLocations.append((x, y + 1))

            # Check two squares ahead from starting position
            if y == 1:
                empty = True
                for piece in self.board:
                    if piece.location == (x, y + 2) or piece.location == (x, y + 1):
                        empty = False
                        break
                if empty:
                    possibleLocations.append((x, y + 2))

            # Check for kill moves
            for offset in [-1, 1]:
                target_row = y + 1
                target_column = x + offset
                if 0 <= target_column <= 7 and 0 <= target_row <= 7:  # Ensure the target is within the board
                    for piece in self.board:
                        if piece.location == (target_column, target_row) and piece.white != self.white:
                            possibleLocations.append((target_column, target_row))
                            break
            

        else:
            if y - 1 >= 0:
                has_piece = False
                for piece in self.board:
                    if piece.location == (x, y - 1):
                        has_piece = True
                        break
                if not has_piece:
                    possibleLocations.append((x, y - 1))

            # Check two squares ahead from starting position
            if y == 6:
                empty = True
                for piece in self.board:
                    if piece.location == (x, y - 2) or piece.location == (x, y - 1):
                        empty = False
                        break
                if empty:
                    possibleLocations.append((x, y - 2))

            # Check for kill moves
            for offset in [-1, 1]:
                target_row = y - 1
                target_column = x + offset
                if 0 <= target_column <= 7 and 0 <= target_row <= 7:  # Ensure the target is within the board
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
