import pygame

from const import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_col = 0
        self.initial_row = 0

    # blit method
    def update_blit(self, surface):
        self.piece.set_texture(size = 128)
        texture = self.piece.texture
        
        img = pygame.image.load(texture)

        img_center = self.mouseX, self.mouseY

        self.piece.texture_rect = img.get_rect(center = img_center)

        surface.blit(img, self.piece.texture_rect)

    # other methods
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_inital(self, pos):
        self.initial_col, self.initial_row = pos[0] // sqsize, pos[1] // sqsize

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False