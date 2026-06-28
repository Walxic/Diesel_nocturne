#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
from unittest import case

from pygame.examples.grid import WINDOW_HEIGHT

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def oscurecer_superficie(surf_original, nivel_brillo=120):
        filtro = pygame.Surface(surf_original.get_size()).convert_alpha()
        filtro.fill((nivel_brillo, nivel_brillo, nivel_brillo))

        surf_oscura = surf_original.copy()
        surf_oscura.blit(filtro, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return surf_oscura

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range (7):
                    list_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
               return Player(f'Player1', (10, WIN_HEIGHT/ 2 - 30))
            case 'Player2':
                return Player(f'Player2', (10, WIN_HEIGHT/ 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))