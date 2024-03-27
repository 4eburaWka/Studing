import os
import random

import pygame

from pygame.math import Vector2
from pygame.draw import rect
from tkinter import messagebox as mb

from config import *
from components import *
from functions import block_map, check_collide
from editor import Editor, PlayerEditor, show_editor

pygame.init()

pygame.event.set_allowed([pygame.QUIT])
screen = pygame.display.set_mode([1920,1080])

DEADTH_SOUND = pygame.mixer.Sound("sounds/death-sound.mp3")
DEADTH_SOUND.set_volume(3.0)
LEVEL_COMPLETE_SOUND = pygame.mixer.Sound("sounds/level-complete-sound.mp3")

# controls the main game while loop
done = False

# controls whether or not to start the game from the main menu
start = False

# sets the frame rate of the program
clock = pygame.time.Clock()

"""
Main player class
"""

class Player(pygame.sprite.Sprite):
    """Class for player. Holds update method, win and die variables, collisions and more."""
    win: bool
    died: bool
    is_orb_jump: bool

    def __init__(self, platforms, pos, *groups):
        """
        :param image: block face avatar
        :param platforms: obstacles such as coins, blocks, spikes, and orbs
        :param pos: starting position
        :param groups: takes any number of sprite groups.
        """
        super().__init__(*groups)
        self.onGround = False  # player on ground?
        self.platforms = platforms  # obstacles but create a class variable for it
        self.died = False  # player died?
        self.win = False  # player beat level?

        self.type = CUBE
        self.pos = pos
        self.update_avatar(CUBE_AVATAR)  # get rect gets a Rect object from the image
        self.jump_amount = jump_amount  # jump strength
        self.gravity = GRAVITY
        self.gravity_sign = 1
        self.particles = []  # player trail
        self.isjump = False  # is the player jumping?
        self.vel = Vector2(0, 0)  # velocity starts at zero
        self.in_portal = False

    def update_avatar(self, image):
        self.image = pygame.transform.smoothscale(image, (objects_size, objects_size))
        self.rect = self.image.get_rect(center=self.pos)

    def draw_particle_trail(self, x, y, color=(255, 255, 255)):
        """draws a trail of particle-rects in a line at random positions behind the player"""

        self.particles.append(
                [[x - 5, y - 8], [random.randint(0, 25) / 10 - 1, random.choice([0, 0])],
                 random.randint(5, 8)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.5
            particle[1][0] -= 0.4
            rect(alpha_surf, color,
                 ([int(particle[0][0]), int(particle[0][1])], [int(particle[2]) for i in range(2)]))
            if particle[2] <= 0:
                self.particles.remove(particle)

    def collide(self, yvel, platforms):
        global coins
        
        if self.rect.y < 0:
            self.died = True
            return

        for p in platforms:
            if not 100 < p.rect.x < 200:
                continue
            collide = check_collide(self.rect, p.rect)
            if not collide:
                continue

            if isinstance(p, Platform) or isinstance(p, NarrowPlatform) or isinstance(p, DownNarrowPlatform):  # these are the blocks (may be confusing due to self.platforms)
                if (yvel > 0 and self.gravity_sign > 0) or (yvel < 0 and self.gravity_sign < 0):
                    """if player is going down(yvel is +)"""
                    if self.gravity_sign > 0:
                        self.rect.bottom = p.rect.top  # dont let the player go through the ground
                    else:
                        self.rect.top = p.rect.bottom
                    self.vel.y = 0  # rest y velocity because player is on ground

                    # set self.onGround to true because player collided with the ground
                    self.onGround = True

                    # reset jump
                    self.isjump = False
                    self.died = False
                elif yvel < 0 and collide > 10 and self.gravity_sign > 0:
                    """if yvel is (-),player collided while jumping"""
                    self.vel.y = 0
                    self.rect.top = p.rect.bottom  # player top is set the bottom of block like it hits it head
                elif yvel > 0 and collide > 10 and self.gravity_sign < 0:
                    self.vel.y = 0
                    self.rect.bottom = p.rect.top
                elif yvel == 0 and collide > 10:
                    """otherwise, if player collides with a block, he/she dies."""
                    self.vel.x = CameraX
                    self.rect.right = p.rect.left  # dont let player go through walls
                    self.died = True
            
            elif isinstance(p, Trick):  # these are the blocks (may be confusing due to self.platforms)
                if (yvel > 0 and self.gravity_sign > 0) or (yvel < 0 and self.gravity_sign < 0):
                    """if player is going down(yvel is +)"""
                    if self.gravity_sign > 0:
                        self.rect.bottom = p.rect.top  # dont let the player go through the ground
                    else:
                        self.rect.top = p.rect.bottom
                    self.vel.y = 0  # rest y velocity because player is on ground

                    # set self.onGround to true because player collided with the ground
                    self.onGround = True

                    # reset jump
                    self.isjump = False
                    self.died = False
                elif (yvel < 0 and self.gravity_sign > 0) or (yvel > 0 and self.gravity_sign < 0) or (yvel == 0):
                    """if yvel is (-),player collided while jumping"""
                    p.rect.x = 0
                    p.rect.y = 0

            elif collide > 8 and (isinstance(p, Spike) or isinstance(p, ShortSpike)):
                self.died = True  # die on spike
            
            elif isinstance(p, Pad):
                self.jump(self.jump_amount+1)

            elif isinstance(p, PinkPad):
                self.jump(self.jump_amount-1)

            elif isinstance(p, Orb) and (keys[pygame.K_UP] or keys[pygame.K_SPACE]):
                if not p.is_jumped:
                    self.jump()
            
            elif isinstance(p, GravityPortal) and p.is_active:
                self.gravity_sign *= -1
                p.is_active = False

            elif isinstance(p, RocketPortal):
                self.type = ROCKET
                self.gravity = ROCKET_GRAVITY
                self.jump_amount = rocket_jump_amount
                self.update_avatar(ROCKET_AVATAR)

            elif isinstance(p, CubePortal):
                self.type = CUBE
                self.gravity = GRAVITY
                self.jump_amount = jump_amount
                self.update_avatar(CUBE_AVATAR)

            elif isinstance(p, Coin):
                # keeps track of all coins throughout the whole game(total of 6 is possible)
                coins += 1

                # erases a coin
                p.rect.x = 0
                p.rect.y = 0

            elif isinstance(p, End):
                self.win = True
                break


    def jump(self, jump_amount = None):
        if jump_amount is None:
            jump_amount = self.jump_amount
        self.vel.y = -jump_amount * self.gravity_sign  # players vertical velocity is negative so ^
            

    def update(self):
        """update player"""
        if self.type == CUBE and self.isjump and self.onGround:
            """if player wants to jump and player is on the ground: only then is jump allowed"""
            self.jump()
        elif self.type == ROCKET and self.isjump:
            self.jump()

        if not self.onGround:  # only accelerate with gravity if in the air
            self.vel += self.gravity * self.gravity_sign  # Gravity falls

            # max falling speed
            if self.vel.y > 100: self.vel.y = 100

        # do x-axis collisions
        self.collide(0, self.platforms)

        # increment in y direction
        self.rect.top += self.vel.y

        # assuming player in the air, and if not it will be set to inversed after collide
        self.onGround = False

        # do y-axis collisions
        self.collide(self.vel.y, self.platforms)

        # check if we won or if player won
        eval_outcome(self.win, self.died)
    

"""
Functions
"""

def init_level(map):
    """this is similar to 2d lists. it goes through a list of lists, and creates instances of certain obstacles
    depending on the item in the list"""
    x = 0
    y = objects_size

    for row in map:
        for col in row:

            if col == PLATFORM:
                Platform((x, y), elements)

            elif col == NARROW_PLATFORM:
                NarrowPlatform((x, y), elements)

            elif col == DOWN_NARROW_PLATFORM:
                DownNarrowPlatform((x, y), elements)

            elif col == COIN:
                Coin((x, y), elements)

            elif col == SPIKE:
                Spike((x, y), elements)
            
            elif col == SHORT_SPIKE:
                ShortSpike((x, y), elements)
            
            elif col == PAD:
                Pad((x, y), elements)
            
            elif col == PINK_PAD:
                PinkPad((x, y), elements)
            
            elif col == GRAVITY_PORTAL:
                GravityPortal((x, y), elements)
            
            elif col == CUBE_PORTAL:
                CubePortal((x, y), elements)
            
            elif col == ROCKET_PORTAL:
                RocketPortal((x, y), elements)
        
            elif col == ORB:
                # orbs.append([x, y])
                Orb((x, y), elements)

            elif col == TRICK:
                Trick((x, y), elements)
            
            elif col == END:
                End((x, y), elements)

            x += objects_size
        y += objects_size
        x = 0


def blitRotate(surf, image, pos, originpos: tuple, angle: float):
    """
    rotate the player
    :param surf: Surface
    :param image: image to rotate
    :param pos: position of image
    :param originpos: x, y of the origin to rotate about
    :param angle: angle to rotate
    """
    # calculate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]

    # make sure the player does not overlap, uses a few lambda functions(new things that we did not learn about number1)
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    # calculate the translation of the pivot
    pivot = Vector2(originpos[0], -originpos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originpos[0] + min_box[0] - pivot_move[0], pos[1] - originpos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotozoom(image, angle, 1)

    # rotate and blit the image
    surf.blit(rotated_image, origin)


def won_screen():
    """show this screen when beating a level"""
    global attempts, level, fill
    attempts = 0
    player_sprite.clear(player.image, screen)
    screen.fill(pygame.Color("yellow"))
    if level == len(levels) - 1:
        if coins == 6:
            txt_win1 = f"Coin{coins}/6! "
            txt_win2 = "the game, Congratulations"
    else:
        txt_win1 = f"level{level}"
        txt_win2 = f"Coins: {coins}/3. "
    txt_win = f"{txt_win1} You beat {txt_win2}! Press SPACE to restart, or ESC to exit"

    won_game = font.render(txt_win, True, BLUE)

    screen.blit(won_game, (200, 300))
    level += 1

    wait_for_key()
    reset()


def death_screen():
    """show this screenon death"""
    global attempts, fill
    fill = 0
    player_sprite.clear(player.image, screen)
    attempts += 1
    wait_for_key()
    reset()


def eval_outcome(won: bool, died: bool):
    """simple function to run the win or die screen after checking won or died"""
    if won:
        LEVEL_COMPLETE_SOUND.play()
        won_screen()
    if died:
        DEADTH_SOUND.play()
        pygame.mixer_music.stop()
        death_screen()


def start_screen():
    """main menu. option to switch level, and controls guide, and game overview."""
    global level
    screen.fill(BLACK)
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        level += 1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        level -= 1
    if level == len(levels):
        level = 0
    elif level == -1:
        level = len(levels) - 1
    clock.tick(15)


    welcome = font.render(f"Welcome to Pydash. choose level({level + 1}) by keypad", True, WHITE)

    controls = font.render("Controls: jump: Space/Up exit: Esc", True, GREEN)

    screen.blits([[welcome, (100, 100)], [controls, (100, 400)], [tip, (100, 500)]])

    level_memo = font.render(f"Level '{levels[level]}'", True, (255, 255, 0))
    screen.blit(level_memo, (100, 200))


def reset():
    """resets the sprite groups, music, etc. for death and new level"""
    global player, elements, player_sprite, level, level_len, music

    player_sprite = pygame.sprite.Group()
    elements = pygame.sprite.Group()
    player = Player(elements, PLAYER_START_POS, player_sprite)
    map, level_len, music = block_map(levels[level % len(levels)])
    try:
        pygame.mixer.music.load(os.path.join("music", music))
    except pygame.error:
        pass
        # mb.showerror("pygame.error", "Невозможно загрузить трек")
    else:
        pygame.mixer_music.play()
    init_level(map)

def move_map():
    """moves obstacles along the screen"""
    global x
    for sprite in elements:
        sprite.rect.x -= CameraX
        if sprite.rect.x < -objects_size:
            elements.remove(sprite)


def draw_stats(surf):
    """
    draws progress bar for level, number of attempts, displays coins collected, and progressively changes progress bar
    colors
    """
    global fill

    tries = font.render(f" Attempt {str(attempts)}", True, WHITE)
    BAR_LENGTH = 1800
    BAR_HEIGHT = 10

    fill += (BAR_LENGTH / level_len) * (CameraX / objects_size) * 1.048

     
    outline_rect = pygame.Rect(0, 0, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(0, 0, fill, BAR_HEIGHT)
    col = pygame.Color("white")
    rect(surf, col, fill_rect, 0, 4)
    rect(surf, WHITE, outline_rect, 3, 4)
    screen.blit(tries, (BAR_LENGTH, 0))

CUBE_AVATAR = pygame.image.load(os.path.join("images", "player.png"))
def wait_for_key():
    """separate game loop for waiting for a key press while still running game loop
    """
    global level, start, player, CUBE_AVATAR
    waiting = True
    while waiting:
        clock.tick(60)
        pygame.display.flip()

        if not start:
            start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True
                    waiting = False
                    CUBE_AVATAR = pygame.image.load(os.path.join("images", "player.png"))
                    player.update_avatar(CUBE_AVATAR)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_e:
                    show_editor(Editor)
                elif event.key == pygame.K_g:
                    show_editor(PlayerEditor)


def coin_count(coins):
    """counts coins"""
    if coins >= 3:
        coins = 3
    coins += 1
    return coins


"""
Global variables
"""
font = pygame.font.SysFont("lucidaconsole", 20)

# square block face is main character the icon of the window is the block face
avatar = pygame.image.load(os.path.join("images", "avatar.png"))  # load the main character
pygame.display.set_icon(avatar)
#  this surface has an alpha value with the colors, so the player trail will fade away using opacity
alpha_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

# sprite groups
player_sprite = pygame.sprite.Group()
elements = pygame.sprite.Group()


#  ints
fill = 0
num = 0
CameraX = 0
attempts = 0
coins = 0
angle = 0
level = start_lvl

# list
particles = []
# orbs = []
win_cubes = []

# initialize level with


# set window title suitable for game
pygame.display.set_caption('Pydash: Geometry Dash in Python')

# initialize the font variable to draw text later
text = font.render('image', False, (255, 255, 0))

# music
# music = pygame.mixer_music.load(os.path.join("music", "bossfight-Vextron.mp3"))
# pygame.mixer_music.play()

# bg image
bg = pygame.image.load(os.path.join("images", "bg.png"))

# create object of player class
player = Player(elements, (250, 550), player_sprite)

# show tip on start and on death
tip = font.render("tip: tap and hold for the first few seconds of the level", True, BLUE)

while not done:
    keys = pygame.key.get_pressed()

    if not start:
        wait_for_key()
        reset()

        start = True

    player.vel.x = 10

    eval_outcome(player.win, player.died)
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        player.isjump = True
    elif keys[pygame.K_ESCAPE]:
        start = False
        pygame.mixer_music.stop()
        continue
    else:
        player.isjump = False

    # Reduce the alpha of all pixels on this surface each frame.
    # Control the fade2 speed with the alpha value.


    player_sprite.update()
    CameraX = player.vel.x  # for moving obstacles
    move_map()  # apply CameraX to all elements

    screen.fill((0,0,255))
    # screen.blit(bg, (0, 0))  # Clear the screen(with the bg)

    player.draw_particle_trail(player.rect.left - 1, player.rect.bottom + 2,
                               WHITE)
    draw_stats(screen)
 
    if player.isjump and player.type == CUBE:
        """rotate the player by an angle and blit it if player is jumping"""
        angle -= 8.1712  # this may be the angle needed to do a 360 deg turn in the length covered in one jump by player
        blitRotate(screen, player.image, player.rect.center, (16, 16), angle)
    else:
        """if player.isjump is false, then just blit it normally(by using Group().draw() for sprites"""
        player_sprite.draw(screen)  # draw player sprite group
    elements.draw(screen)  # draw all other obstacles

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
