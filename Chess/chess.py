from Board.board import Board
from Board.boardgui import ChessBoard

import wx

board = Board()
app = wx.App()
frame = wx.Frame(None, size=(400, 400))
ChessBoard(frame, board)
app.MainLoop()