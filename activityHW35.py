import pygame
import sys

# Initialize pygame
pygame.init()

# Window size
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Set caption
pygame.display.set_caption("My first game screen")

# Colors
BLACK = (0, 0, 0)      # Background (note: this is actually black, not white)
BLUE = (0, 128, 255)   # Rectangle color
WHITE = (255, 255, 255)

# Font setup
font = pygame.font.SysFont("Arial", 30)
text = font.render("Hello, Pygame!", True, WHITE)

# Rectangle setup (centered)
rect_width, rect_height = 150, 100
rect_x = (width - rect_width) // 2
rect_y = (height - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BLACK)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rectangle)

    # Draw text (top center)
    text_rect = text.get_rect(center=(width // 2, 50))
    screen.blit(text, text_rect)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
