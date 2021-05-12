
import math

class Pawn():
     def  __init__(self, color, position):
          # True for white, False for black
          self.color = color

          # position is a tuple (row,col)
          self.position = position


     def getClass(self):
          return("Pawn")

     #returns list of valid moves (row, col)
     #does include moves where pawn will eat
     def moves(self):
          validMoves = []
          (row,col) = self.position

          
          if row < 7:
               if self.color == "white":
                    validMoves.append( (row-1,col) )
                    validMoves.append( (row-1,col) )
                    if col < 7:
                         validMoves.append( (row-1, col+1) )
                    if col > 0:
                         validMoves.append( (row-1, col-1) )

               else:
                    validMoves.append( (row+1,col) )
                    if col < 7:
                         validMoves.append( (row+1, col+1) )
                    if col > 0:
                         validMoves.append( (row+1, col-1) )
          
          return validMoves



#      7     -  -  -  -  -  -  -  -,
#      6     -  -  -  -  -  -  -  -,
#      5     -  -  -  -  -  -  -  -,
#      4     -  -  *  -  -  -  -  -,
#      3     -  -  -  -  -  -  -  -,
#      2     -  -  -  -  -  -  -  -,
#      1     -  -  -  -  -  -  -  -,
#      0     -  -  -  -  -  -  -  -

#            0  1  2  3  4  5  6  7