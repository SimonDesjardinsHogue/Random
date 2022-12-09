import pygame

# Set the screen size
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the game window
pygame.display.set_caption('My Game')

# Set the background color
screen.fill((0, 0, 0))

# Load an image
image = pygame.image.load('player.png')

# Set the initial position of the image
x = 100
y = 100

# Set the initial speed of the image
speed_x = 0
speed_y = 0

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Set the speed of the image based on the user's input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            elif event.key == pygame.K_RIGHT:
                speed_x = 3
            elif event.key == pygame.K_UP:
                speed_y = -3
            elif event.key == pygame.K_DOWN:
                speed_y = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0

    # Update the position of the image
    x += speed_x
    y += speed_y

    # Draw the background
    screen.fill((0, 0, 0))

    # Draw the image
    screen.blit(image, (x, y))

    # Update the display
    pygame.display.flip()
