import pygame


class DrumLoopButton():
    def __init__(self,game,deafultColor, otherColor):
        self.game = game
        x = int(self.game.displayW*.9) -60
        y = int(self.game.displayH* 19/20)
        w = x
        h = int(self.game.displayH*.1/2)

        self.game = game
        self.toggleState = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.deafultColor = deafultColor
        self.otherColor = otherColor


    def __call__(self, *args, **kwargs):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        deafultColor = self.deafultColor
        otherColor = self.otherColor
        onStr = "Menu"

        name = "Drum Loop"
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()



        if self.toggleState == 0:
            pygame.draw.rect(self.game.gameDisplay, deafultColor, (x, y, w, h))
            TextSurf, TextRect = self.game.text_objects(name, self.game.BiggerText)

            TextRect.center = ( int(self.game.displayW - 70), int((y + self.game.displayH*.025)))

            self.game.gameDisplay.blit(TextSurf, TextRect)


        else:
            pygame.draw.rect(self.game.gameDisplay, self.game.white, (x, y, w, h))

            TextSurf, TextRect = self.game.text_objects(onStr, self.game.BiggerText)

            TextRect.center = ( int(self.game.displayW - 70), int((y + self.game.displayH*.025)))
            self.game.gameDisplay.blit(TextSurf, TextRect)



        if ((mouse[0] < (x + w) and mouse[0] > x) and (mouse[1] < (y + h) and mouse[1] > y)):

            if self.toggleState == 0:
                pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))
                TextSurf, TextRect = self.game.text_objects(name, self.game.BiggerText)

                TextRect.center = (int(self.game.displayW - 70), int((y + self.game.displayH*.025)))

                self.game.gameDisplay.blit(TextSurf, TextRect)

            if click[0] == 1:
                self.game.moddrumFlag=0
                self.game.drumloopFlag=1

