import pygame

class Ship:

    def _init_(self, screen):
        
    ## inicializando espaçonave e definindo sua posição inicial

        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.image_size = (70, 70)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        def blitme(self):

        ##Desenha a espaçonave em sua posição inicial
             
            self.screen.blit(self.image, self.rect)