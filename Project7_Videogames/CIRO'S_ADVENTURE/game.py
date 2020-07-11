import pygame
from settings import *

from map import Map
from sprites import *

from os import path


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(GAME_TITLE)

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()

        self.large_font = pygame.font.SysFont("arial", 80)
        self.small_font = pygame.font.SysFont("arial", 32)
        self.uid_font = pygame.font.SysFont("arial", 26)

        self.score_levels = 0
        self.score_mobs = 0  # per level
        self.total_score_mobs = 0  # in total
        self.saved_weapons = [
            "WING",
        ]
        self.button = ""
        self.load_img_and_sound()
        pygame.mixer.music.play(-1)

    def load_img_and_sound(self):
        self.root_folder = path.dirname(__file__)
        fx_folder = path.join(self.root_folder, "sound")

        self.main_menu_img = pygame.image.load(
            path.join(self.root_folder, "img/main_menu.png")
        ).convert_alpha()
        self.new_weapon_img = pygame.image.load(
            path.join(self.root_folder, "img/new_weapon_menu.png")
        ).convert_alpha()

        img_bullet_folder = path.join(self.root_folder, "img/bullets")
        img_weapon_folder = path.join(self.root_folder, "img/weapons/resizing")
        img_weapon_big_size_folder = path.join(self.root_folder, "img/weapons")
        self.bullet_images = []
        self.weapons_obtained = {}
        self.weapons_obtained_big_size = {}
        self.weapons_sounds = []
        for weapon in WEAPONS:
            bullet_sprite = WEAPONS[weapon]["BULLET"]
            weapon_name = WEAPONS[weapon]["WEAPON"]
            sound_name = WEAPONS[weapon]["FX"]
            self.bullet_images.append(
                pygame.image.load(
                    path.join(img_bullet_folder, bullet_sprite)
                ).convert_alpha()
            )
            self.weapons_obtained[weapon] = pygame.image.load(
                path.join(img_weapon_folder, weapon_name)
            ).convert_alpha()
            self.weapons_obtained_big_size[weapon] = pygame.image.load(
                path.join(img_weapon_big_size_folder, weapon_name)
            ).convert_alpha()
            self.weapons_sounds.append(
                pygame.mixer.Sound(path.join(fx_folder, sound_name))
            )

        img_mobs_folder = path.join(self.root_folder, "img/mobs")
        self.mobs_images = []
        self.dye_sound = []
        for mob in MOBS:
            mob_sprite = MOBS[mob]["IMG"]
            sound_name = MOBS[mob]["FX"]
            self.mobs_images.append(
                pygame.image.load(
                    path.join(img_mobs_folder, mob_sprite)
                ).convert_alpha()
            )
            self.dye_sound.append(pygame.mixer.Sound(path.join(fx_folder, sound_name)))

        img_walls_folder = path.join(self.root_folder, "img/walls")
        self.walls_images = []
        for wall in WALLS:
            wall_sprite = WALLS[wall]["IMG"]
            self.walls_images.append(
                pygame.image.load(
                    path.join(img_walls_folder, wall_sprite)
                ).convert_alpha()
            )

        img_health_folder = path.join(self.root_folder, "img/items/health")
        self.health_images = []
        for fruit in ITEMS["HEALTHPACK"]:
            fruit_sprite = ITEMS["HEALTHPACK"][fruit]["IMG"]
            self.health_images.append(
                pygame.image.load(
                    path.join(img_health_folder, fruit_sprite)
                ).convert_alpha()
            )

        img_speed_folder = path.join(self.root_folder, "img/items/speed")
        self.speed_images = pygame.image.load(
            path.join(img_speed_folder, ITEMS["SPEEDUP"]["IMG"])
        )

        self.health_fx = pygame.mixer.Sound(path.join(fx_folder, "health.wav"))
        self.speed_fx = pygame.mixer.Sound(path.join(fx_folder, "speed.wav"))
        self.cut_down_fx = pygame.mixer.Sound(path.join(fx_folder, "cut_down.wav"))
        self.game_over_fx = pygame.mixer.Sound(path.join(fx_folder, "game_over.wav"))
        self.new_weapon_fx = pygame.mixer.Sound(path.join(fx_folder, "new_weapon.wav"))
        self.win_fx = pygame.mixer.Sound(path.join(fx_folder, "win.wav"))
        pygame.mixer.music.load(path.join(fx_folder, "ElBosqueEncantado.mp3"))

    def start_game(self):
        self.run()

    def run(self):
        self.load_data()
        self.score_levels += 1
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def load_data(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.nests = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.players = pygame.sprite.Group()

        self.map = Map()
        # self.map.load_from_file("map.txt")
        # self.map.carve_cave_drunken_diggers(self, WIDTH, HEIGHT)
        self.map.carve_cave_cellular_automata(self, WIDTH, HEIGHT)
        self.populate_map()
        self.map.create_sprites_from_map_data(self)

        self.total_mobs = len(self.mobs)
        self.player = self.map.player
        self.weapon_number = -1
        self.player.changing_weapons(self.saved_weapons[self.weapon_number])

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

    def counting_destroyed_mobs(self):
        self.new_mobs = len(self.mobs)
        if self.total_mobs > self.new_mobs:
            killed = self.total_mobs - self.new_mobs
            self.score_mobs += killed
            self.total_score_mobs += killed
            self.total_mobs = self.new_mobs
        if self.total_mobs < self.new_mobs:
            self.total_mobs = self.new_mobs

    def adding_new_weapons(self):
        if len(self.mobs) == 0:
            if "GUN" not in self.saved_weapons:
                self.saved_weapons.append("GUN")
                return True
            elif "MACHINEGUN" not in self.saved_weapons:
                self.saved_weapons.append("MACHINEGUN")
                return True
            elif "SHOTGUN" not in self.saved_weapons:
                self.saved_weapons.append("SHOTGUN")
                return True

    def changing_current_weapon(self):
        if self.button == 4:
            if self.weapon_number >= len(self.saved_weapons) - 1:
                self.weapon_number = 0
            else:
                self.weapon_number += 1
            self.player.changing_weapons(self.saved_weapons[self.weapon_number])
            self.button = ""
        elif self.button == 5:
            if self.weapon_number <= -(len(self.saved_weapons)):
                self.weapon_number = -1
            else:
                self.weapon_number -= 1
            self.player.changing_weapons(self.saved_weapons[self.weapon_number])
            self.button = ""

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                or event.type == pygame.MOUSEBUTTONUP
            ):
                if event.button == 4 or event.button == 5:
                    self.button = event.button

    def update(self):
        self.all_sprites.update()
        self.counting_destroyed_mobs()
        self.changing_current_weapon()
        if self.player.health == 0:
            self.playing = False
            self.game_over()

        if len(self.nests) == 0:
            self.next_level()

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
        health_background = pygame.Rect(5, 5, width, height)
        bar_width = int(health * (width - padding * 2))
        health_fill = pygame.Rect(
            5 + padding, 5 + padding, bar_width, height - padding * 2
        )
        pygame.draw.rect(self.screen, DARKBLUE, health_background)
        pygame.draw.rect(self.screen, BLUE, health_fill)

        levels_text = self.uid_font.render(f"Level: {self.score_levels}", True, WHITE)
        destroyed_text = self.uid_font.render(f"Killed: {self.score_mobs}", True, WHITE)
        enemies_text = self.uid_font.render(f"Alive: {len(self.mobs)}", True, WHITE)
        self.screen.blit(enemies_text, (WIDTH - 275, 0))

        self.screen.blit(levels_text, (175, 3))
        self.screen.blit(destroyed_text, (WIDTH - 135, 0))

        weapon_background = pygame.Rect(108, 5, width - 38, height)
        pygame.draw.rect(self.screen, WHITE, weapon_background)

        current_weapon_img = self.weapons_obtained[self.player.weapon_name]
        self.screen.blit(current_weapon_img, (110, 5))

    def main_menu(self):
        pygame.mixer.music.pause()
        title_text = self.large_font.render("CIRO'S ADVENTURE", True, BLUE)
        instructions_text = self.small_font.render(
            "[Press any key to begin]", True, BLACK
        )

        self.screen.blit(self.main_menu_img, (0, 0))
        self.screen.blit(
            title_text,
            (
                WIDTH // 2 - title_text.get_rect().centerx,
                HEIGHT // 2 - title_text.get_rect().centery,
            ),
        )
        self.screen.blit(
            instructions_text,
            (WIDTH // 2 - instructions_text.get_rect().centerx, HEIGHT // 2 + 150),
        )

        pygame.display.flip()
        pygame.time.delay(1000)
        in_main_menu = True
        while in_main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_main_menu = False
        pygame.mixer.music.unpause()
        self.start_game()

    def game_over(self):
        title_text = self.large_font.render("GAME OVER", True, RED)
        levels_text = self.small_font.render(
            f"You have reached {self.score_levels} levels", True, WHITE
        )
        destroyed_text = self.small_font.render(
            f"You have destroyed {self.total_score_mobs} enemies", True, WHITE
        )
        continue_text = self.small_font.render(
            "[Press any key to continue]", True, WHITE
        )

        self.screen.fill(BLACK)
        self.screen.blit(
            title_text,
            (
                WIDTH // 2 - title_text.get_rect().centerx,
                HEIGHT // 2 - title_text.get_rect().centery - 100,
            ),
        )
        self.screen.blit(
            levels_text, (WIDTH // 2 - levels_text.get_rect().centerx, HEIGHT // 2 + 25)
        )
        self.screen.blit(
            destroyed_text,
            (WIDTH // 2 - destroyed_text.get_rect().centerx, HEIGHT // 2 + 75),
        )
        self.screen.blit(
            continue_text,
            (WIDTH // 2 - continue_text.get_rect().centerx, HEIGHT // 2 + 150),
        )

        pygame.display.flip()
        pygame.mixer.music.stop()
        self.game_over_fx.play()
        pygame.time.delay(1000)
        in_gameover_menu = True
        while in_gameover_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_gameover_menu = False

        self.player.health = PLAYER_HEALTH
        self.score_levels = 0
        self.score_mobs = 0
        self.total_score_mobs = 0
        self.saved_weapons = [
            "WING",
        ]
        self.main_menu()

    def new_weapon_notification(self):
        if self.adding_new_weapons() == True:
            title_text = self.small_font.render(
                "CONGRATS, YOU'VE KILLED ALL ENEMIES!", True, BLACK
            )
            notification_text = self.small_font.render(
                f"Now you can shoot in {self.saved_weapons[-1]} mode", True, BLACK
            )
            instructions_text = self.small_font.render(
                "[Press any key to go to next level]", True, BLACK
            )

            self.screen.blit(self.main_menu_img, (0, 0))
            self.screen.blit(
                title_text,
                (
                    WIDTH // 2 - title_text.get_rect().centerx,
                    HEIGHT // 2 - title_text.get_rect().centery - 150,
                ),
            )
            self.screen.blit(
                notification_text,
                (WIDTH // 2 - notification_text.get_rect().centerx, HEIGHT // 2 - 75),
            )
            current_weapon_img = self.weapons_obtained_big_size[self.saved_weapons[-1]]
            self.screen.blit(
                current_weapon_img,
                (WIDTH // 2 - current_weapon_img.get_rect().centerx, HEIGHT // 2),
            )
            self.screen.blit(
                instructions_text,
                (WIDTH // 2 - instructions_text.get_rect().centerx, HEIGHT // 2 + 150),
            )
            pygame.time.delay(500)
            pygame.mixer.music.pause()
            pygame.display.flip()
            self.new_weapon_fx.play()
            pygame.time.delay(1000)
            in_new_weapon_menu = True
            while in_new_weapon_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        in_new_weapon_menu = False

    def next_level(self):
        if not self.new_weapon_notification():
            pygame.mixer.music.pause()
        title_text = self.large_font.render("YOU WIN", True, INTENSEGREEN)
        levels_text = self.small_font.render(
            f"LEVELS COMPLETED: {self.score_levels}", True, BLACK
        )
        total_destroyed_text = self.small_font.render(
            f"TOTAL ENEMIES DESTROYED: {self.total_score_mobs}", True, BLACK
        )
        level_destroyed_text = self.small_font.render(
            f"ENEMIES DESTROYED ON THIS LEVEL: {self.score_mobs}", True, BLACK,
        )
        instructions_text = self.small_font.render(
            "[Press any key to go to next level]", True, BLACK
        )

        self.screen.blit(self.main_menu_img, (0, 0))
        self.screen.blit(
            title_text,
            (
                WIDTH // 2 - title_text.get_rect().centerx,
                HEIGHT // 2 - title_text.get_rect().centery - 125,
            ),
        )
        self.screen.blit(
            levels_text,
            (WIDTH // 2 - levels_text.get_rect().centerx, HEIGHT // 2 - 25),
        )
        self.screen.blit(
            total_destroyed_text,
            (WIDTH // 2 - total_destroyed_text.get_rect().centerx, HEIGHT // 2 + 25),
        )
        self.screen.blit(
            level_destroyed_text,
            (WIDTH // 2 - level_destroyed_text.get_rect().centerx, HEIGHT // 2 + 75),
        )
        self.screen.blit(
            instructions_text,
            (WIDTH // 2 - instructions_text.get_rect().centerx, HEIGHT // 2 + 150),
        )
        pygame.time.delay(500)
        pygame.display.flip()
        self.win_fx.play()
        pygame.time.delay(1000)
        in_next_level_menu = True
        while in_next_level_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_next_level_menu = False
        pygame.mixer.music.unpause()
        self.score_mobs = 0
        self.start_game()


game = Game()
game.main_menu()
