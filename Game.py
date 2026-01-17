import pygame
from Food import Food

class Game:
    def __init__(self):
        pygame.init()
        
        self.score = 0
        self.food = Food()
        self.entities = [self.food, self.snake]

    