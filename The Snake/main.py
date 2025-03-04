import pygame
from random import randrange

# Constants
RES = 850
SIZE = 50

# Coordinates of the snake and apple
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

dirs = {'W': True, 'S': True, 'A': True, 'D': True} # Directions
length = 1 # Snake length
snake = [(x, y)] # Snake body
dx, dy = 0, 0 # Snake movement
fps = 5 # Snake speed

pygame.init()
sc = pygame.display.set_mode([RES, RES])

clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black')) # Background
    # Snake
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    # Apple
    [(pygame.draw.rect(sc, pygame.Color('red'), (i, j, SIZE, SIZE))) for i, j in [apple]]

    # Snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # Eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1


    # Game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
      break
    if len(snake) != len(set(snake)):
      break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get(): # Event handling
        if event.type == pygame.QUIT:
            exit()

    # Control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0,
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}