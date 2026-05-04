import pygame
import sys

# Initialize pygame
pygame.init()

# 1. Window size (500, 500)
screen = pygame.display.set_mode((500, 500))

# 2. Set caption
pygame.display.set_caption("My first game screen")

# 4. Background color (Grey)
bg_color = (58, 58, 58)

# Load image (replace 'image.png' with your image file)
image = pygame.image.load("image.png")

# 3. Resize image to (300, 300)
image = pygame.transform.scale(image, (300, 300))

# Get rectangle and center it
image_rect = image.get_rect(center=(250, 250))  # center of 500x500 window

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill background
    screen.fill(bg_color)

    # Draw image at center
    screen.blit(image, image_rect)

    # Update display
    pygame.display.update()