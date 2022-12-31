from const import *
from square import Square
from piece import *



class Board:

    def __init__(self):
       self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)]
       self.add_pieces("white")
       self.add_pieces("black")

    
        
        
        
        

    def add_pieces(self,color):
        if color == 'white':
            row_pawn, row_other = 6,7
        else:
            row_pawn, row_other = 1,0


        #Pawns
        for col in range(cols):
            self.squares[col][row_pawn] = Square(row_pawn, col, Pawn(color))

        #Rooks
        self.squares[0][row_other] = Square(row_other, 0, Rook(color))
        self.squares[7][row_other] = Square(row_other, 7, Rook(color))

        #Knights
        self.squares[1][row_other] = Square(row_other, 1, Knight(color))
        self.squares[6][row_other] = Square(row_other, 6, Knight(color))
        #self.squares[3][3] = Square(3, 3, Knight(color))
        #self.squares[4][4] = Square(4,4, Knight(color))

        #Bishops
        self.squares[2][row_other] = Square(row_other, 2, Bishop(color))
        self.squares[5][row_other] = Square(row_other, 5, Bishop(color))

        #Queen
        self.squares[3][row_other] = Square(row_other, 3, Queen(color))
           
        #King
        self.squares[4][row_other] = Square(row_other, 0, King(color))

      
            
            

