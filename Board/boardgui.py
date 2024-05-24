import wx
from Board.board import Board

class ChessBoard(wx.Frame):
    def __init__(self, parent, board, size=(400, 400)):
        title = 'Chess'

        super(ChessBoard, self).__init__(parent, title=title, size=size)
        self.board = board

        self.initUI()

    def initUI(self):
        panel = wx.Panel(self)

        # Create a grid sizer to hold the chessboard squares
        grid = wx.GridSizer(8, 8, 0, 0)

        # Create 64 squares for the chessboard
        for i in range(1, 9):
            for j in range(1, 9):
                square = wx.Panel(panel)
                if (i + j) % 2 == 0:
                    square.SetBackgroundColour(wx.Colour(240, 217, 181))  # Light color for white squares
                else:
                    square.SetBackgroundColour(wx.Colour(181, 136, 99))   # Dark color for black squares
                grid.Add(square, 0, wx.EXPAND)

                for piece in self.board.board:
                    if piece.location == (j, i):
                        if piece.name == 'King':
                            square.SetBackgroundColour(wx.Colour(255, 0, 0))
                        elif piece.name == 'Queen':
                            square.SetBackgroundColour(wx.Colour(0, 255, 0))
                        elif piece.name == 'Rook':
                            square.SetBackgroundColour(wx.Colour(255, 255, 0))
                        elif piece.name == 'Bishop':
                            square.SetBackgroundColour(wx.Colour(0, 0, 255))
                        elif piece.name == 'Knight':
                            square.SetBackgroundColour(wx.Colour(255, 0, 255))
                        elif piece.name == 'Pawn':
                            square.SetBackgroundColour(wx.Colour(0, 0, 0))

        panel.SetSizer(grid)
        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()

    # Example: Create a board instance (assuming you have a Board class)
    board = Board()
    
    # Create ChessBoard instance with custom size and the board object
    frame = ChessBoard(None, board, size=(500, 500))
    
    frame.Show()
    app.MainLoop()
