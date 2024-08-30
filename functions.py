
import pygame
import random

def draw_snake(screen, snake_body, block_size):
    for block in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(block[0], block[1], block_size, block_size))

def generate_food(snake_body, screen_width, screen_height, block_size):
    while True:
        x = random.randint(0, (screen_width - block_size) // block_size) * block_size
        y = random.randint(0, (screen_height - block_size) // block_size) * block_size
        if [x, y] not in snake_body:
            return x, y

def check_collision(snake_head, snake_body):
    if snake_head in snake_body[1:]:
        return True
    return False

def draw_text(screen, text, size, color, position):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
