import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 10
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Fonts
font = pygame.font.Font(None, 36)

# Paddle X positions (defined once, used consistently)
LEFT_PADDLE_X = 10
RIGHT_PADDLE_X = SCREEN_WIDTH - 20  # Fix: was inconsistent between draw and collision

# Game variables
left_paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
right_paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y
left_score = 0
right_score = 0
winning_score = 5

def reset_ball(direction):
    """Reset ball to center with given x direction and random y direction."""
    return (
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT // 2,
        BALL_SPEED_X * direction,
        BALL_SPEED_Y * random.choice([-1, 1])  # Fix: randomize Y on reset
    )

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top/bottom
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_dy = -ball_dy

    # Ball collision with paddles — Fix: use named constants so draw and collision match
    left_paddle_hit = (
        LEFT_PADDLE_X <= ball_x <= LEFT_PADDLE_X + PADDLE_WIDTH and
        left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT
    )
    right_paddle_hit = (
        RIGHT_PADDLE_X <= ball_x + BALL_SIZE <= RIGHT_PADDLE_X + PADDLE_WIDTH and
        right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT
    )
    if left_paddle_hit or right_paddle_hit:
        ball_dx = -ball_dx

    # Scoring
    if ball_x < 0:
        right_score += 1
        ball_x, ball_y, ball_dx, ball_dy = reset_ball(1)
    if ball_x > SCREEN_WIDTH:
        left_score += 1
        ball_x, ball_y, ball_dx, ball_dy = reset_ball(-1)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (LEFT_PADDLE_X, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (RIGHT_PADDLE_X, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(right_text, (3 * SCREEN_WIDTH // 4, 20))

    # Check for winner — Fix: use continue/break to avoid double flip
    if left_score >= winning_score or right_score >= winning_score:
        winner_text = "Player 1 Wins!" if left_score >= winning_score else "Player 2 Wins!"
        screen.fill(BLACK)
        winner_render = font.render(winner_text, True, WHITE)
        screen.blit(winner_render, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()  # Only flip once here, then exit
        pygame.time.wait(3000)
        running = False
        continue  # Fix: skip the flip at the bottom of the loop

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()