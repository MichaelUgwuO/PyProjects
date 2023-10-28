# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    snake_game.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mugwu <mugwu@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/11 04:16:55 by mugwu             #+#    #+#              #
#    Updated: 2023/10/28 15:18:56 by mugwu            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Snake properties
snake_size = 20
snake_speed = 10
snake_x, snake_y = width // 2, height // 2
snake_x_change, snake_y_change = 0, 0
snake_body = [(snake_x, snake_y)]

# Food properties
food_size = 20
food_x = random.randrange(0, width - food_size, food_size)
food_y = random.randrange(0, height - food_size, food_size)

# Score
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -snake_size
            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = snake_size

    # Update snake'ss position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collisions with the screen edges
    if (
        snake_x >= width
        or snake_x < 0
        or snake_y >= height
        or snake_y < 0
    ):
        running = False

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randrange(0, width - food_size, food_size)
        food_y = random.randrange(0, height - food_size, food_size)
    else:
        snake_body.pop(0)

    # Check for self-collision
    if (snake_x, snake_y) in snake_body:
        running = False

    # Add the snake's current position to its body
    snake_body.append((snake_x, snake_y))

    # Clear the screen
    screen.fill(black)

    # Draw food
    pygame.draw.rect(screen, green, (food_x, food_y, food_size, food_size))

    # Draw snake
    for segment in snake_body:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

    pygame.display.update()

    # Control the game speed
    pygame.time.Clock().tick(snake_speed)

# Quit Pygame
pygame.quit()
sys.exit()
