from const import *
from square import Square
from piece import *
from move import Move


class Board:

    def __init__(self):
       self.squares = [[0,0,0,0,0,0,0,0] for col in range(cols)]
       self.add_pieces("white")
       self.add_pieces("black")

    def calc_moves(self, piece, row, col):
        '''
        method for pieces that move in a straightline
        #moves_list: list of movable directions
        #row,col: row & col the piece is currently on
        #move_row, move_col: one of the 4 tuples from possible_moves
        #length: length of possible_moves used as a depth recursion counter
        #index: index of moves_list starting at index 1
        '''
        def straightline_move(moves_list, row, col, move_row, move_col, length, index):
            #base case
            if length == 1: 
                return
            
            else:                    
                const_row = move_row
                const_col = move_col

                possible_move_row, possible_move_col = row+move_row, col+move_col
                
                while True:
                    #checks if posssible square is within board range
                    if Square.in_range(possible_move_row, possible_move_col):
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(final)#initial, final)

                        #checks if square is empty
                        if self.squares[possible_move_row][possible_move_col]==0:
                            piece.add_moves(move) #adds square to piece moves
                            
                        #checks if square has an enemy piece
                        elif self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            piece.add_moves(move) #adds square to piece moves
                            move_row, move_col = moves_list[index][0], moves_list[index][1] #changes move direction by incrementing moves_list
                            straightline_move(moves_list,row, col, move_row, move_col,length-1, index+1) #recursively calls method with new dir and a decremented depth recursion counter
                            break 

                        #checks if square has a team piece
                        elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            move_row, move_col = moves_list[index][0], moves_list[index][1] #changes move direction by incrementing moves_list
                            straightline_move(moves_list, row, col, move_row, move_col,length-1, index+1) #recursively calls method with new dir and a decremented depth recursion counter
                            break

                        possible_move_row += const_row #increments and changes current row by move_dir (row)
                        possible_move_col += const_col #increments and changes current col by move_dir (col)
                    
                    #if possible square isnt within board range    
                    else:
                        move_row, move_col = moves_list[index][0], moves_list[index][1] #change move dir by incrementing moves_list
                        straightline_move(moves_list, row, col, move_row, move_col,length-1, index+1) #recursively calls method with new dir and a decremented depth recursion counter
                        break

        '''
        method that moves in a specified step pattern
        #possible_moves_list: list of possible moves
        '''
        def step_moves(possible_moves_list):
            for possible_move in possible_moves_list:
                possible_move_row, possible_move_col = possible_move
                #checks if possible square is within board range
                if Square.in_range(possible_move_row, possible_move_col):
                    #checks if square is empty or if square has an enemy piece
                    if self.squares[possible_move_row][possible_move_col]==0 or self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        #initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(final)#initial, final)
                        piece.add_moves(move) #adds square to piece moves
            
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
            step_moves(possible_moves)

            


        def bishop_moves():
            moves_dir = [(1,1), (-1,1), (-1,-1), (1,-1),(0,0)] #(0,0) to avoid index out of range error
            #bottom_right = 1,1, bottom_left = -1,1, top_left = -1,-1, top_right = 1,-1
            index = 1
            straightline_move(moves_dir, row, col, moves_dir[0][0], moves_dir[0][1], len(moves_dir), index)

        def rook_moves():
            moves_dir = [(0,-1),(0,1),(1,0),(-1,0),(0,0)]
            #up = 0,-1, down = 0,1, right = 1,0, left = -1,0
            index = 1
            straightline_move(moves_dir, row, col, moves_dir[0][0], moves_dir[0][1], len(moves_dir), index)

        def queen_moves():
            bishop_moves()
            rook_moves()

        def king_moves():
            possible_moves = [(row, col-1), (row, col+1), (row+1, col), (row-1,col), (row+1,col+1), (row-1,col+1), (row-1,col-1), (row+1,col-1)]
            #up = 0,-1, down = 0,1, right = 1,0, left = -1,0, bottom_right = 1,1, bottom_left = -1,1, top_left = -1,-1, top_right = 1,-1
            step_moves(possible_moves)

        if piece.name == 'pawn':
            pass
        elif piece.name == 'knight':
            knight_moves()
            
        elif piece.name == 'bishop':
            bishop_moves()
            
        elif piece.name == 'rook':
            rook_moves()
        elif piece.name == 'queen':
            queen_moves()
        elif piece.name == 'king':
            king_moves()

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
        

        #Bishops
        self.squares[2][row_other] = Square(row_other, 2, Bishop(color))
        self.squares[5][row_other] = Square(row_other, 5, Bishop(color))

        #Queen
        self.squares[3][row_other] = Square(row_other, 3, Queen(color))
           
        #King
        self.squares[4][row_other] = Square(row_other, 0, King(color))

      
            
            

