import pygame
import random
from MovingEntity import MovingEntity


class Food(MovingEntity):
    def __init__(self):
        """Initialize the food objects"""
        super().__init__()
        self._x = 0
        self._y = 0

    def draw(self, screen):
        """Draw the food on the screen
        
        args:
            screen: The pygame screen surface where the food will be drawn
        """
        pygame.draw.rect(
            screen, 
            (255, 0, 0), 
            (self._x, 
             self._y, 
             self.CELL_SIZE, 
             self.CELL_SIZE
            )
        )

    def pos(self):
        """Return the current position of the food"""

        return (self._x, self._y)

    def respawn(self, occupied_positions):
        """
        Respawn the food at a random position not occupied by the snake
        
        args:
            occupied_positions: A list of tuples representing positions occupied by the snake
        """
        surface = pygame.display.get_surface()
        max_x = (surface.get_width() // MovingEntity.CELL_SIZE) -1
        max_y = (surface.get_height() // MovingEntity.CELL_SIZE) - 1

        while True:
            x = random.randint(0, max_x) * self.CELL_SIZE
            y = random.randint(0, max_y) * self.CELL_SIZE
            
            # Ensure the new position is not occupied by the snake
            if (x, y) not in occupied_positions:
                self._x = x
                self._y = y
                break

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
    