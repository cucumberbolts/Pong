# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 2019

@author: alwaysPoondering
"""

import pygame  # Imports pygame
import random  # Imports random

# Sets things up
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480  # Defines screen size
SCREEN = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)  # Defines screen
BG_COLOUR = [0, 0, 0]  # Background colour
SCREEN.fill(BG_COLOUR)  # Fills screen with background colour
ICON = pygame.image.load("pong.ico")  # Icon
CAPTION = "Pong"  # Caption
PADDLE_IMAGE = "paddle.png"  # Defines paddle image
BALL_IMAGE = "Ball.png"  # Defines ball image
pygame.display.set_caption(CAPTION)  # Sets caption
pygame.display.set_icon(ICON)  # Sets icon

player_score = 0  # Player's score
computer_score = 0  # Computer's sccore
speed = 20  # Defines the speed the game plays at
pygame.key.set_repeat(speed, speed)  # Sets the key repeat speed

class Paddle(pygame.sprite.Sprite):
    """paddle class"""
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.dimensions = self.height, self.width = 30, 10

    def move(self, new_location):
        pygame.draw.rect(SCREEN, BG_COLOUR, self.rect)  # "Erases" current paddle
        self.rect.left, self.rect.top = new_location
        SCREEN.blit(self.image, self.rect)

class Ball(pygame.sprite.Sprite):
    """ball class"""
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.dimensions = self.height, self.width = 10, 10
        self.y_speed = random.randint(-(speed - 15), (speed - 15))
        self.x_speed = random.randint(-(speed - 15), (speed - 15))

    def move(self, new_location):
        pygame.draw.rect(SCREEN, BG_COLOUR, self.rect)  # "Erases current ball
        self.rect.left, self.rect.top = new_location
        SCREEN.blit(self.image, self.rect)

    def animate(self):
        self.move([self.rect.left + self.x_speed, self.rect.top + self.y_speed])


player = Paddle(PADDLE_IMAGE, [100, 100])  # Player instance
computer = Paddle(PADDLE_IMAGE, [540, 100])  # Computer instance
ball = Ball(BALL_IMAGE, [int(SCREEN_WIDTH / 2) - 5, int(SCREEN_HEIGHT / 2) - 5])  # Ball instance. Makes the ball start in the center

running = True

# Shows the stuff on the screen
SCREEN.blit(player.image, player.rect)
SCREEN.blit(computer.image, computer.rect)
SCREEN.blit(ball.image, ball.rect)

# Game loop thingy
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move([100, player.rect.top - 10])

                if player.rect.top < 0:  # If paddle is past the screen top...
                    player.move([100, 0])  # Move the paddle to the limit

            elif event.key == pygame.K_DOWN:
                player.move([100, player.rect.top + 10])

                if player.rect.top > SCREEN_HEIGHT - player.height:  # If paddle bottom is past the screen bottom...
                    player.move([100, SCREEN_HEIGHT - player.height])  # Move the paddle to the limit

    ball.animate()  # Animates ball

    # Bounces off the walls
    if self.rect.top <= 0:
        self.y_speed = -self.y_speed
    elif self.rect.left <= 0:
        self.x_speed = -self.x_speed
    elif self.rect.top + self.height >= SCREEN_HEIGHT:
        self.y_speed = -self.y_speed
    elif self.rect.left + self.width >= SCREEN_WIDTH:
        self.x_speed = -self.x_speed

    # Updates scores
    if ball.rect.left <= 0:
        computer_score += 1  # Adds 1 point to the computer's score
    elif ball.rect.left + ball.width >= SCREEN_WIDTH:
        player_score += 1  # Adds 1 poing to the player's score

    #computer.move([540, ball.rect.top])  # Moves the computer's paddle

    if pygame.sprite.collide_rect(player, ball):
        ball.x_speed = -ball.x_speed
        SCREEN.blit(player.image, player.rect)
    elif pygame.sprite.collide_rect(computer, ball):
        ball.x_speed = -ball.x_speed
        SCREEN.blit(computer.image, computer.rect)

    pygame.time.delay(speed)  # Sets the game speed

    pygame.display.flip()  # uhh... refreshes the display?? I'm not entirely sure...

pygame.quit()  # Quits the game
print(f"computer's score: {computer_score}")
print(f"player's score: {player_score}")
