import pygame
import random
import MovingEntity
import Entity


class Food(Entity):
    def __init__(self):
        """Initialize the food object."""
        self._x = 0
        self._y = 0

    def draw(self, screen):
        """Draw the food on the screen.
        
        args:
            screen: The pygame screen surface where the food will be drawn.
        """

        cell = MovingEntity.CELL_SIZE
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, cell, cell))


        pass

    def pos(self):
        """Return the current position of the food."""

        return (self.x, self.y)

    def respawn(self, occupied_positions):
        """
        Respawn the food at a random position not occupied by the snake.
        
        args:
            occupied_positions: A list of tuples representing positions occupied by the snake.
        """

        pass
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
    