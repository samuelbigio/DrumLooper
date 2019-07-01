import pygame


class toggleBtn:

    def __init__(self, game,stayonFlag=0):
        self.game = game
        self.toggleState = 0
        self.stayonFlag = stayonFlag

    def button(self, name, x, y, w, h, deafultColor, otherColor, onStr =""):
        self.name = name

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.toggleState == 0:
            pygame.draw.rect(self.game.gameDisplay, deafultColor, (x, y, w, h))

            TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)

            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        else:
            pygame.draw.rect(self.game.gameDisplay, self.game.green, (x, y, w, h))

            TextSurf, TextRect = self.game.text_objects(onStr, self.game.largeText)

            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        if ((mouse[0] < (x + w) and mouse[0] > x) and (mouse[1] < (y + h) and mouse[1] > y)):

            if self.toggleState == 0:
                pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))

            # pygame.draw.circle(self.game.gameDisplay,otherColor,(x+ w/2,y+ h/2),10)
            if click[0] == 1:
                if self.stayonFlag ==0:
                    self.toggleState ^= 1

                if self.stayonFlag !=0:
                    if self.toggleState ==0:
                        self.toggleState=1

                # pass #is clicked
                # pygame.mixer_music.play(-1)

                # pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 10)
                # pygame.draw.rect(self.game.gameDisplay, self.game.white, (x, y, w, h))


class Grid:
    def __init__(self, game):
        self.game = game

        self.ToggleButton = [[0 for i in range(self.game.numButtonRow)] for j in range(self.game.numButtonCol)]
        for i in range(self.game.numButtonCol):
            for j in range(self.game.numButtonRow):
                ## Button Innit
                self.ToggleButton[i][j] = toggleBtn(self.game)

    def readButtons(self):

        buttonSize = 20
        xBuffer = (self.game.displayW *.8 - (
                    self.game.displayW *.8/ self.game.numButtonCol * (self.game.numButtonCol - 1))) / 2 - \
                  buttonSize / 2 + self.game.displayW * .1

        self.game.xBuffer= xBuffer

        ## takes display height including borders and subtracts that by newdisplay height divided by rows multiplied by
        # row number. divided by 2 (to center it) including button size and offsetting it by the border.
        yBuffer = (self.game.displayH * .8 - (
                    self.game.displayH * .8 / self.game.numButtonRow * (self.game.numButtonRow - 1))) \
                  / 2 - buttonSize / 2 + self.game.displayH * .1

        self.game.yBuffer = yBuffer

        for i in range(self.game.numButtonCol):
            for j in range(self.game.numButtonRow):
                ## Button Innit

                if i % 4 == 0:  # make 1st beats stand out
                    self.ToggleButton[i][j].button("", int(
                        xBuffer + i * (self.game.displayW*.8 / self.game.numButtonCol)),
                                                        int(yBuffer + j * (
                                                                self.game.displayH * 0.8 / self.game.numButtonRow)),
                                                        buttonSize, buttonSize,
                                                        self.game.red,
                                                        self.game.bright_red)

                else:
                    self.ToggleButton[i][j].button("", int(
                        xBuffer + i * (self.game.displayW *.8 / self.game.numButtonCol)),
                                                        int(yBuffer + j * (
                                                                self.game.displayH * .8 / self.game.numButtonRow)),
                                                        buttonSize,
                                                        buttonSize,
                                                        self.game.redhue,
                                                        self.game.bright_red)

