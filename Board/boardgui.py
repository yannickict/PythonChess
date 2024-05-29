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
        self.selected_piece = None
        self.highlighted_squares = []

        self.initUI()

    def onPieceClick(self, piece):
        if piece.square.selectedBy:
            p = piece.square.selectedBy
            p.move(piece.location)
            self.selected_piece = None
            self.board.whiteToMove = not self.board.whiteToMove
            self.refreshBoard()
            self.resetHighlights()
            self.selected_piece = None
            return
        # Reset the background color of previously highlighted squares
        if self.board.whiteToMove != piece.white:
            return
        self.selected_piece = piece
        self.resetHighlights()
        moves = piece.showMoves()
        self.highlightMoves(moves, piece)

    def onSquareClick(self, event):
        if self.selected_piece:
            square = event.GetEventObject()
            x, y = square.position
            if square.selectedBy:
                self.selected_piece.move((x, 7 - y))
                self.board.whiteToMove = not self.board.whiteToMove 
                self.refreshBoard()
                self.resetHighlights()
                self.selected_piece = None
            else:
                self.resetHighlights()

    def resetHighlights(self):
        for square in self.highlighted_squares:
            square.SetBackgroundColour(square.original_color)
            square.selectedBy = None
        self.highlighted_squares = []
        self.Refresh()

    def highlightMoves(self, moves, piece):
        for move in moves:
            x, y = move
            square = self.squares[7 - y][x]
            square.SetBackgroundColour(wx.Colour(255, 0, 0))  # Highlight color
            square.selectedBy = piece
            self.highlighted_squares.append(square)
        self.Refresh()

    def refreshBoard(self):
        # Clear all squares
        for row in self.squares:
            for square in row:
                square.DestroyChildren()
        
        # Place pieces on their new locations
        for piece in self.board.board:
            if piece.location:
                x, y = piece.location
                square = self.squares[7 - y][x]
                piece.square = square
                image_path = os.path.join(images_dir, f"{piece.name}{'White' if piece.white else 'Black'}.png")
                if os.path.exists(image_path):
                    piece_image = wx.Image(image_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                    bitmap = wx.StaticBitmap(square, wx.ID_ANY, piece_image)
                    bitmap.Bind(wx.EVT_LEFT_DOWN, lambda event, p=piece: self.onPieceClick(p))
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
                square.selectedBy = None
                square.position = (x, y)  # Store position for easy access
                square.Bind(wx.EVT_LEFT_DOWN, self.onSquareClick)
                grid.Add(square, 0, wx.EXPAND)

                row.append(square)
            self.squares.append(row)

        # Initial placement of pieces
        self.refreshBoard()

        panel.SetSizer(grid)
        self.Centre()
        self.Show()
