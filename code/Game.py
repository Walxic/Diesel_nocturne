import pygame

from code.Menu import Menu

#class Menu:
#    def __init__(self, window):
#        self.window = window

#    def run(self):
#        self.window.fill((0, 0, 0))
#        pygame.display.flip()



class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(742, 540))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass


    # chequer todos los events
    # for event in pygame.event.get():
    #       if event.type == pygame.QUIT:
    #          pygame.quit()  # close la ventana
    #         quit()  # end pygame
