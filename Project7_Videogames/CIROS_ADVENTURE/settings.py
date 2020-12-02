GAME_TITLE = "CIRO'S ADVENTURE"
WIDTH = 1280
HEIGHT = 700
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 100, 100)
INTENSERED = (255, 0, 0)
GREEN = (100, 200, 100)
DARKGREEN = (40, 80, 40)
INTENSEGREEN = (33, 158, 0)
BLUE = (100, 100, 200)
DARKBLUE = (25, 25, 50)
YELLOW = (200, 200, 100)
INTENSEYELLOW = (200, 200, 0)
ORANGE = (200, 150, 100)
DARKORANGE = (100, 75, 50)
PURPLE = (182, 56, 157)

TILESIZE = 24
BOSS_LEVEL_DIVISOR = 5

DRAG = 10
AVOID_RADIUS = 50

"""
PLAYER_MAX_SPEED = 100
PLAYER_ACCELERATION = 2000
PLAYER_HEALTH = 100

BEE_MAX_SPEED = 50
BEE_ACCELERATION = 1000
BEE_HEALTH = 10
BEE_HIT_DAMAGE = 10

BEE_NEST_SPAWN_FREQUENCY = 5000
BEE_NEST_MAX_POPULATION = 5
BEE_NEST_HEALTH = 100
BEE_VISION_RADIUS = 150
"""

WALLS = {
    "LITLE_TREE": {"ID": 0, "IMG": "tree3.png"},
    "TREE_TRUNK": {"ID": 1, "IMG": "tree1.png"},
    "TREE": {"ID": 2, "IMG": "tree2.png"},
    "TREE_TRUNK_AUTUMN": {"ID": 3, "IMG": "tree4.png"},
    "TREE_AUTUMN": {"ID": 4, "IMG": "tree5.png"},
}

MOBS = {
    "PLAYER": {
        "ID": 0,
        "HEALTH": 100,
        "ACCELERATION": 2000,
        "MAX_SPEED": 100,
        "IMG": "parrot.png",
        "FX": "hit.wav",
    },
    "RED_BEE": {
        "ID": 1,
        "HEALTH": 10,
        "ACCELERATION": 1000,
        "MAX_SPEED": 75,
        "HIT_DAMAGE": 10,
        "VISION_RADIUS": 150,
        "IMG": "red_bee.png",
        "FX": "squish.wav",
    },
    "FAST_BEE": {
        "ID": 2,
        "HEALTH": 20,
        "ACCELERATION": 1750,
        "MAX_SPEED": 200,
        "HIT_DAMAGE": 5,
        "VISION_RADIUS": 300,
        "IMG": "fast_bee.png",
        "FX": "squish.wav",
    },
    "GRAY_BEE": {
        "ID": 3,
        "HEALTH": 15,
        "ACCELERATION": 1000,
        "MAX_SPEED": 50,
        "HIT_DAMAGE": 20,
        "VISION_RADIUS": 1000,
        "IMG": "gray_bee.png",
        "FX": "squish.wav",
    },
    "QUEEN_BEE": {
        "ID": 4,
        "HEALTH": 500,
        "ACCELERATION": 1000,
        "MAX_SPEED": 125,
        "HIT_DAMAGE": 30,
        "VISION_RADIUS": 500,
        "CAN_SHOOT": 0,
        "CAN_DAMAGE": 1,
        "WEAPON_NAME": "TOWER_GUN",
        "IMG": "Queen_bee.png",
        "FX": "squish.wav",
    },
    "BEE_NEST": {
        "ID": 5,
        "HEALTH": 100,
        "MAX_POPULATION": 5,
        "SPAWN_FREQUENCY": 5000,
        "IMG": "bee_nest3.png",
        "FX": "hit.wav",
    },
    "TOWER": {
        "ID": 6,
        "HEALTH": 100,
        "ACCELERATION": 0,
        "MAX_SPEED": 0,
        "WEAPON_NAME": "TOWER_GUN",
        "IMG": "gun_hunter.png",
        "FX": "scream.wav",
    },
    "WALKING_TOWER": {
        "ID": 7,
        "HEALTH": 100,
        "ACCELERATION": 1000,
        "MAX_SPEED": 50,
        "WEAPON_NAME": "TOWER_GUN",
        "IMG": "walking_gun_hunter_run.png",
        "FX": "scream.wav",
    },
    "WALKING_TOWER_SLASH": {
        "ID": 8,
        "HEALTH": 100,
        "ACCELERATION": 1000,
        "MAX_SPEED": 50,
        "WEAPON_NAME": "SWORD",
        "IMG": "walking_sword_hunter_run.png",
        "FX": "scream.wav",
    },
    "HUNTER_KING": {
        "ID": 9,
        "HEALTH": 500,
        "ACCELERATION": 1000,
        "MAX_SPEED": 125,
        "HIT_DAMAGE": 30,
        "VISION_RADIUS": 750,
        "CAN_SHOOT": 1,
        "CAN_DAMAGE": 0,
        "WEAPON_NAME": "HUNTER_KING_GUN",
        "IMG": "Hunter_King.png",
        "FX": "scream.wav",
    },
}

ITEM_HOVER_SPEED = 0.01
ITEMS = {
    "HEALTHPACK": {
        "APPLE": {"ID": 0, "HEAL": 30, "FX": "heal.wav", "IMG": "apple.png"},
        "BANANA": {"ID": 1, "HEAL": 10, "FX": "heal.wav", "IMG": "banana.png"},
        "BLACKBERRIES": {
            "ID": 2,
            "HEAL": 20,
            "FX": "heal.wav",
            "IMG": "blackberries.png",
        },
        "BLUEBERRIES": {
            "ID": 3,
            "HEAL": 20,
            "FX": "heal.wav",
            "IMG": "blueberries.png",
        },
        "CHERRIES": {"ID": 4, "HEAL": 20, "FX": "heal.wav", "IMG": "cherries.png"},
        "COCONUT": {"ID": 5, "HEAL": 50, "FX": "heal.wav", "IMG": "coconut.png"},
        "EGGPLANT": {"ID": 6, "HEAL": 30, "FX": "heal.wav", "IMG": "eggplant.png"},
        "GRAPES": {"ID": 7, "HEAL": 20, "FX": "heal.wav", "IMG": "grapes.png"},
        "KIWI": {"ID": 8, "HEAL": 30, "FX": "heal.wav", "IMG": "kiwi.png"},
        "LEMON": {"ID": 9, "HEAL": 20, "FX": "heal.wav", "IMG": "lemon.png"},
        "ORANGE": {"ID": 10, "HEAL": 20, "FX": "heal.wav", "IMG": "orange.png"},
        "PEAR": {"ID": 11, "HEAL": 30, "FX": "heal.wav", "IMG": "pear.png"},
        "PINEAPPLE": {"ID": 12, "HEAL": 70, "FX": "heal.wav", "IMG": "pineapple.png"},
        "PLUM": {"ID": 13, "HEAL": 40, "FX": "heal.wav", "IMG": "plum.png"},
        "RASPBERRIES": {
            "ID": 14,
            "HEAL": 20,
            "FX": "heal.wav",
            "IMG": "raspberries.png",
        },
        "STRAWBERRY": {
            "ID": 15,
            "HEAL": 50,
            "FX": "heal.wav",
            "IMG": "strawberry.png",
        },
        "TOMATO": {"ID": 16, "HEAL": 40, "FX": "heal.wav", "IMG": "tomato.png"},
        "TOMATOES_CHERRY": {
            "ID": 17,
            "HEAL": 20,
            "FX": "heal.wav",
            "IMG": "tomatoes_cherry.png",
        },
        "WATTERMELON": {
            "ID": 18,
            "HEAL": 100,
            "FX": "heal.wav",
            "IMG": "watermelon.png",
        },
        "WATTERMELON_SLICE": {
            "ID": 19,
            "HEAL": 25,
            "FX": "heal.wav",
            "IMG": "watermelon_slice.png",
        },
        "AVOCADO": {"ID": 20, "HEAL": 15, "FX": "heal.wav", "IMG": "avocado.png",},
    },
    "SPEEDUP": {"SPEED": 50, "TTL": 3000, "IMG": "speed.png"},
}

WEAPONS = {
    "WING": {
        "ID": 0,
        "FIRING_RATE": 250,
        "SPREAD": 0.1,
        "TTL": 125,
        "SPEED": 300,
        "DAMAGE": 10,
        "BULLET": "wing.png",
        "SIZE": 30,
        "AMMO_PER_SHOT": 1,
        "FX": "flutter.wav",
        "WEAPON": "wing.png",
    },
    "GUN": {
        "ID": 1,
        "FIRING_RATE": 250,
        "SPREAD": 0.1,
        "TTL": 2000,
        "SPEED": 300,
        "DAMAGE": 5,
        "BULLET": "seed.png",
        "SIZE": 10,
        "AMMO_PER_SHOT": 1,
        "FX": "spitting.wav",
        "WEAPON": "gun.png",
    },
    "MACHINEGUN": {
        "ID": 2,
        "FIRING_RATE": 100,
        "SPREAD": 0.1,
        "TTL": 1500,
        "SPEED": 300,
        "DAMAGE": 2.5,
        "BULLET": "seed.png",
        "SIZE": 8,
        "AMMO_PER_SHOT": 1,
        "FX": "spitting.wav",
        "WEAPON": "machinegun.png",
    },
    "BAZOOKA": {
        "ID": 3,
        "FIRING_RATE": 1500,
        "SPREAD": 0,
        "TTL": 5000,
        "SPEED": 750,
        "DAMAGE": 50,
        "BULLET": "seed.png",
        "SIZE": 10,
        "AMMO_PER_SHOT": 1,
        "FX": "spitting.wav",
        "WEAPON": "bazooka.png",
    },
    "SHOTGUN": {
        "ID": 4,
        "FIRING_RATE": 1000,
        "SPREAD": 0.5,
        "TTL": 500,
        "SPEED": 300,
        "DAMAGE": 10,
        "BULLET": "seed.png",
        "SIZE": 8,
        "AMMO_PER_SHOT": 10,
        "FX": "spitting.wav",
        "WEAPON": "shotgun.png",
    },
    "TOWER_GUN": {
        "ID": 5,
        "FIRING_RATE": 250,
        "SPREAD": 0.1,
        "TTL": 2000,
        "SPEED": 300,
        "DAMAGE": 5,
        "BULLET": "bullet.png",
        "SIZE": 10,
        "AMMO_PER_SHOT": 1,
        "FX": "shot.wav",
        "WEAPON": "gun.png",
    },
    "SWORD": {
        "ID": 6,
        "FIRING_RATE": 1250,
        "SPREAD": 0.1,
        "TTL": 125,
        "SPEED": 300,
        "DAMAGE": 20,
        "BULLET": "sword2.png",
        "SIZE": 1,
        "AMMO_PER_SHOT": 1,
        "FX": "flutter.wav",
        "WEAPON": "sword.png",
    },
    "HUNTER_KING_GUN": {
        "ID": 7,
        "FIRING_RATE": 600,
        "SPREAD": 0.01,
        "TTL": 3000,
        "SPEED": 300,
        "DAMAGE": 20,
        "BULLET": "bullet.png",
        "SIZE": 10,
        "AMMO_PER_SHOT": 1,
        "FX": "shot.wav",
        "WEAPON": "gun.png",
    },
    "DRILL": {
        "ID": 8,
        "FIRING_RATE": 1500,
        "SPREAD": 0.1,
        "TTL": 125,
        "SPEED": 300,
        "DAMAGE": 10,
        "BULLET": "drill.png",
        "SIZE": 5,
        "AMMO_PER_SHOT": 1,
        "FX": "pecking.wav",
        "WEAPON": "drill.png",
    },
}

# TLL = TIME TO LIVE = TIEMPO VIVO DE LA BALA
