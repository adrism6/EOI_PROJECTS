import pygame
from settings import *

from map import Map
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.nests = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.players = pygame.sprite.Group()

        self.map = Map()
        self.map.carve_cave_cellular_automata(self, WIDTH, HEIGHT)
        self.populate_map()
        # self.map.load_from_file("map.txt")
        self.map.create_sprites_from_map_data(self)

        self.player = Player(
            self,
            self.map.player_entry_point,
            PLAYER_MAX_SPEED,
            PLAYER_ACCELERATION,
            PLAYER_HEALTH,
            YELLOW,
        )

    def populate_map(self):
        for _ in range(3):
            x, y = self.map.get_empty_position()
            self.map.map_data[y][x] = "B"

        x, y = self.map.get_empty_position()
        self.map.map_data[y][x] = "P"

        x, y = self.map.get_empty_position()
        self.map.map_data[y][x] = "h"

        x, y = self.map.get_empty_position()
        self.map.map_data[y][x] = "s"

        x, y = self.map.get_empty_position()
        self.map.map_data[y][x] = "T"

    def start_game(self):
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(DARKGREEN)
        self.all_sprites.draw(self.screen)
        for mob in self.mobs:
            mob.draw_health()

        self.draw_game_ui()

        pygame.display.flip()

    def draw_game_ui(self):
        health = self.player.health / self.player.max_health
        padding = 3
        width = 100
        height = 25
        health_background = pygame.Rect(1, 1, width, height)
        bar_width = int(health * (width - padding * 2))
        health_fill = pygame.Rect(
            1 + padding, 1 + padding, bar_width, height - padding * 2
        )
        pygame.draw.rect(self.screen, DARKBLUE, health_background)
        pygame.draw.rect(self.screen, BLUE, health_fill)


game = Game()
game.start_game()
