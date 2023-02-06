import pygame, sys
from const import *
from game import Game
from square import Square
from piece import *
from move import Move
from DoublyLinkedList import *
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
        dragger = game.dragger#self.game.dragger
        board = self.game.board
        row_name = {0:"a", 1: "b", 2:"c" ,3:"d", 4:"e" ,5:"f", 6:"g", 7:"h"}
        while True:
            
            game.show_bg(screen)
        
            game.show_selected_piece(screen)
            game.show_last_move(screen)
            
            game.show_hover(screen)
        
            game.show_pieces(screen)
            game.show_moves(screen)
            game.show_cursor()
            
            

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
                game.show_hover(screen)
                
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
                        dragger = game.dragger
                        board = self.game.board

                    #TRAVERSE THROUGH MOVES
                    
                    
                    elif event.key == pygame.K_LEFT:
                        
                        
                        if game.current_move!=None:
                            piece, initial, final, captured = game.current_move.data[0], game.current_move.data[1], game.current_move.data[2], game.current_move.data[3]
                            if game.current_move == None or game.current_move.get_prev() == None:
                                piece.moved = False
                            
                            if captured:
                                captured_piece = game.current_move.data[4]
                                print("Captured: ", captured_piece.color, captured_piece.name)
                                
                                game.dragger.initial_row, game.dragger.initial_col = None, None #the previously selected piece wont show
                                last_move = Move(final,initial) #reverse order 
                                board.move(piece, last_move) 
                                board.squares[final.row][final.col] = Square(final.row, final.col, captured_piece)
                                board.squares[initial.row][initial.col] = Square(initial.row, initial.col, piece)

                                #game.current_move = game.current_move.get_prev()
                            #print(piece.color +" "+ piece.name, (initial.row,initial.col),(final.row, final.col)) 
                            else:
                                game.dragger.initial_row, game.dragger.initial_col = None, None #the previously selected piece wont show
                                last_move = Move(final,initial) #reverse order 
                                board.move(piece, last_move)
                                board.squares[initial.row][initial.col] = 0
                                board.squares[initial.row][initial.col] = Square(initial.row, initial.col, piece)


                            game.current_move = game.current_move.get_prev()
                            if game.current_move == None:
                                print("Cant go back")
                                print("len: ", game.game_moves.size)
                        
                                
                            
                    
                    
                    elif event.key == pygame.K_RIGHT:
                        
                        
                        if game.current_move!=None:
                            print("R")
                            game.current_move = game.current_move.get_next()
                            
                            piece, initial, final = game.current_move.data[0], game.current_move.data[1], game.current_move.data[2]
                            #game.dragger.initial_row, game.dragger.initial_col = None, None #the previously selected piece wont show
                            last_move = Move(initial,final)
                            board.move(piece, last_move)
                            board.squares[initial.row][initial.col] = 0
                            board.squares[final.row][final.col] = Square(final.row, final.col, piece)
                            
                            print(piece.color +" "+ piece.name, (initial.row,initial.col),(final.row, final.col))

                            game.current_move = game.current_move.get_next()
                            if game.current_move == None:
                                print("Cant go forward")
                                print("len: ", game.game_moves.size)
                        
                    
                    
                        

                    '''
                    elif event.key == pygame.K_LEFT:
                        
                        if current!=None:
                            print("L")
                            piece, initial, final = current.data[0], current.data[1], current.data[2]
                            
                            board.squares[final.row][final.col] = 0
                            board.squares[initial.row][initial.col] = Square(initial.row, initial.col, piece)
                            
                            print(piece.color +" "+ piece.name, (initial.row,initial.col),(final.row, final.col))
                            current = current.get_prev()
                             
                            piece.moved = False


                    elif event.key == pygame.K_RIGHT:
                        
                        if current!=None:
                            print("R")
                            piece, initial, final = current.data[0], current.data[1], current.data[2]
                            
                            board.squares[initial.row][initial.col] = 0
                            board.squares[final.row][final.col] = Square(final.row, final.col, piece)
                            
                            print(piece.color +" "+ piece.name, (initial.row,initial.col),(final.row, final.col))
                            current = current.get_next()
                            piece.moved = True
                            
                            '''
                            

    
        
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
    
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseX // sqsize
                    clicked_col = dragger.mouseY // sqsize
                   
                    #print(row_name[clicked_row], abs(clicked_col-8))
                    #print(board.squares[clicked_row][clicked_col].piece.name)
                   

                    if board.squares[clicked_row][clicked_col]!=0:
                        piece = board.squares[clicked_row][clicked_col].piece
                        #print(piece.color, piece.name)
                        
                        #board with checks
                        board.calc_moves(piece, clicked_row, clicked_col, Bool = True)
                        #if piece.color == game.next_player:
                        board.calc_moves(piece, clicked_row, clicked_col) 
                            
                        dragger.save_inital(event.pos)
                        dragger.drag_piece(piece)
                        #game.show_bg(screen)
                        #game.show_moves(screen)
                        #game.show_pieces(screen)
                    
                    #piece = board.squares[clicked_row][clicked_row]
                        
                elif event.type == pygame.MOUSEMOTION:
                    game.set_hover(pygame.mouse.get_pos()[0]//sqsize, pygame.mouse.get_pos()[1]//sqsize)
                    #game.show_hover(screen)
                    
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
                        
                        captured = False
                        captured_piece = None

                        if board.valid_move(dragger.piece, move):
                            print()
                            print(piece.color, piece.name)
                            print(row_name[clicked_row],abs(clicked_col-8))
                            if board.squares[move.final.row][move.final.col]!=0:
                                captured = True
                                captured_piece = board.squares[move.final.row][move.final.col].piece
                                #print("Captured: ",captured_piece.color, captured_piece.name)
                            else:
                                captured = False
                                
                            
                            #print(captured)
                            if captured:
                                game.game_moves.add((piece, initial, final, captured, captured_piece))
                            else:
                                game.game_moves.add((piece, initial, final, captured))
                            
                            game.current_move = game.game_moves.tail
                            board.move(dragger.piece, move)
                            
                           
                            
                            #board.king_in_check(dragger.piece, move)
                            game.next_turn()
                         #   print(game.next_player)
                            

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

       # except:
        #    pass

main = Main()
main.mainloop()
