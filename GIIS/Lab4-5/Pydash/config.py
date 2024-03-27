import random
import os

from pygame import Vector2
import pygame

start_lvl = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DEATH_EFFECT = [
    pygame.image.load(os.path.join("images/death_effect", "effect-1.png")),
    pygame.image.load(os.path.join("images/death_effect", "effect-2.png")),
    pygame.image.load(os.path.join("images/death_effect", "effect-3.png")),
    pygame.image.load(os.path.join("images/death_effect", "effect-4.png")),
    pygame.image.load(os.path.join("images/death_effect", "effect-5.png")),
    pygame.image.load(os.path.join("images/death_effect", "effect-6.png")),
]

# CUBE_AVATAR = pygame.image.load(os.path.join("images", "player.png"))
ROCKET_AVATAR = pygame.image.load(os.path.join("images", "rocket-avatar.png"))
color = lambda: tuple([random.randint(0, 255) for i in range(3)])  # lambda function for random color, not a constant.
GRAVITY = Vector2(0, 1.1)  # Vector2 is a pygame
ROCKET_GRAVITY = Vector2(0, 0.4)
jump_amount = 14
rocket_jump_amount = 8
PLAYER_START_POS = (150, 550)
CameraX = 10

### PLAYER TYPES
CUBE = 0
ROCKET = 1
###

objects_size = 48

# csv objects
NOTHING = 0
PLATFORM = 1
TRICK = 2
SPIKE = 3
ORB = 4
COIN = 5
END = 6
PAD = 7
GRAVITY_PORTAL = 8
ROCKET_PORTAL = 9
PINK_PAD = 10
NARROW_PLATFORM = 11
SHORT_SPIKE = 12
DOWN_NARROW_PLATFORM = 13
CUBE_PORTAL = 14

blocks_images = {
    PLATFORM: "block_1.png",
    NARROW_PLATFORM: "narrow-platform.png",
    DOWN_NARROW_PLATFORM: "down-narrow-platform.png",
    TRICK: "obj-breakable.png",
    SPIKE: "obj-spike.png",
    SHORT_SPIKE: "short-spike.png",
    COIN: "coin.png",
    ORB: "orb-yellow.png",
    PAD: "pad.png",
    PINK_PAD: "pink-pad.png",
    GRAVITY_PORTAL: "gravity-portal.png",
    ROCKET_PORTAL: "rocket-portal.png",
    CUBE_PORTAL: "delete_icon.png",
    END: "avatar.png",
}

levels = os.listdir('levels')
music = os.listdir('music')

### EDITOR
CELL_SIZE = 51
###

