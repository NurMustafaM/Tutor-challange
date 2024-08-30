import pygame
import sys
from functions import draw_snake, generate_food, check_collision, draw_text

# Initialize PyGame
pygame.init()

# Screen settings
screen_width = 600
screen_height = 400
block_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Game settings
snake_speed = 5
snake_body = [[100, 100], [80, 100], [60, 100]]
snake_direction = 'RIGHT'
food_position = generate_food(snake_body, screen_width, screen_height, block_size)
score = 0

def main_menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, 'Snake Game', 40, (255, 255, 255), (screen_width // 4, screen_height // 4))
        draw_text(screen, 'Press any key to start', 30, (255, 255, 255), (screen_width // 4, screen_height // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

def game_loop():
    global snake_body, snake_direction, food_position, score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'
                elif event.key == pygame.K_UP and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif event.key == pygame.K_p:
                    pause_menu()

        if snake_direction == 'LEFT':
            snake_head = [snake_body[0][0] - block_size, snake_body[0][1]]
        elif snake_direction == 'RIGHT':
            snake_head = [snake_body[0][0] + block_size, snake_body[0][1]]
        elif snake_direction == 'UP':
            snake_head = [snake_body[0][0], snake_body[0][1] - block_size]
        elif snake_direction == 'DOWN':
            snake_head = [snake_body[0][0], snake_body[0][1] + block_size]

        snake_body.insert(0, snake_head)

        if snake_head == list(food_position):
            food_position = generate_food(snake_body, screen_width, screen_height, block_size)
            score += 10
        else:
            snake_body.pop()

        if (snake_head[0] < 0 or snake_head[0] >= screen_width or
            snake_head[1] < 0 or snake_head[1] >= screen_height or
            check_collision(snake_head, snake_body)):
            return

        screen.fill((0, 0, 0))
        draw_snake(screen, snake_body, block_size)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_position[0], food_position[1], block_size, block_size))
        draw_text(screen, f'Score: {score}', 30, (255, 255, 255), (10, 10))
        pygame.display.flip()
        clock.tick(snake_speed)

def pause_menu():
    while True:
        draw_text(screen, 'Paused', 40, (255, 255, 255), (screen_width // 4, screen_height // 4))
        draw_text(screen, 'Press "R" to resume', 30, (255, 255, 255), (screen_width // 4, screen_height // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return

if __name__ == '__main__':
    main_menu()
    game_loop()

