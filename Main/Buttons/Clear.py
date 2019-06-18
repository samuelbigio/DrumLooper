import pygame


class Clearbtn:
    def __init__(self,game):
        self.game = game

    def button(self, name, x, y, w, h, deafultColor, otherColor):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


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
                for i in range(self.game.numButtonCol):
                    for j in range(self.game.numButtonRow):
                        self.game.ToggleButton[i][j].toggleState = 0
