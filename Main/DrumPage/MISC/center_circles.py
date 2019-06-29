import pygame

class CenterDesign():
    def __init__(self,game):
        self.game=game


    def __call__(self, *args, **kwargs):

        ###make these turn colors and turn into squares and different shapes to music later


        pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 10, 1)

        pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 20, 2)

        pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 40, 4)

        pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 60, 6)

        pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 80, 8)
