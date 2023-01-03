
import pygame, sys
from const import *
from game import Game
from square import Square
from piece import *

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        board = self.game.board
        
        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)
            #click
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
    
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseX // sqsize
                    clicked_col = dragger.mouseY // sqsize

                    print(clicked_row, clicked_col)
                    #print(board.squares[clicked_row][clicked_col].piece.name)
                   

                    if board.squares[clicked_row][clicked_col]!=0:
                        piece = board.squares[clicked_row][clicked_col].piece
                        print(piece.name)
                        board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_inital(event.pos)
                        dragger.drag_piece(piece)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                    
                        

                    


                    
                    #piece = board.squares[clicked_row][clicked_row]
                        
                elif event.type == pygame.MOUSEMOTION:
                    #if dragger.dragging:
                    dragger.update_mouse(event.pos)
                       # dragger.update_blit(screen)


                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    #dragger.undrag_piece()
                    #board.squares[clicked_row][clicked_col] = dragger.mouseX, dragger.mouseY
                                        
                    clicked_row = dragger.mouseX // sqsize
                    clicked_col = dragger.mouseY // sqsize
                    #print(dragger.initial_col, dragger.initial_row)
                   
                   
                    board.squares[dragger.initial_col][dragger.initial_row] = 0
                
                   
                    board.squares[clicked_row][clicked_col] = Square(clicked_col, clicked_row, piece)
                    dragger.piece.moves.clear()
                    
                    dragger.undrag_piece()
                    
                    
                    
                    
                    

                
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.mainloop()
