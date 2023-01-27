import pygame

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the background color
screen.fill((255, 255, 255))

# Define the dog's body
dog_body = pygame.Rect(250, 350, 200, 150)
pygame.draw.ellipse(screen, (255, 0, 0), dog_body)

# Define the dog's head
dog_head = pygame.Rect(325, 250, 50, 50)
pygame.draw.ellipse(screen, (255, 0, 0), dog_head)

# Define the dog's ears
dog_ear1 = pygame.Rect(310, 250, 25, 25)
pygame.draw.ellipse(screen, (255, 0, 0), dog_ear1)
dog_ear2 = pygame.Rect(360, 250, 25, 25)
pygame.draw.ellipse(screen, (255, 0, 0), dog_ear2)

# Define the dog's eyes
dog_eye1 = pygame.Rect(332, 260, 10, 10)
pygame.draw.ellipse(screen, (0, 0, 0), dog_eye1)
dog_eye2 = pygame.Rect(347, 260, 10, 10)
pygame.draw.ellipse(screen, (0, 0, 0), dog_eye2)

# Define the dog's nose
dog_nose = pygame.Rect(340, 270, 10, 10)
pygame.draw.ellipse(screen, (0, 0, 0), dog_nose)

# Define the dog's mouth
dog_mouth = pygame.Rect(335, 285, 20, 5)
pygame.draw.rect(screen, (0, 0, 0), dog_mouth)

# Update the screen
pygame
