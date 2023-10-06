import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window_size = (window_width, window_height)
game_window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up snake
snake_block_size = 20
snake_speed = 15
snake_x = window_width // 2
snake_y = window_height // 2
snake_x_change = 0
snake_y_change = 0
snake_body = []
snake_length = 1

# Set up food
food_block_size = 20
food_x = round(random.randrange(0, window_width - food_block_size) / 20) * 20
food_y = round(random.randrange(0, window_height - food_block_size) / 20) * 20

# Set up score
score_font = pygame.font.SysFont(None, 36)

# Function to draw the snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(game_window, GREEN, [block[0], block[1], snake_block_size, snake_block_size])

# Function to display the score
def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, WHITE)
    game_window.blit(score_text, (10, 10))

# Game loop
running = True
game_over = False
while running:
    while game_over:
        game_window.fill(BLACK)
        game_over_text = score_font.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
        game_window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    game_over = False
                if event.key == pygame.K_c:
                    snake_x = window_width // 2
                    snake_y = window_height // 2
                    snake_x_change = 0
                    snake_y_change = 0
                    snake_body = []
                    snake_length = 1
                    food_x = round(random.randrange(0, window_width - food_block_size) / 20) * 20
                    food_y = round(random.randrange(0, window_height - food_block_size) / 20) * 20
                    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_x_change != snake_block_size:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT and snake_x_change != -snake_block_size:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP and snake_y_change != snake_block_size:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN and snake_y_change != -snake_block_size:
                snake_y_change = snake_block_size
                snake_x_change = 0

    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    snake_x += snake_x_change
    snake_y += snake_y_change
    game_window.fill(BLACK)

    pygame.draw.rect(game_window, RED, [food_x, food_y, food_block_size, food_block_size])
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    for block in snake_body[:-1]:
        if block == snake_head:
            game_over = True

    draw_snake(snake_body)
    show_score(snake_length - 1)

    pygame.display.update()

    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - food_block_size) / 20) * 20
        food_y = round(random.randrange(0, window_height - food_block_size) / 20) * 20
        snake_length += 1

    pygame.time.Clock().tick(snake_speed)

# Quit the game
pygame.quit()