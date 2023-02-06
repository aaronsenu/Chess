import pygame
from const import *
from board import Board
from dragger import Dragger
from square import Square
from DoublyLinkedList import *

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.hovered_sqr = None
        self.next_player = 'white'
        self.game_moves = DoublyLinkedList()
        self.current_move = None

    #blit methods
    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (row+col)%2 == 0:
                    color = '#EEEED2'#(234, 235, 200) #light green

                else:
                    color = '#769656'#(119,154,88) #dark green

                rect = (col*sqsize, row*sqsize, sqsize, sqsize)

                pygame.draw.rect(surface, color,  rect)

    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (self.board.squares[row][col])!=0:
                    piece = self.board.squares[row][col].piece
                    if piece != self.dragger.piece:
                        piece.set_texture()
                        img = pygame.image.load(piece.texture)
                        img_center = row * sqsize + sqsize // 2, col * sqsize + sqsize // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)


    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            if self.current_move!=None:
                 initial,final = self.current_move.data[1], self.current_move.data[2]
            else:
                initial,final = None, None
            
            for move in piece.moves:
                #empty square moves
                if (move.final.row+move.final.col) % 2 == 0:
                    if (initial,final) != (None,None):
                        if (move.final.row, move.final.col) == (initial.row, initial.col):
                            color = '#DFDF63' #light yellow
                            
                        else:
                           
                            color = '#D6D6BD' #light green
                            
                    else:
                        color = '#D6D6BD' #light green
                        
                else:
                    if (initial,final)!= (None,None):
                        if (move.final.row, move.final.col) == (initial.row, initial.col):
                            color = '#B4BF36' #dark yellow
                            
                        else:
                            color = '#6A874D' #dark green
                    else:
                        color = '#6A874D' #dark green
                

                circle_center = move.final.row * sqsize + sqsize // 2, move.final.col * sqsize + sqsize // 2

                if self.board.squares[move.final.row][move.final.col]==0:
                    radius = 17
                    thickness = 0

                #capture moves
                elif self.board.squares[move.final.row][move.final.col].has_rival_piece(self.dragger.piece.color):
                    if (move.final.col+move.final.row) % 2 == 0:
                        #if square color is yellow
                        if (move.final.row, move.final.col) == (final.row, final.col):
                            color = '#DFDF63' #light yellow 
                        else:
                             color = '#D6D6BD' #light green
                            
                    else:
                        #if square color is dark yellow
                        if (move.final.row, move.final.col) == (final.row, final.col):
                            color = '#B4BF36' #dark yellow
                        else:
                            color = '#6A874D' #dark green
                            
                    radius = 50
                    thickness = 7

                   
                pygame.draw.circle(surface, color, circle_center, radius, thickness)


                #rect = (move.final.row*sqsize, move.final.col*sqsize, sqsize, sqsize)

                #pygame.draw.rect(surface, color, rect)

            '''
            last_move = self.board.last_move
            
            
            for move in piece.moves:
                #empty square moves
                if (move.final.row+move.final.col) % 2 == 0:
                    if last_move!= None:
                        if (move.final.row, move.final.col) == (last_move.initial.row, last_move.initial.col):
                            color = '#DFDF63' #light yellow
                            
                        else:
                           
                            color = '#D6D6BD' #light green
                            
                    else:
                        color = '#D6D6BD' #light green
                        
                else:
                    if last_move!= None:
                        if (move.final.row, move.final.col) == (last_move.initial.row, last_move.initial.col):
                            color = '#B4BF36' #dark yellow
                            
                        else:
                            color = '#6A874D' #dark green
                    else:
                        color = '#6A874D' #dark green
                

                circle_center = move.final.row * sqsize + sqsize // 2, move.final.col * sqsize + sqsize // 2

                if self.board.squares[move.final.row][move.final.col]==0:
                    radius = 17
                    thickness = 0

                #capture moves
                elif self.board.squares[move.final.row][move.final.col].has_rival_piece(self.dragger.piece.color):
                    if (move.final.col+move.final.row) % 2 == 0:
                        #if square color is yellow
                        if (move.final.row, move.final.col) == (last_move.final.row, last_move.final.col):
                            color = '#DFDF63' #light yellow 
                        else:
                             color = '#D6D6BD' #light green
                            
                    else:
                        #if square color is dark yellow
                        if (move.final.row, move.final.col) == (last_move.final.row, last_move.final.col):
                            color = '#B4BF36' #dark yellow
                        else:
                            color = '#6A874D' #dark green
                            
                    radius = 50
                    thickness = 7

                   
                pygame.draw.circle(surface, color, circle_center, radius, thickness)


                #rect = (move.final.row*sqsize, move.final.col*sqsize, sqsize, sqsize)

                #pygame.draw.rect(surface, color, rect)
                '''

    def show_last_move(self, surface):
        if self.current_move != None:
            initial,final = self.current_move.data[1], self.current_move.data[2]
            if (initial.row+initial.col) % 2 == 0:
                color = '#F8F86E' #light yellow
            else:
                color = '#C8D53C' #dark yellow
                
            if (final.row+final.col) % 2 == 0 :
                color2 = '#F8F86E' #light yellow
            else:
                color2 = '#C8D53C' #dark yellow

            #initial square
            rect = (initial.row*sqsize, initial.col*sqsize, sqsize, sqsize)
            pygame.draw.rect(surface, color, rect)
            #final square
            rect2 = (final.row*sqsize, final.col*sqsize, sqsize, sqsize)
            pygame.draw.rect(surface, color2, rect2)
            
        '''
        last_move = self.board.last_move     
        if last_move!=None:
            if (last_move.initial.row+last_move.initial.col) % 2 == 0:
                color = '#F8F86E' #light yellow
            else:
                color = '#C8D53C' #dark yellow
                
            if (last_move.final.row+last_move.final.col) % 2 == 0 :
                color2 = '#F8F86E' #light yellow
            else:
                color2 = '#C8D53C' #dark yellow

           

            

            #initial square
            rect = (last_move.initial.row*sqsize, last_move.initial.col*sqsize, sqsize, sqsize)
            pygame.draw.rect(surface, color, rect)
            #final square
            rect2 = (last_move.final.row*sqsize, last_move.final.col*sqsize, sqsize, sqsize)
            pygame.draw.rect(surface, color2, rect2)
            '''
        
    def show_selected_piece(self, surface):
        #color = '#D6D6BD' #light green
        row,col = self.dragger.initial_row, self.dragger.initial_col
        
        if (row,col)!=(None,None):        
            
            if (self.board.squares[row][col])!=0:
                if (row+col) % 2 == 0:
                    color = '#F8F86E'
                else:
                    color = '#C8D53C'
                rect = (row*sqsize, col*sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rect)



    def show_hover(self, surface):
        
        if self.board.promote_pawn:
            
            color = (180,180,180)
            rect = (self.hovered_sqr.row*sqsize, self.hovered_sqr.col*sqsize, sqsize, sqsize)
            pygame.draw.rect(surface, color, rect, width = 3)
            
        else:
            if self.dragger.dragging:
                if self.hovered_sqr != None:
                    if (self.hovered_sqr.row + self.hovered_sqr.col) % 2 == 0:
                        color = '#F9F9EF' #light green square hover color
                    else:
                        color = '#CFDAC4' #dark green square hover color
                    rect = (self.hovered_sqr.row*sqsize, self.hovered_sqr.col*sqsize, sqsize, sqsize)
                    pygame.draw.rect(surface, color, rect, width = 5)

    def show_cursor(self):
        if self.hovered_sqr!= None:
            if self.board.squares[self.hovered_sqr.row][self.hovered_sqr.col]!=0 or self.dragger.dragging:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                 pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            
    def next_turn(self):
        if self.next_player == 'black':
            self.next_player = 'white'
        else:
            self.next_player = 'black'


    
    def set_hover(self, row, col):
        self.hovered_sqr = Square(row,col)
            
    
    def reset(self):
        self.__init__()
