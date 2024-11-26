import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 100
        
        # Movement physics
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_jumping = False
        self.score = 0
        
    def update(self, platforms):
        # Apply gravity
        self.velocity_y += 0.5
        
        # Move horizontally
        self.rect.x += self.velocity_x
        
        # Check horizontal collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_x > 0:
                    self.rect.right = platform.rect.left
                elif self.velocity_x < 0:
                    self.rect.left = platform.rect.right
        
        # Move vertically
        self.rect.y += self.velocity_y
        
        # Check vertical collisions
        self.is_jumping = True
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.is_jumping = False
                elif self.velocity_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
        
        # Screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity_y = 0
            self.is_jumping = False

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, patrol_distance):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.patrol_distance = patrol_distance
        self.direction = 1
        self.speed = 2

    def update(self):
        self.rect.x += self.speed * self.direction
        if abs(self.rect.x - self.start_x) > self.patrol_distance:
            self.direction *= -1

def main():
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Create platforms
    platform_list = [
        (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),  # Ground
        (300, 450, 200, 20),
        (100, 350, 200, 20),
        (500, 250, 200, 20),
        (200, 150, 200, 20),
    ]

    for plat in platform_list:
        platform = Platform(*plat)
        platforms.add(platform)
        all_sprites.add(platform)

    # Create coins
    coin_positions = [
        (350, 400),
        (150, 300),
        (550, 200),
        (250, 100),
    ]

    for pos in coin_positions:
        coin = Coin(*pos)
        coins.add(coin)
        all_sprites.add(coin)

    # Create enemies
    enemy_data = [
        (400, 420, 100),
        (200, 320, 100),
        (600, 220, 100),
    ]

    for enemy_pos in enemy_data:
        enemy = Enemy(*enemy_pos)
        enemies.add(enemy)
        all_sprites.add(enemy)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not player.is_jumping:
                    player.velocity_y = -12
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Handle continuous keyboard input
        keys = pygame.key.get_pressed()
        player.velocity_x = 0
        if keys[pygame.K_LEFT]:
            player.velocity_x = -5
        if keys[pygame.K_RIGHT]:
            player.velocity_x = 5

        # Update
        player.update(platforms)
        enemies.update()

        # Coin collection
        coin_hits = pygame.sprite.spritecollide(player, coins, True)
        for coin in coin_hits:
            player.score += 10

        # Enemy collision
        enemy_hits = pygame.sprite.spritecollide(player, enemies, False)
        if enemy_hits:
            running = False

        # Draw
        SCREEN.fill(WHITE)
        all_sprites.draw(SCREEN)
        
        # Draw score
        score_text = font.render(f'Score: {player.score}', True, BLACK)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # Game over screen
    SCREEN.fill(WHITE)
    game_over_text = font.render(f'Game Over! Final Score: {player.score}', True, BLACK)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    SCREEN.blit(game_over_text, text_rect)
    pygame.display.flip()
    
    # Wait a few seconds before closing
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
