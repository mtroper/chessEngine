
import math

class Queen():
     def  __init__(self, color, position):
          # True for white, False for black
          self.color = color

          # position is a tuple (row,col)
          self.position = position


     def getClass(self):
          return("Queen")

     #returns list of valid moves (row, col)
     def moves(self):
          validMoves = []
          (row,col) = self.position
          
          #Bishop
          i = 1
          while(row + i < 8 and col - i >= 0):
               validMoves.append( (row + i, col - i) )
               i += 1
          i = 1
          while(row + i < 8 and col + i < 8):
               validMoves.append( (row + i, col + i) )
               i += 1
          i = 1
          while(row - i >= 0 and col - i >= 0):
               validMoves.append( (row - i, col - i) )
               i += 1
          i = 1
          while(row - i >= 0 and col + i < 8):
               validMoves.append( (row - i, col + i) )
               i += 1
          
          #Rook
          #horizontal
          for i in range(0,8):
               if i != col:
                    validMoves.append( (row,i) )
          #vertical
          for i in range(0,8):
               if i != row:
                    validMoves.append( (i,col) )

          return validMoves