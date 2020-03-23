# https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
# Pygame Tutorial #2 - Jumping and Boundaries
import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

# These go near the top of your program, outside the while loop
isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Making sure the top left corner of our character is greater than our vel so we never move off the screen
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    # Making sure the top right corner of our character is less than the screen width - its width
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel

    # Checks is user is not jumping
    if not (isJump):
        # Same principles apply for the y coordinate
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        # Goes inside the while loop, under event for moving down
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        # This is what will happen if we are jumping
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        # This will execute if our jump is finished
        else:
            jumpCount = 10
            isJump = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()