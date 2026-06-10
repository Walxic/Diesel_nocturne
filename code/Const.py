import pygame

COLOR_RED = (189, 42, 13)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (34, 153, 84)

MENU_OPTION = ('New Game Player I',
               'New Game Player II cooperative',
               'New Game Player II competitive',
               'High Score',
               'Exit',)

ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Level1Bg5' : 5,
    'Level1Bg6' : 6,
    'Player1' : 3,
    'Player2' : 3,
    'Enemy1' : 2,
    'Enemy2' : 4,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}





EVENT_ENEMY = pygame.USEREVENT + 1

WIN_WIDTH = 576
WIN_HEIGHT = 324

PLAYER_K_UP = {'Player2': pygame.K_UP,
                 'Player1': pygame.K_w}
PLAYER_K_DOWN = {'Player2': pygame.K_DOWN,
                   'Player1': pygame.K_s}
PLAYER_K_LEFT = {'Player2': pygame.K_LEFT,
                   'Player1': pygame.K_a}
PLAYER_K_RIGHT = {'Player2': pygame.K_RIGHT,
                    'Player1': pygame.K_d}
PLAYER_K_SHOOT = {'Player2': pygame.K_SPACE,
                    'Player1': pygame.K_0}
