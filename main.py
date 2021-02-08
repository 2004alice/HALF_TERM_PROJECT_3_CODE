import pygame

pygame.init()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

DISPLAY = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
FPSCLOCK = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (90, 0, 90)
'''left = 30
top = 30
width = 30
height = 30'''
x_speed = 5
y_speed = 5


class MainCharacter(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        pygame.draw.rect(DISPLAY, green, (30, 30, 30, 30))
        self.rect = self.image.get_rect()
        self.max_health = 10
        self.attack_damage = 2
        self.move_speed = 30
        self.name = MainCharacter
        self.current_health = 10

    def move_right(self, pixels):
        self.rect.x += pixels

    def move_left(self, pixels):
        self.rect.x -= pixels


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        pygame.draw.rect(DISPLAY, red, (100, 100, 30, 30))
        self.rect = self.image.get_rect()
        self.health = 6
        self.move_speed = 20


class Attack(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        pygame.draw.rect(DISPLAY, purple, (200, 200, 35, 10))
        self.rect = self.image.get_rect()
        self.damage = 2
        self.mode = "melee"
        self.count = None
        self.move_speed = None
        self.direction = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            MainCharacter.move_left(self, 5)
        if keys[pygame.K_RIGHT]:
            MainCharacter.move_right(self, 5)
    DISPLAY.fill((0, 0, 0))

    MainCharacter()
    Enemy()
    Attack()

    pygame.display.update()
    FPSCLOCK.tick(20)
