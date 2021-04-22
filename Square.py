
class Square:
     def __init__(self, position, piece):
          # a tuple, (0,0) for the bottom leftmost square
          self.position = position

          # a ChessPiece object, piece=None if there is no piece occupying square
          self.piece = piece