from random import randrange
import pygame


class Food():
    def __init__(self, game):
        self.game = game
        self.coordinates = []
        self.generate_food(4)

    def generate_food(self, foods_count):
        not_spawned_in_snake = lambda x, y: (x, y) not in self.game.snake.body
        not_spawned_in_food = lambda x, y: (x, y) not in self.coordinates

        for _ in range(foods_count):
            while True:
                x = randrange(1, self.game.width / 10) * 10
                y = randrange(1, self.game.height / 10) * 10
                if not_spawned_in_snake(x, y) and not_spawned_in_food(x, y):
                    self.coordinates.append((x, y))
                    break

    def eat(self, coordinates):
        self.coordinates.remove(coordinates)
        self.generate_food(1)

    def render(self):
        for pos in self.coordinates:
            pygame.draw.rect(self.game.surface, pygame.Color('red'),
                             pygame.Rect(pos[0], pos[1], 10, 10))
