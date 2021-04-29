
import math
from abc import ABC, abstractmethod

# (sketchy)
from ChessPiece.py import ChessPiece

# Pawn extends Chesspiece abstract class
class Pawn(ChessPiece):
     
     #overriding abstract method validMove
     def validMove(target_square):
          #rules for Pawn move

