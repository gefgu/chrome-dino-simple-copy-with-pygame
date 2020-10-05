import sys, pygame, os
from time import sleep

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


class GameState():
    """Manages all variables of the Game"""

    def __init__(self):
        self.dino_y = 300

        # Physics for Jump
        self.jump_initial_velocity = -6
        self.jump_velocity = self.jump_initial_velocity
        self.jump_acceleration = 0.2

        self.running = True
        self.move_dino_y = 0

        self.jumping = False

        # Velocity of Game
        self.game_velocity = -7

        # Obstacle size
        self.obstacle_width = 20
        self.obstacle_height = 50
        self.obstacle_y = 325
        self.obstacle_x = 800

        # Player Object
        self.player = None
        self.obstacle = None

    def update_plus(self, name, value):
        if name in self.__dict__.keys():
            self.__dict__[name] += value

class GameEngine():
    """Controls the Game"""

class UserInterface:
    """Handles User Interface:
        - Process Inputs
        - Render The Game"""
    def __init__(self):
        self.size = (800, 450) # Width, Height
        self.background_color = (255, 255, 255)

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Dino Runner")

        self.game_state = GameState()

        # Set FPS
        self.clock = pygame.time.Clock()

    def process_input(self):
        self.move_dino_y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game_state.jumping = True

    def process_game(self):
        if self.game_state.jumping:
            self.jump()
        self.handle_obstacle()
        if self.game_state.player is not None:
            self.handle_colision()

    def jump(self):
        self.game_state.move_dino_y = self.game_state.jump_velocity
        self.game_state.jump_velocity += self.game_state.jump_acceleration
        if self.game_state.dino_y > 300:
            self.move_dino_y = 0
            self.game_state.dino_y = 300
            self.game_state.jump_velocity = self.game_state.jump_initial_velocity
            self.game_state.jumping = False

    def handle_obstacle(self):
        self.game_state.obstacle_x += self.game_state.game_velocity
        if self.game_state.obstacle_x < -20:
            self.game_state.obstacle_x = 800

    def handle_colision(self):
        if self.game_state.player.colliderect(self.game_state.obstacle):
            sleep(2)
            self.game_state = GameState()

    def update(self):
        self.game_state.update_plus("dino_y", self.move_dino_y)

    def render(self):
        self.screen.fill(self.background_color)
        # Draw Line
        pygame.draw.line(self.screen, (0, 0, 0), (0, 375), (800, 375), 4)
        self.game_state.player = pygame.draw.rect(self.screen, (0, 0, 0), (40, self.game_state.dino_y, 30, 75))
        self.game_state.obstacle = pygame.draw.rect(self.screen, (0, 0, 0), (self.game_state.obstacle_x, self.game_state.obstacle_y,
                                                    self.game_state.obstacle_width, self.game_state.obstacle_height))
        pygame.display.update()

    def run(self):
        while self.game_state.running:
            self.process_input()
            self.process_game()
            self.update()
            self.render()
            self.clock.tick(60)



user_interface = UserInterface()
user_interface.run()
pygame.quit()
