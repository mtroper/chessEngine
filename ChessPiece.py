
#notes:

#pawn, rook, should extend this class

#this is going to serve as a blueprint class for pawn, rook, etc.

import math
from abc import ABC, abstractmethod

class ChessPiece(ABC):
     def __init__(self, color, current_square, is_alive=True):
          # True for white, False for black
          self.color = color

          # current_square is a Square object 
          self.current_square = current_square


     def isTaken():
          self.isAlive = False


     @abstractmethod
     def validMove(target_square):
          # each piece that extends this class will have its own unique (validMove)
          # these are the essentially the rules for the game
          
     
     def move(target_square):
          if validMove(target_square):
               #if there is a piece on target_square
               if target_square.piece:
                    #if that piece is the opposite color
                    if target_square.piece.color != self.color:
                         #set that piece to taken
                         target_square.piece.color.isTaken()

                         #output move to console
                         print("Pawn " + self.current_square + " to " + target_square)

                         #set new position
                         self.current_square = target_square
                         return True
                    else:
                         #if that piece is the same, return False, move is invalid
                         print("invalid move")
                         return False
          else:
               print("invalid move")
               return False