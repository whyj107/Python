import os
import pygame
import glob

SIZE = WIDTH, HEIGHT = 1024, 600  # the width and height of our screen
FPS = 40  # Frames per second

class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super(MySprite, self).__init__()
        os_path = os.getcwd()
        im = glob.glob(os.path.join(os_path, 'png', f"{action}*.png"))
        im.sort()
        lenim = len(im[0])

        tmp = []
        self.images = []
        self.images2 = []
        for img in glob.glob(os.path.join(os_path, 'png', f'{action}*.png')):
            tmp.append(img)

        tmp.sort()

        for i in tmp:
            # print(i, len(i), lenim)
            if len(i) == lenim:
                self.images.append(pygame.image.load(i))
            if len(i) > lenim:
                self.images2.append(pygame.image.load(i))

        self.index = 0
        # original : 150 198
        self.rect = pygame.Rect(275, 0, 50, 66)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1


def create_sprites():
    idle = pygame.sprite.Group(MySprite("Idle"))
    walk = pygame.sprite.Group(MySprite("Walk"))
    run = pygame.sprite.Group(MySprite("Run"))
    jump = pygame.sprite.Group(MySprite("Jump"))
    dead = pygame.sprite.Group(MySprite("Dead"))
    return idle, walk, run, jump, dead


def main():
    global clock
    global font

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    idle, walk, run, jump, dead = create_sprites()
    # 처음 시작 상태
    my_group = idle
    # clock 오브젝트 생성
    clock = pygame.time.Clock()
    loop = 1
    while loop:
        print(f"tick:{clock.tick(FPS)}    fps:{clock.get_fps()}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: my_group = walk
                if event.key == pygame.K_d: my_group = dead
                if event.key == pygame.K_UP: my_group = jump
                if event.key == pygame.K_SPACE: my_group = idle
                if event.key == pygame.K_RIGHT: my_group = run
                if event.key == pygame.K_DOWN: my_group = dead

        my_group.update()
        # 배경 색
        screen.fill((0, 0, 0))
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
    # https://pythonprogramming.altervista.org/pygame-sprite-animation-update/?doing_wp_cron=1584930271.1399350166320800781250