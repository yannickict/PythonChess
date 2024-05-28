import os
import wx
from Board.board import Board

# Get the directory path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, '..', 'Images')

class ChessBoard(wx.Frame):
    def __init__(self, parent, board):
        size = (560, 560)
        title = 'Chess'

        super(ChessBoard, self).__init__(parent, title=title, size=size)
        self.board = board
        self.highlighted_squares = []

        self.initUI()

    def onPieceClick(self, piece):
        # Reset the background color of previously highlighted squares
        self.resetHighlights()
        moves = piece.showMoves()
        print(moves)
        self.highlightMoves(moves)

    def resetHighlights(self):
        for square in self.highlighted_squares:
            square.SetBackgroundColour(square.original_color)
        self.highlighted_squares = []

    def highlightMoves(self, moves):
        for move in moves:
            x, y = move
            square = self.squares[7 - y][x]
            square.SetBackgroundColour(wx.Colour(255, 0, 0))  # Highlight color
            self.highlighted_squares.append(square)
        self.Refresh()

    def initUI(self):
        panel = wx.Panel(self)

        # Create a grid sizer to hold the chessboard squares
        grid = wx.GridSizer(8, 8, 0, 0)

        # Create 64 squares for the chessboard
        self.squares = []
        for y in range(8):
            row = []
            for x in range(8):
                square = wx.Panel(panel)
                color = wx.Colour(240, 217, 181) if (y + x) % 2 == 0 else wx.Colour(181, 136, 99)
                square.SetBackgroundColour(color)
                square.original_color = color
                grid.Add(square, 0, wx.EXPAND)

                row.append(square)
            self.squares.append(row)

        for piece in self.board:
            if piece.location:
                x, y = piece.location
                square = self.squares[7 - y][x]  # Adjusted for 0-based index and grid layout
                image_path = os.path.join(images_dir, f"{piece.name}{'White' if piece.white else 'Black'}.png")
                if os.path.exists(image_path):
                    piece_image = wx.Image(image_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                    bitmap = wx.StaticBitmap(square, wx.ID_ANY, piece_image)
                    bitmap.Bind(wx.EVT_LEFT_DOWN, lambda event, p=piece: self.onPieceClick(p))

        panel.SetSizer(grid)
        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()

    # Example: Create a board instance (assuming you have a Board class)
    board = Board()
    
    # Create ChessBoard instance with custom size and the board object
    frame = ChessBoard(None, board)
    
    frame.Show()
    app.MainLoop()
