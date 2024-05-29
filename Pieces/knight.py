from Pieces.piece import Piece

class Knight(Piece):
    def __init__(self, location, white, board, boardObject):
        super().__init__(location, white, board, boardObject)
        self.name = "Knight"

    def showMoves(self):
        column, row = self.location
        possibleLocations = []

        # Define all possible knight moves
        move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for offset in move_offsets:
            new_column = column + offset[0]
            new_row = row + offset[1]

            if 0 <= new_column < 8 and 0 <= new_row < 8:
                move_valid = True
                for piece in self.board:
                    if piece.location == (new_column, new_row):
                        if piece.white == self.white:
                            move_valid = False  # Block move if friendly piece is there
                        break

                if move_valid:
                    possibleLocations.append((new_column, new_row))

        return possibleLocations

    def move(self, location):
        possibleLocations = self.showMoves()

        if location in possibleLocations:
            super().move(location)
        else:
            print(f"Invalid move for Knight to {location}")
