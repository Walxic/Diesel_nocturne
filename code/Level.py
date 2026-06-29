import random
import pygame

from pygame import Rect
from pygame.font import Font
from pygame.surface import Surface

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, WIN_WIDTH, COLOR_GREEN, COLOR_BLUE, \
    COLOR_VIOLET, EVENT_TIMEOUT, SPAWN_TIME, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player

class Level:
    def __init__(self, window, name, game_mode, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list [Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in (MENU_OPTION[1], MENU_OPTION[2]):
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        self.clock = pygame.time.Clock()
        self.running = True
        self.text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=14)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'../asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        self.clock = pygame.time.Clock()
        while True:
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True
                found_player = False
                for ent in  self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            self.window.fill((0, 0, 0))
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_list.append(shot)
                if ent.name == 'Player1':
                    self.level_text(14, f'1UP: {ent.health} | Score: {ent.score}', COLOR_VIOLET, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'2UP: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 45))
            pygame.display.flip()
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', COLOR_WHITE, (10,5))
            self.level_text(14, f'fps:{self.clock.get_fps() : .0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entities: {len(self.entity_list)}', COLOR_WHITE, (12, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)