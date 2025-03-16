import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Font for displaying score
font = pygame.font.Font(None, 36)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5
        self.shoot_delay = 250  # Delay between shots in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # Move player left and right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        # Shoot bullets with a delay
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10  # Bullets move upwards

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:  # Remove bullet if it goes off screen
            self.kill()

# Regular enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 5)
        self.direction = 1  # 1 = right, -1 = left

    def update(self):
        # Move enemy down and side to side
        self.rect.y += self.speed
        self.rect.x += self.direction * 2
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:  # Change direction at screen edges
            self.direction *= -1
        if self.rect.top > SCREEN_HEIGHT + 10:  # Respawn enemy if it goes off screen
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 5)

# Fast enemy class
class FastEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed = random.randrange(2, 5)  # Slightly slower than before
        self.direction = 1

    def update(self):
        # Move fast enemy down and side to side
        self.rect.y += self.speed
        self.rect.x += self.direction * 3
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speed = random.randrange(2, 5)

# Strong enemy class
class StrongEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-200, -150)
        self.speed = random.randrange(1, 3)
        self.direction = 1
        self.health = 3  # Strong enemies require 3 hits to destroy

    def update(self):
        # Move strong enemy down and side to side
        self.rect.y += self.speed
        self.rect.x += self.direction * 1
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-200, -150)
            self.speed = random.randrange(1, 3)
            self.health = 3

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
fast_enemies = pygame.sprite.Group()
strong_enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create regular enemies
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Create fast enemies
for i in range(3):
    fast_enemy = FastEnemy()
    all_sprites.add(fast_enemy)
    fast_enemies.add(fast_enemy)

# Create strong enemies
for i in range(2):
    strong_enemy = StrongEnemy()
    all_sprites.add(strong_enemy)
    strong_enemies.add(strong_enemy)

# Score variables
score = 0
time_score = 0  # Points earned over time
last_time = pygame.time.get_ticks()  # Time tracking for survival points

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update all sprites
    all_sprites.update()

    # Add points for survival (5 points per second)
    now = pygame.time.get_ticks()
    if now - last_time > 1000:
        time_score += 5
        last_time = now

    # Check for collisions between bullets and regular enemies
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 10
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Check for collisions between bullets and fast enemies
    hits = pygame.sprite.groupcollide(fast_enemies, bullets, True, True)
    for hit in hits:
        score += 20
        fast_enemy = FastEnemy()
        all_sprites.add(fast_enemy)
        fast_enemies.add(fast_enemy)

    # Check for collisions between bullets and strong enemies
    hits = pygame.sprite.groupcollide(strong_enemies, bullets, False, True)
    for hit in hits:
        hit.health -= 1
        if hit.health <= 0:
            score += 30
            hit.kill()
            strong_enemy = StrongEnemy()
            all_sprites.add(strong_enemy)
            strong_enemies.add(strong_enemy)

    # Check for collisions between player and enemies
    if pygame.sprite.spritecollide(player, enemies, False) or \
        pygame.sprite.spritecollide(player, fast_enemies, False) or \
        pygame.sprite.spritecollide(player, strong_enemies, False):
        running = False

    # Render the game
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display total score
    total_score = score + time_score
    score_text = font.render(f"Score: {total_score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

# Game over screen
screen.fill(BLACK)
game_over_text = font.render(f"Game Over! Your Score: {total_score}", True, WHITE)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)  # Wait 3 seconds before closing

pygame.quit()
sys.exit()