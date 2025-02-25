import pygame


def load_image(name):
    image = pygame.image.load(f"{'data'}/{name}")
    return image


class Start():
    pygame.init()

    font = pygame.font.SysFont("Risk", 72)

    text = font.render("Start Game", True, (0, 128, 0))

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Заставка игры')

    all_sprites = pygame.sprite.Group()

    size = pygame.display.get_window_size()
    clock = pygame.time.Clock()
    running = True
    while running:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        screen.fill('black')
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - text.get_height() // 2))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        pygame.time.wait(10)
    pygame.quit()


class Arkanoid():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Арканоид')

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = pygame.transform.rotate(load_image("platform.png").convert_alpha(), 0)
    sprite.rect = sprite.image.get_rect()
    size = pygame.display.get_window_size()
    sprite.rect[0] = platform_x = size[0] - 100
    sprite.rect[1] = platform_y = size[1] - 80
    clock = pygame.time.Clock()
    running = True
    c = (100, 10)
    f = 1
    s = 2
    r = 0
    while running:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                s *= -1
            key = pygame.key.get_pressed()
        screen.fill('black')
        if f:
            circles = list(c) + [1, 1]
            f = 0
        if circles[0] < 10 or circles[0] > size[0] - 10:
            circles[2] *= -1
        if circles[1] < 10 or circles[1] > size[1] - 10:
            circles[3] *= -1
        circles[0] += circles[2]
        circles[1] += circles[3]
        if (max(platform_x, circles[0], platform_x + 148, circles[0] + 10) - min(platform_x, circles[0],
                platform_x + 148, circles[0] + 10) <= 148 + 10 and circles[1] >= size[1] - 35):
            circles[3] *= -1
        pygame.draw.circle(screen, 'white', (circles[0], circles[1]), 10)
        platform_x -= s
        if platform_x == -24:
            s = -2
        if platform_x == size[0] - 120:
            s = 2
        if circles[1] == size[1] - 10:
            r += 1
            print(size)
            break
        screen.blit(sprite.image, (platform_x, platform_y))
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()


class OverGame():
    pygame.init()

    font = pygame.font.SysFont("Risk", 72)

    text = font.render("Game Over", True, (0, 128, 0))

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Игра окончена')

    all_sprites = pygame.sprite.Group()

    size = pygame.display.get_window_size()
    clock = pygame.time.Clock()
    running = True
    while running:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        screen.fill('black')
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - text.get_height() // 2))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        pygame.time.wait(10)
    pygame.quit()
