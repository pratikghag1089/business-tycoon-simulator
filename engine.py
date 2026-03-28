import pygame
import sys
from world import World
from config import FPS, GAME_DAYS_PER_SECOND

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Business Tycoon Simulator")
        self.clock = pygame.time.Clock()
        self.running = True
        self.world = World()
        self.game_time = 0.0  # in days
        
    def run(self):
        while self.running:
            delta_time = self.clock.tick(FPS) / 1000.0  # Convert to seconds
            self.handle_input()
            self.update(delta_time)
            self.render()
        
        pygame.quit()
        sys.exit()
    
    def update(self, delta_time):
        # Update world state
        self.world.update(delta_time)
        
        # Update game time (1 real second = 1 game day)
        self.game_time += delta_time * GAME_DAYS_PER_SECOND
        
        # Update window title with current day
        pygame.display.set_caption(f"Business Tycoon Simulator - Day {int(self.game_time)}")
    
    def render(self):
        # Clear screen with a neutral color
        self.screen.fill((240, 240, 240))
        
        # Placeholder: draw a simple border
        pygame.draw.rect(self.screen, (100, 100, 100), (10, 10, 780, 580), 2)
        
        # Update display
        pygame.display.flip()
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False