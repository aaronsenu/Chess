from const import *
from square import Square
from piece import *



class Board:

    def __init__(self):
       self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)]
       self.add_pieces("white")
       self.add_pieces("black")

    def calc_moves(self, piece, row, col):
        def knight_moves():
            possible_moves = [
                (row-2, col+1),
                (row-2, col-1),
                (row-1, col+2),
                (row-1, col-2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col+2),
                (row+1, col-2)
                ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    
                    
                    #if self.squares[possible_move_col][possible_move_row]== 0 or (self.squares[possible_move_col][possible_move_row].isEmpty_or_rival(piece.color)):#self.squares[possible_move_col][possible_move_row].isEmpty_or_rival(piece.color):# and self.squares[possible_move_col][possible_move_row].piece.color!= piece.color):
                    #initial = Square(row, col)
                    
                    if self.squares[possible_move_row][possible_move_col]==0 or self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        
                        final = Square(possible_move_row, possible_move_col)
                                

                        move = Move(final)#initial, final)
                        piece.add_moves(move)
                        
        
        if piece.name == 'pawn':
            pass
        elif piece.name == 'knight':
            knight_moves()
            
        elif piece.name == 'bishop':
            pass
        elif piece.name == 'rook':
            pass
        elif piece.name == 'queen':
            pass
        elif piece.name == 'king':
            pass
        
        
        
        

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

      
            
            

