from settings import *


class Game:
    def __init__(self):
        # Setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Operation Depths')
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # Delta Time
            delta_time = self.clock.tick() / 1000

            # Game Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Draw
            self.display_surface.fill('black')

        pygame.quit()
