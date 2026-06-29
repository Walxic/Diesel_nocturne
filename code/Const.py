import pygame

COLOR_RED = (189, 42, 13)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (34, 153, 84)
COLOR_BLUE = (81, 162, 255)
COLOR_VIOLET = (152, 16, 250)

MENU_OPTION = ('New Game Player I',
               'New Game Player II cooperative',
               'New Game Player II competitive',
               'High Score',
               'Exit',)

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Level2Bg6': 6,
    'Player1': 3,
    'Player1Shot': 4,
    'Player2': 3,
    'Player2Shot': 4,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 4,
    'Enemy2Shot': 8,
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
    'Level2Bg6': 999,
    'Player1': 500,
    'Player1Shot': 1,
    'Player2': 500,
    'Player2Shot': 1,
    'Enemy1': 20,
    'Enemy1Shot': 5,
    'Enemy2': 20,
    'Enemy2Shot': 5,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 55,
    'Enemy2': 45,
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

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
PLAYER_K_SHOT = {'Player2': pygame.K_RCTRL,
                 'Player1': pygame.K_LCTRL}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Player1': 1,
    'Player1Shot': 10,
    'Player2': 1,
    'Player2Shot': 10,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 10,
    'Enemy1Shot': 0,
    'Enemy2': 15,
    'Enemy2Shot': 0,
}

SPAWN_TIME = 4000
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 30000