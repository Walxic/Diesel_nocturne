import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    #chequear todos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Cerrar la ventana
            quit() #fin del juego al presionar 'X'

