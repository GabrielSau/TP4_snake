import Entity

class MovingEntity(Entity):
    CELL_SIZE = 20
    DEFAULT_SPEED = 10
    def __init__(self):
        super().__init__()
        self._dx = self.CELL_SIZE
        self._dy = 0
        self._speed = self.DEFAULT_SPEED
        self._cell = self.CELL_SIZE

    def set_direction(self, dx: int, dy: int):
        """
        Set the direction of the entity.
        
        Args:
            dx: Change in x direction.
            dy: Change in y direction.
        """
        self._dx += dx
        self._dy += dy
        

    def set_default_speed(self, value:int):
        """
        Set the default speed of the entity.
        """
        if value > 0:
            self._speed = value

    def set_cell_size(self, value: int):
        """
        Set the cell size
        
        Args:
            value: An integer representing the cell size.
        """
        if value > 0:
            self._cell = value