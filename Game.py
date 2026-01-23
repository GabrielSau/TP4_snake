import pygame
from Snake import Snake
from Food import Food

class Game:
    WIDTH = 600
    HEIGHT = 400
    BG_COLOR = (0, 0, 0)
    FRAME_RATE = 10

    def __init__(self):
        """Initialize the game"""
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game")

        # Set up the clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        # Set up font for displaying score
        self.font = pygame.font.SysFont(None, 36)
        self.score = 0
        self.game_over = False
        self.pause = False

        # Initialize game entities
        self.snake = Snake(self.WIDTH // 2, self.HEIGHT // 2)
        self.food = Food()
        self.food.respawn(self.snake._body)

        self.entities = [self.food, self.snake]

    def handle_events(self):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP and self.snake._dy != self.snake.CELL_SIZE and not self.pause:
                    self.snake.set_direction(0, -self.snake.CELL_SIZE)
                elif event.key == pygame.K_DOWN and self.snake._dy != -self.snake.CELL_SIZE and not self.pause:
                    self.snake.set_direction(0, self.snake.CELL_SIZE)
                elif event.key == pygame.K_LEFT and self.snake._dx != self.snake.CELL_SIZE and not self.pause:
                    self.snake.set_direction(-self.snake.CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and self.snake._dx != -self.snake.CELL_SIZE and not self.pause:
                    self.snake.set_direction(self.snake.CELL_SIZE, 0)

                elif event.key == pygame.K_r and self.game_over:
                    self.__init__()
                    self.run()
                
                elif event.key == pygame.K_p and not self.game_over:
                    self.pause = not getattr(self, 'pause', False)                
            
        return True
    
    def update(self):
        """Update the game state"""
        if self.game_over:
            return

        new_head = self.snake.update(self)

        # Check for food collision
        if new_head == self.food.pos():
            self.snake.grow()
            self.score += 1
            self.food.respawn(self.snake._body)

        if self.snake.game_over:
            self.game_over = True
    
    def draw(self):
        """Draw all game entities and UI elements"""
        self.screen.fill(self.BG_COLOR)

        for entity in self.entities:
            entity.draw(self.screen)

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to Restart", True, (255, 0, 0))
            rect = game_over_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
            self.screen.blit(game_over_text, rect)

        if self.pause:
            pause_text = self.font.render("Paused", True, (255, 255, 0))
            rect = pause_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
            self.screen.blit(pause_text, rect)

        pygame.display.flip()

    def run(self):
        """Run the main game loop"""
        running = True
        while running:
            self.clock.tick(self.FRAME_RATE)  # Control the frame rate
            running = self.handle_events()
            if not self.pause:
                self.update()
            self.draw()
                

        pygame.quit()
