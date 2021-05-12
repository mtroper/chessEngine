
import math

class King():
     def  __init__(self, color, position):
          # True for white, False for black
          self.color = color

          # position is a tuple (row,col)
          self.position = position


     def getClass(self):
          return("King")


     #returns list of valid moves (row, col)
     def moves(self):
          tempValidMoves = []
          (row,col) = self.position

          tempValidMoves.append( (row,col-1) )
          tempValidMoves.append( (row,col+1) )
          tempValidMoves.append( (row+1,col) )
          tempValidMoves.append( (row-1,col) )
          tempValidMoves.append( (row+1,col-1) )
          tempValidMoves.append( (row+1,col+1) )
          tempValidMoves.append( (row-1,col-1) )
          tempValidMoves.append( (row-1,col+1) )

          validMoves = []
          for pos in tempValidMoves:
               if pos[0] > 7 or pos[0] < 0 or pos[1] > 7 or pos[1] < 0:
                    continue
               else:
                    validMoves.append(pos)

          return validMoves