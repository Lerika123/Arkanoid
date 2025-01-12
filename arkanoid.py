import pygame

pygame.init()
pygame.display.set_caption('Шарики')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

c = (250, 250)
running = True
v = 100
fps = 100
clock = pygame.time.Clock()
circles = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            c = event.pos
            if 10 < c[0] < 490 and 10 < c[1] < 490:
                circles.append(list(c) + [-1, -1])
    screen.fill((0, 0, 0))
    for x in circles:
        if x[1] < 10 or x[1] > 490:
            x[3] *= -1
        if x[0] < 10 or x[0] > 490:
            x[2] *= -1
        x[0] += x[2]
        x[1] += x[3]
        pygame.draw.circle(screen, 'white', (x[0], x[1]), 10)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
