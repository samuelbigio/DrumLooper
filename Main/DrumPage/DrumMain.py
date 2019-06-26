import pygame
import pygame

BORDER = 0
Verbose = 1

class DrumLoop():
    def __init__(self,game):
        self.game= game

    def __call__(self, *args, **kwargs):


        for i in range(self.game.numberofmeasures):
            if i == self.game.activeMeasure:
                self.game.grid[i].readButtons()

        if BORDER == 1:
            # TOP BORDER
            pygame.draw.line(self.game.gameDisplay, self.black, (0, self.displayH * .1), (self.displayW, self.displayH * .1), 10)

            # BOTTOM BORDER
            pygame.draw.line(self.game.gameDisplay, self.black, (0, self.displayH * .9), (self.displayW, self.displayH * .9), 10)

        self.game.toolbar()
        self.game.printBPM()
        self.game.string = pygame.time.get_ticks()

        if Verbose == 1:
            TextSurfDebug, TextRectDebug = self.game.text_objects(str(self.game.string), self.game.largeText)
            TextRectDebug.center = (self.game.displayW / 2, int(self.game.displayH * .9 + self.game.displayH * .05))
            self.game.gameDisplay.blit(TextSurfDebug, TextRectDebug)



def text_objects(self,text, font, color = (0,0,0)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()



