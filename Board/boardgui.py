import os
import wx
from Board.board import Board

# Get the directory path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, '..', 'Images')

class ChessBoard(wx.Frame):
    def __init__(self, parent, board):
        size=(560, 560)
        title = 'Chess'

        super(ChessBoard, self).__init__(parent, title=title, size=size)
        self.board = board

        self.initUI()

    def onPieceClick(self, piece):
        moves = piece.showMoves()
        print(moves)

    def initUI(self):
        panel = wx.Panel(self)

        # Create a grid sizer to hold the chessboard squares
        grid = wx.GridSizer(8, 8, 0, 0)

        # Create 64 squares for the chessboard
        for i in range(1, 9):
            for j in range(1, 9):
                square = wx.Panel(panel)
                if (i + j) % 2 == 0:
                    square.SetBackgroundColour(wx.Colour(240, 217, 181))
                else:
                    square.SetBackgroundColour(wx.Colour(181, 136, 99))
                grid.Add(square, 0, wx.EXPAND)

                for piece in self.board:
                    if piece.location == (j, i):
                        image_path = os.path.join(images_dir, f"{piece.name}{'White' if piece.white else 'Black'}.png")
                        if os.path.exists(image_path):
                            piece_image = wx.Image(image_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                            # Create wx.StaticBitmap and add it to the square
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
    frame = ChessBoard(None, board, size=(550, 550))
    
    frame.Show()
    app.MainLoop()
