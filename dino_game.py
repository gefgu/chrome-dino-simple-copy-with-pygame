import sys, pygame, os
from time import sleep
import objects

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.font.init()

class GameState():
    """Manages all variables of the Game"""

    def __init__(self):
        # Player Object
        self.dino = objects.dino.Dino()
        self.dino.rect.y = 300
        self.dino.rect.x = 25

        # Physics for Jump
        self.jump_initial_velocity = -6
        self.jump_velocity = self.jump_initial_velocity
        self.jump_acceleration = 0.2

        # Boolean Variables
        self.running = True
        self.jumping = False

        # Velocity of Game
        self.game_velocity = -7

        # Obstacle object
        self.obstacle = objects.obstacle.Cactus()
        self.obstacle.rect.y = 300
        self.obstacle_initial_x = 800
        self.obstacle.rect.x = self.obstacle_initial_x

        # Screen Variables
        self.size = (800, 450) # Width, Height
        self.background_color = (255, 255, 255)

        # Ground
        self.ground = objects.ground.Ground()
        self.ground.rect.y = 360

        # Sprites List
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.ground)
        self.all_sprites_list.add(self.dino)
        self.all_sprites_list.add(self.obstacle)

        # Frame
        self.frame = 0

    def update_plus(self, name, value):
        if name in self.__dict__.keys():
            self.__dict__[name] += value

class GameEngine():
    """Controls the Game"""
    def __init__(self):
        self.game_state = GameState()
        self.user_interface = UserInterface(self.game_state)

        # Set FPS
        self.clock = pygame.time.Clock()

    def process_game(self):
        if self.game_state.jumping:
            self.jump()
            self.game_state.dino.jump_posture()
        else:
            # Dino Animation
            if (self.game_state.frame % 15) == 0:
                self.game_state.dino.animate()
        self.handle_obstacle()
        if self.game_state.dino is not None:
            self.handle_colision()

        # Ground
        self.game_state.ground.rect.x += self.game_state.game_velocity
        if self.game_state.ground.rect.x <= -1600:
            self.game_state.ground.rect.x = 0
            self.game_state.ground.flip_side()

        self.game_state.frame += 1

    def jump(self):
        self.move_dino_y = self.game_state.jump_velocity
        self.game_state.jump_velocity += self.game_state.jump_acceleration
        if self.game_state.dino.rect.y > 300:
            self.move_dino_y = 0
            self.game_state.dino.rect.y = 300
            self.game_state.jump_velocity = self.game_state.jump_initial_velocity
            self.game_state.jumping = False
            self.game_state.dino.animate()

    def handle_obstacle(self):
        self.game_state.obstacle.rect.x += self.game_state.game_velocity
        if self.game_state.obstacle.rect.x < -20:
            self.game_state.obstacle.rect.x = 800

    def handle_colision(self):
        if self.game_state.dino.check_colision(self.game_state.obstacle.rect):
            self.restart()

    def restart(self):
        sleep(1)
        self.game_state.__init__()

    def process_input(self):
        self.move_dino_y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game_state.jumping = True

    def update(self):
        self.game_state.dino.rect.y += self.move_dino_y

    def run(self):
        while self.game_state.running:
            self.process_input()
            self.process_game()
            self.update()
            self.user_interface.render()
            self.clock.tick(60)

class UserInterface:
    """Render The Game"""

    def __init__(self, game_state):
        self.game_state = game_state

        self.screen = pygame.display.set_mode(self.game_state.size)
        pygame.display.set_caption("Dino Runner")
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        self.screen.fill(self.game_state.background_color)

        # Draw Line
        self.game_state.all_sprites_list.update()
        self.game_state.all_sprites_list.draw(self.screen)

        score_text = self.font.render(str(int(self.game_state.frame / 4)), False, (0, 0, 0))
        self.screen.blit(score_text, (725, 15))

        pygame.display.flip()
        pygame.display.update()

if __name__ == "__main__":
    game = GameEngine()
    game.run()
    pygame.quit()
