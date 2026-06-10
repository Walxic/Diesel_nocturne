#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple, imagen_original=None):
        self.name = name
        self.surf = pygame.image.load('./asset/'+ name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass
