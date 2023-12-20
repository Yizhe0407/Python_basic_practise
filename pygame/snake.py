import pygame
import sys
import random

pygame.init()

window_size = 500
grid_size = 20
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Snake Game")

black = (0, 0, 0)

snake_size = 20
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
speed = 10

food_pos = [round(random.randrange(1, (window_size // snake_size)) * snake_size),
            round(random.randrange(1, (window_size // snake_size)) * snake_size)]

food_spawn = True
score = 0


class Snake:
    def __init__(self):
        self.color = (144, 238, 144)


snake = Snake()


def draw_snake(snake_body):
    for i, pos in enumerate(snake_body):
        if i == 0:
            pygame.draw.rect(window, snake.color, pygame.Rect(
                pos[0], pos[1], snake_size, snake_size))
        else:
            color_ratio = i / len(snake_body)
            color = (
                snake.color[0] - int(snake.color[0] * color_ratio),
                snake.color[1] - int(snake.color[1] * color_ratio),
                snake.color[2] - int(snake.color[2] * color_ratio)
            )
            pygame.draw.rect(window, color, pygame.Rect(
                pos[0], pos[1], snake_size, snake_size))


def draw_food(food_pos):
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(
        food_pos[0], food_pos[1], snake_size, snake_size))


def draw_score(score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))


def check_collision(snake_head, snake_body):
    for segment in snake_body[1:]:
        if snake_head[0] == segment[0] and snake_head[1] == segment[1]:
            return True
    return False


def draw_grid():
    grid_color = (50, 50, 50)
    for x in range(0, window_size, grid_size):
        pygame.draw.line(window, grid_color, (x, 0), (x, window_size))
    for y in range(0, window_size, grid_size):
        pygame.draw.line(window, grid_color, (0, y), (window_size, y))


def start_screen():
    font = pygame.font.Font(None, 48)
    title_text = font.render("Snake Game", True, (255, 255, 255))
    instruction_text = font.render("Press any key to start", True, (255, 255, 255))

    title_text_rect = title_text.get_rect(center=(window_size // 2, window_size // 3))
    instruction_text_rect = instruction_text.get_rect(center=(window_size // 2, window_size // 2))

    window.fill(black)
    window.blit(title_text, title_text_rect)
    window.blit(instruction_text, instruction_text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


# Display start screen
start_screen()

# Create a clock outside the game loop
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not direction == 'DOWN':
                change_to = 'UP'
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not direction == 'UP':
                change_to = 'DOWN'
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not direction == 'RIGHT':
                change_to = 'LEFT'
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not direction == 'LEFT':
                change_to = 'RIGHT'

    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= snake_size
        snake_pos[1] = round(snake_pos[1] / snake_size) * snake_size
    if direction == 'DOWN':
        snake_pos[1] += snake_size
        snake_pos[1] = round(snake_pos[1] / snake_size) * snake_size
    if direction == 'LEFT':
        snake_pos[0] -= snake_size
        snake_pos[0] = round(snake_pos[0] / snake_size) * snake_size
    if direction == 'RIGHT':
        snake_pos[0] += snake_size
        snake_pos[0] = round(snake_pos[0] / snake_size) * snake_size

    if (
        snake_pos[0] < 0 or
        snake_pos[0] >= window_size or
        snake_pos[1] < 0 or
        snake_pos[1] >= window_size or
        check_collision(snake_pos, snake_body)
    ):
        pygame.quit()
        sys.exit()

    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] in range(food_pos[0], food_pos[0] + snake_size) and snake_pos[1] in range(food_pos[1], food_pos[1] + snake_size):
        food_spawn = False
        score += 1
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [round(random.randrange(1, (window_size // snake_size)) * snake_size),
                    round(random.randrange(1, (window_size // snake_size)) * snake_size)]
        food_spawn = True

    if score >= 30 and window_size == 500:
        window_size = 700
        window = pygame.display.set_mode((window_size, window_size))

    window.fill(black)
    draw_grid()
    draw_snake(snake_body)
    draw_food(food_pos)
    draw_score(score)

    pygame.display.flip()

    # Use the clock to control the frame rate
    clock.tick(speed)
