# https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
# Pygame Tutorial #3 - Character Animation & Sprites
import pygame
pygame.init()
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('png/Run (01).png'), pygame.image.load('png/Run (02).png'), pygame.image.load('png/Run (03).png'),
             pygame.image.load('png/Run (04).png'), pygame.image.load('png/Run (05).png'), pygame.image.load('png/Run (06).png'),
             pygame.image.load('png/Run (07).png'), pygame.image.load('png/Run (08).png'), pygame.image.load('png/Run (09).png'),
             pygame.image.load('png/Run (10).png'), pygame.image.load('png/Run (11).png'), pygame.image.load('png/Run (12).png'),
             pygame.image.load('png/Run (13).png'), pygame.image.load('png/Run (14).png'), pygame.image.load('png/Run (15).png')]
walkLeft = [pygame.image.load('png/Walk (01).png'), pygame.image.load('png/Walk (02).png'), pygame.image.load('png/Walk (03).png'),
            pygame.image.load('png/Walk (04).png'), pygame.image.load('png/Walk (05).png'), pygame.image.load('png/Walk (06).png'),
            pygame.image.load('png/Walk (07).png'), pygame.image.load('png/Walk (08).png'), pygame.image.load('png/Walk (09).png'),
            pygame.image.load('png/Walk (10).png'), pygame.image.load('png/Walk (11).png'), pygame.image.load('png/Walk (12).png'),
            pygame.image.load('png/Walk (13).png'), pygame.image.load('png/Walk (14).png'), pygame.image.load('png/Walk (15).png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('png/Idle (01).png')

x = 0
y = 0
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()