import pygame


class SaveKit():
    def __init__(self,game, x, y, w, h, defaultColor, otherColor):
        self.game = game
        self.toggleState = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.deafultColor = defaultColor
        self.otherColor = otherColor

    def __call__(self, *args, **kwargs):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        name = "SaveKit"
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
            TextSurf, TextRect = self.game.text_objects("press me", self.game.largeText)
            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

            if click[0] == 1:

                LoadNum = self.game.modifyDrumPage.loadpresets.activeToggle

                self.game.modifyDrumPage.loadpresets.savedkits[LoadNum].savedStatus=\
                    self.game.measures.sounds[self.game.activeMeasure][:]




