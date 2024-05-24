class Piece:
    def __init__(self, location, white, board):
        self.location = location
        self.alive = True
        self.white = white
        self.board = board

    def die(self):
        self.board.remove_piece(self)
        self.alive = False

    def move(self, location):
        for piece in self.board:
            if piece.location == location and piece.white != self.white:
                piece.die()
        self.location = location