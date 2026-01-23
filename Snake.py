from MovingEntity import MovingEntity
import pygame

class Snake(MovingEntity):
    def __init__ (self, x, y):
        """Initialize the snake object"""
        super().__init__()
        self._body = [(x, y)]
        self._grow_pending = 0
        self.game_over = False

    def update(self, game):
        """
        Update the snake's position and check for collisions
        
        Args: 
            self: The snake instance
            game: The game instance containing game state
        
        return: The new head position of the snake
        """
        if self.game_over:
            return
        
        head_x, head_y = self._body[0]

        new_head = (head_x + self._dx, head_y + self._dy)

        # Check for self-collision
        if new_head in self._body:
            self.game_over = True
            return

        # Check for wall collision
        if (new_head[0] < 0 or new_head[0] >= game.WIDTH or
            new_head[1] < 0 or new_head[1] >= game.HEIGHT):
            self.game_over = True
            return
        
        # Move the snake
        self._body.insert(0, new_head)

        if self._grow_pending > 0:
            self._grow_pending -= 1
        else:
            self._body.pop()
        
        return new_head
            
    def draw(self, screen):
        """
        Draw the snake on the screen
        """
        for segment in self._body:
            pygame.draw.rect(
                screen, 
                (0, 255, 0), 
                (segment[0], 
                 segment[1], 
                 self.CELL_SIZE, 
                 self.CELL_SIZE
                )
            )
    
    def grow(self, n: int = 1):
        """
        Grow the snake by one segment
        """
        self._grow_pending += n
