from snake import Snake
from food import Food
import pygame
import sys


class Game:
    def __init__(self, fps, width, height):
        self.width = width
        self.height = height
        self.surface = None
        self.fps_count = fps
        self.fps = pygame.time.Clock()
        self.active = True

        self.snake = Snake(self)
        self.food = Food(self)

    def run(self):
        errors = pygame.init()
        if errors[1] > 0:
            sys.exit()

        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Змейка')

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    self.snake.new_direction = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    self.snake.new_direction = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    self.snake.new_direction = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    self.snake.new_direction = "DOWN"
                elif event.key == pygame.K_RETURN and not self.active:
                    self.restart()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def render_score(self, coordinates=(40, 10)):
        score = len(self.snake.body) - 3
        self.render_text(24, f'Счет: {score}', pygame.Color('white'), coordinates)

    def render_text(self, size, text, color, coordinates):
        go_font = pygame.font.Font(None, size)
        go_surf = go_font.render(text, True, color)
        go_rect = go_surf.get_rect()
        go_rect.midtop = coordinates
        self.surface.blit(go_surf, go_rect)

    def end(self):
        self.active = False
        self.surface.fill(pygame.Color('black'))
        self.render_text(72, 'Игра окончена', pygame.Color('red'), (250, 50))
        self.render_text(32, 'Нажмите Enter, чтобы перезапустить', pygame.Color('white'), (250, 170))
        self.render_text(32, 'Нажмите Escape, чтобы выйти', pygame.Color('white'), (250, 210))
        self.render_score((250, 20))
        pygame.display.flip()

    def restart(self):
        pygame.display.flip()
        self.snake = Snake(self)
        self.food = Food(self)
        self.active = True

    def render(self):
        self.fps.tick(self.fps_count)
        if self.active:
            pygame.display.flip()
            self.surface.fill(pygame.Color(138, 43, 226))
            self.snake.change_direction()
            self.render_score()
            self.snake.render()
            self.food.render()
