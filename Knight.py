
import math

class Knight():
     def  __init__(self, color, position):
          # True for white, False for black
          self.color = color

          # position is a tuple (row,col)
          self.position = position

     def getClass(self):
          return("Knight")


     #returns list of valid moves (row, col)
     def moves(self):
          tempValidMoves = []
          (row,col) = self.position
          
          tempValidMoves.append( (row-2,col-1) )
          tempValidMoves.append( (row-1,col-2) )
          tempValidMoves.append( (row+1,col-2) )
          tempValidMoves.append( (row+2,col-1) )
          tempValidMoves.append( (row-2,col+1) )
          tempValidMoves.append( (row-1,col+2) )
          tempValidMoves.append( (row+1,col+2) )
          tempValidMoves.append( (row+2,col+1) )


          validMoves = []
          for pos in tempValidMoves:
               if pos[0] > 7 or pos[0] < 0 or pos[1] > 7 or pos[1] < 0:
                    continue
               else:
                    validMoves.append(pos)

          return validMoves


#      0     -  -  -  -  -  -  -  -,
#      1     -  *  -  *  -  -  -  -,
#      2     *  -  -  -  *  -  -  -,
#      3     -  -  o  -  -  -  -  -,
#      4     *  -  -  -  *  -  -  -,
#      5     -  *  -  *  -  -  -  -,
#      6     -  -  -  -  -  -  -  -,
#      7     -  -  -  -  -  -  -  -

#            0  1  2  3  4  5  6  7

#     (3,2)
#     (1,1)(2,0)(4,0)(5,1)(1,3)(2,4)(4,4)(5,3)