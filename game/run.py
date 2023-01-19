from game import Game

width = 500
height = 500
fps = 8

game = Game(fps, width, height)
game.run()

while True:
    game.event_loop()
    game.render()
