import pygame


class Paste:
    def __init__(self, game, name, x, y, w, h, deafultColor, otherColor):
        self.game = game
        self.toggleState = 0
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.deafultColor = deafultColor
        self.otherColor = otherColor



    def __call__(self, *args, **kwargs):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        name = self.name
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        deafultColor = self.deafultColor
        otherColor = self.otherColor

        pygame.draw.circle(self.game.gameDisplay, deafultColor, (x + w / 2, y + h / 2), 20)

        TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)

        TextRect.center = ((x + w / 2), (y + h / 2))

        self.game.gameDisplay.blit(TextSurf, TextRect)

        self.game.gameDisplay.blit(TextSurf, TextRect)

        if ((mouse[0] < (x + w) and mouse[0] > x) and (mouse[1] < (y + h) and mouse[1] > y)):

            pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 20)
            TextSurf, TextRect = self.game.text_objects("", self.game.largeText)
            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

            if click[0] == 1:
                for i in range(self.game.numButtonCol):
                    for j in range(self.game.numButtonRow):
                        ## finds the measure that is on screen and clears that current grid.
                        # takes the array of grids in game class and indexes the active measure then sets all toggle
                        # states to zero.
                        self.game.grid[self.game.activeMeasure].ToggleButton[i][j].toggleState = \
                            self.game.toggleCopy[i][j]



