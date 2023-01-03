import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

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

            for move in piece.moves:
                if (move.final.col+move.final.row) % 2 == 0 :
                    color = '#D6D6BD' #ED1C24 #light green
                else:
                    color = '#6A874D' #ED1C24 #dark green

                circle_center = move.final.row * sqsize + sqsize // 2, move.final.col * sqsize + sqsize // 2

                if self.board.squares[move.final.row][move.final.col]==0:
                    radius = 17
                    thickness = 0

                elif self.board.squares[move.final.row][move.final.col].has_rival_piece(self.dragger.piece.color):
                    radius = 50
                    thickness = 7

                   
                pygame.draw.circle(surface, color, circle_center, radius, thickness)


                #rect = (move.final.row*sqsize, move.final.col*sqsize, sqsize, sqsize)

                #pygame.draw.rect(surface, color, rect)

            
