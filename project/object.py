

import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Food:
    def __init__(self, game_screen):
        self.apple = pygame.image.load("resources/3-removebg-preview.png")
        self.hamburger = pygame.image.load("resources/1-removebg-preview.png")
        self.cake = pygame.image.load("resources/2-removebg-preview.png")
        self.water_melons = pygame.image.load("resources/4-removebg-preview.png")
        self.image = random.choice([self.apple, self.hamburger, self.cake, self.water_melons])
        self.parent_screen = game_screen
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.image = random.choice([self.apple, self.hamburger, self.cake, self.water_melons])
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.image2 = pygame.image.load("resources/5-removebg-preview.png").convert_alpha()
        self.image3 = pygame.image.load("resources/6-removebg-preview.png").convert_alpha()
        self.image4 = pygame.image.load("resources/7-removebg-preview.png").convert_alpha()
        self.image5 = pygame.image.load("resources/8-removebg-preview.png").convert_alpha()
        self.direction = random.choice(['up', 'down', 'left', 'right'])

        #snake do not spawn at edge of border
        self.length = 1
        self.x = [random.randint(3,20)*SIZE]
        self.y = [random.randint(3,15)*SIZE]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body : tail move first till the second
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head: time for first block move(head of snake)
        if self.direction == 'left':
            self.x[0] -= SIZE 
        if self.direction == 'right':
            self.x[0] += SIZE 
        if self.direction == 'up':
            self.y[0] -= SIZE 
        if self.direction == 'down':
            self.y[0] += SIZE 

        self.draw()

    #work like frame to cover old frame
    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    #the value of append is not important (lenght is the key)
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

        if self.length > 60:
            self.image = self.image5
        elif self.length > 45:
            self.image = self.image4
        elif self.length > 30:
            self.image = self.image3           
        elif self.length > 15:
            self.image = self.image2
        
        
        
