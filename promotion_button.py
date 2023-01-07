import pygame

class Button:
    def __init__(self,screen, img, width, height, pos):
        self.select = False
        
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#FFFFFF'
        self.screen = screen
        self.img_name = img
        self.img = pygame.image.load("images/imgs-80px/{}.png".format(img))
        self.img_rect = self.img.get_rect(center = self.top_rect.center)
        
    def draw(self):
        pygame.draw.rect(self.screen, self.top_color, self.top_rect,border_radius = 5)
        self.screen.blit(self.img, self.img_rect)

    def select_piece(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.select = True
                return True
            return False
        return False
##            else:
##                if self.select == True:
##                    self.select = False
##                    print(self.img_name)
##                    
