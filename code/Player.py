import pygame

from code.Const import (ENTITY_SPEED, WIN_HEIGHT, PLAYER_K_RIGHT, PLAYER_K_LEFT, PLAYER_K_DOWN, PLAYER_K_UP,
                        WIN_WIDTH, PLAYER_K_SHOT, ENTITY_SHOT_DELAY)
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
    def update(self, ):
        self.move()
    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_K_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_K_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_K_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_K_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
    def shot(self):
        if self.shot_delay > 0:
            self.shot_delay -= 1
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_K_SHOT[self.name]]:
            if self.shot_delay == 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None