#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Rect
from pygame.examples.grid import WINDOW_HEIGHT

from pygame.font import Font
from pygame.surface import Surface

from code.Const import COLOR_WHITE, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 5000
        self.clock = pygame.time.Clock()
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list [Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 2000

    def run(self, ):
        pygame.mixer_music.load(f'./asset/Level1.mp3')
        pygame.mixer_music.play(-1)
        self.clock = pygame.time.Clock()
        while True:
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.window.fill((0, 0, 0))
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', COLOR_WHITE, (10,5))
            self.level_text(14, f'fps:{self.clock.get_fps() : .0f}', COLOR_WHITE, (10, WINDOW_HEIGHT - 5))
            self.level_text(14, f'entities: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))
            pygame.display.flip()
        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

