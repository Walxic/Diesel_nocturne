#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Self

import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, PLAYER_K_RIGHT, PLAYER_K_LEFT, PLAYER_K_DOWN, PLAYER_K_UP
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position),


    def update(self, ):
        pass


    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_K_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_K_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_K_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_K_RIGHT[self.name]] and self.rect.right < WIN_HEIGHT:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
