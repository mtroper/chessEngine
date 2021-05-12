
import math

class Bishop():
     def  __init__(self, color, position):
          # True for white, False for black
          self.color = color

          # position is a tuple (row,col)
          self.position = position

     def getClass(self):
          return("Bishop")


     #returns list of valid moves (row, col)
     def moves(self):
          validMoves = []
          (row,col) = self.position

          #bottom left
          i = 1
          while(row + i < 8 and col - i >= 0):
               validMoves.append( (row + i, col - i) )
               i += 1
          #bottom right
          i = 1
          while(row + i < 8 and col + i < 8):
               validMoves.append( (row + i, col + i) )
               i += 1
          #upper left
          i = 1
          while(row - i >= 0 and col - i >= 0):
               validMoves.append( (row - i, col - i) )
               i += 1
          #upper right
          i = 1
          while(row - i >= 0 and col + i < 8):
               validMoves.append( (row - i, col + i) )
               i += 1

          return validMoves