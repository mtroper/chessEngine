
import math

class Rook():
     def  __init__(self, color, position):
          # True for white, False for black
          self.color = color

          # position is a tuple (row,col)
          self.position = position

     def getClass(self):
          return("Rook")

     #returns list of valid moves (row, col)
     def moves(self):
          validMoves = []
          (row,col) = self.position
          
          #horizontal
          for i in range(0,8):
               if i != col:
                    validMoves.append( (row,i) )
          #vertical
          for i in range(0,8):
               if i != row:
                    validMoves.append( (i,col) )
          
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