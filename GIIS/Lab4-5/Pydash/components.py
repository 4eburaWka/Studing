
# Parent class
import pygame

from functions import get_image_by_name
from config import *

"""
Obstacle classes
"""

class Draw(pygame.sprite.Sprite):
    """parent class to all obstacle classes; Sprite class"""

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.rect = self.image.get_rect(topleft=pos)


#  ====================================================================================================================#
#  classes of all obstacles. this may seem repetitive but it is useful(to my knowledge)
#  ====================================================================================================================#
# children
class Platform(Draw):
    """block"""
    image = get_image_by_name(blocks_images[PLATFORM])

class NarrowPlatform(Draw):
    """block"""
    image = get_image_by_name(blocks_images[NARROW_PLATFORM])

class DownNarrowPlatform(Draw):
    """block"""
    image = get_image_by_name(blocks_images[DOWN_NARROW_PLATFORM])

class Spike(Draw):
    """spike"""
    image = get_image_by_name(blocks_images[SPIKE])

class ShortSpike(Draw):
    """spike"""
    image = get_image_by_name(blocks_images[SHORT_SPIKE])

class Coin(Draw):
    """coin. get 6 and you win the game"""
    image = get_image_by_name(blocks_images[COIN])


class Orb(Draw):
    """orb. click space or up arrow while on it to jump in midair"""
    image = get_image_by_name(blocks_images[ORB])
    is_jumped = False


class Pad(Draw):
    """yellow pad."""
    image = get_image_by_name(blocks_images[PAD])

class PinkPad(Draw):
    """yellow pad."""
    image = get_image_by_name(blocks_images[PINK_PAD])


class Trick(Draw):
    """block, but its a trick because you can go through it"""
    image = get_image_by_name(blocks_images[TRICK])

class GravityPortal(Draw):
    """change gravity."""
    image = get_image_by_name(blocks_images[GRAVITY_PORTAL])
    is_active = True

class RocketPortal(Draw):
    """change gravity."""
    image = get_image_by_name(blocks_images[ROCKET_PORTAL])
    is_active = True

class CubePortal(Draw):
    """change gravity."""
    image = get_image_by_name(blocks_images[CUBE_PORTAL])
    is_active = True

class End(Draw):
    "place this at the end of the level"
    image = get_image_by_name(blocks_images[END])
