import pygame
import sys

pygame.init()

# Window setup
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My first game screen")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 30)
text = font.render("Hello, Pygame!", True, WHITE)

# Rectangle (center)
rect = pygame.Rect(width//2 - 75, height//2 - 50, 150, 100)

# -------- Custom Event --------
SPACE_EVENT = pygame.USEREVENT + 1

# -------- Sprite Class --------
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self):
        self.rect.y -= 10  # move up when event triggered

# Create sprites
sprite1 = MySprite(RED, 100, 300)
sprite2 = MySprite(GREEN, 500, 300)

sprites = pygame.sprite.Group(sprite1, sprite2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect SPACE key press → post custom event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.event.post(pygame.event.Event(SPACE_EVENT))

        # Handle custom event
        elif event.type == SPACE_EVENT:
            print("Space event triggered!")
            for sprite in sprites:
                sprite.move()

    # Background
    screen.fill(BLACK)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rect)

    # Draw text
    text_rect = text.get_rect(center=(width // 2, 50))
    screen.blit(text, text_rect)

    # Draw sprites
    sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()