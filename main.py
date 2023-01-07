import pygame, sys
from const import *
from game import Game
from square import Square
from piece import *
from move import Move
from promotion_button import Button

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Chess")
        self.game = Game()
        #w_queen_img = pygame.image.load("images/imgs-80px/white_queen.png")
        #w_queen_button = button.Button(100,100,w_queen_img, 1)
    def mainloop(self):
        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        board = self.game.board
        #white_queen = Button(screen,"white_queen", sqsize,sqsize, (100,450))
        #white_knight = Button(screen,"white_knight", sqsize,sqsize, (200,450))
        #white_rook = Button(screen,"white_rook", sqsize,sqsize, (300,450))
        #white_bishop = Button(screen,"white_bishop", sqsize,sqsize, (400,450))
        while True:
            
            game.show_bg(screen)
            game.show_selected_piece(screen)
            game.show_last_move(screen)
            
            game.show_pieces(screen)
            game.show_moves(screen)
            #white_queen.draw()
            #white_queen.select_piece()
            #white_knight.draw()
            #white_knight.select_piece()
            #white_rook.draw()
            #white_rook.select_piece()
            #white_bishop.draw()
            #white_bishop.select_piece()

            if board.promote_pawn:
                board.squares[board.pawn_row][board.pawn_col] = 0
                queen = Button(screen,"{}_queen".format(board.pawn_color), sqsize,sqsize, (board.pawn_row*sqsize,board.pawn_col*sqsize))
                knight = Button(screen,"{}_knight".format(board.pawn_color), sqsize,sqsize, (board.pawn_row*sqsize,(board.pawn_col+(1*board.dir))*sqsize))
                rook = Button(screen,"{}_rook".format(board.pawn_color), sqsize,sqsize, (board.pawn_row*sqsize,(board.pawn_col+(2*board.dir))*sqsize))
                bishop = Button(screen,"{}_bishop".format(board.pawn_color), sqsize,sqsize, (board.pawn_row*sqsize,(board.pawn_col+(3*board.dir))*sqsize))

                queen.draw()
                knight.draw()
                rook.draw()
                bishop.draw()
                
                if queen.select_piece():
                    board.promote_pawn = False
                    board.squares[board.pawn_row][board.pawn_col] = Square(board.pawn_row, board.pawn_col, Queen(board.pawn_color))

                elif knight.select_piece():
                    board.promote_pawn = False
                    board.squares[board.pawn_row][board.pawn_col] = Square(board.pawn_row, board.pawn_col, Knight(board.pawn_color))

                elif rook.select_piece():
                    board.promote_pawn = False
                    board.squares[board.pawn_row][board.pawn_col] = Square(board.pawn_row, board.pawn_col, Rook(board.pawn_color))

                elif bishop.select_piece():
                    board.promote_pawn = False
                    board.squares[board.pawn_row][board.pawn_col] = Square(board.pawn_row, board.pawn_col, Bishop(board.pawn_color))
                    
                    
            if dragger.dragging:
                dragger.update_blit(screen)
     
            #click
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        dragger = self.game.dragger
                        board = self.game.board
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
    
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
                        #game.show_bg(screen)
                        #game.show_moves(screen)
                        #game.show_pieces(screen)

                    
                        

                    


                    
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
                   
                    
                    #board.squares[dragger.initial_col][dragger.initial_row] = 0
                
                   
                    #board.squares[clicked_row][clicked_col] = Square(clicked_row, clicked_col, piece)
                    #dragger.piece.moves.clear()
                    #if board.squares[dragger.initial_col][dragger.initial_row] == 0:
                     #   dragger.piece.moved = True
                    #print(dragger.piece.moved)

                    
                        
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseX // sqsize
                        released_col = dragger.mouseY // sqsize
                        
                       

                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)
                        

                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece, move)

                            #game.show_bg(screen)
                            #game.show_pieces(screen)
                            
                    if board.squares[clicked_row][clicked_col]!=0:
                        try:
                            dragger.piece.moves.clear()
                        except:
                            pass
                    else:
                        pass
                    dragger.undrag_piece()
                    
                    
                        
                

                
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.mainloop()
