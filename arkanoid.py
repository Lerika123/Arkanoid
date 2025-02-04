import pygame


pipe_x = 400
pipe_y = 420


def load_image(name):
    image = pygame.image.load(f"{'data'}/{name}")
    return image


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Шарики')

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite(all_sprites)
sprite.image = pygame.transform.rotate(load_image("platform.png").convert_alpha(), 0)
sprite.rect = sprite.image.get_rect()
clock = pygame.time.Clock()
running = True
c = (250, 100)
circles = []
f = 1
s = 2
while running:
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            sprite.rect.left -= 10
        if key[pygame.K_RIGHT]:
            sprite.rect.left += 10
    screen.fill('black')
    if f:
        circles.append(list(c) + [1, 1])
        f = 0
    for x in circles:
        if x[1] < 10 or x[1] > 490:
            x[3] *= -1
        if x[0] < 10 or x[0] > 490:
            x[2] *= -1
        if sprite.image.overlap_area(circles[:2], offset) > 0:
        x[0] += x[2]
        x[1] += x[3]
        pygame.draw.circle(screen, 'white', (x[0], x[1]), 10)
    pipe_x -= s
    if pipe_x == -24:
        s = -2
    if pipe_x == 380:
        s = 2
    screen.blit(sprite.image, (pipe_x, pipe_y))
    # all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
