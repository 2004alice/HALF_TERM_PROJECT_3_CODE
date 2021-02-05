import pygame

pygame.init()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

DISPLAY = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
FPSCLOCK = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
left = 30
top = 30
width = 30
height = 30
x_speed = 5
y_speed = 5


class MainCharacter(pygame.sprite.Sprite):

    def __init__(self, width, height, health):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.max_health = health
        self.max_health = None
        self.attack_damage = None
        self.move_speed = None
        self.name = None
        self.current_health = None

    def health(self):
        max_health = 3
        if left + width >= WINDOWWIDTH:
            max_health = - 1
        elif top + height >= WINDOWHEIGHT:
            max_health = - 1

        if max_health == 0:
            quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    DISPLAY.fill((0, 0, 0))
    pygame.draw.rect(DISPLAY, white, (left, top, width, height))

    left += x_speed
    if left + width >= WINDOWWIDTH:
        x_speed *= -1
    if left <= 0:
        x_speed *= -1

    top += y_speed
    if top + height >= WINDOWHEIGHT:
        y_speed *= -1
    if top <= 0:
        y_speed *= -1

    pygame.display.update()
    FPSCLOCK.tick(20)