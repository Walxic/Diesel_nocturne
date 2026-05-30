import pygame
import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Menu_.png")
        self.rect = self.surf.get_rect()

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()
            # chequer todos los events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()  # close la ventana
                     quit()  # end pygame

    pass
