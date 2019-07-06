import pygame



class LoadSavedKit():
    def __init__(self, game):
        self.game = game




        self.Loadkits = toggleBtn(self.game)


        self.activeToggle = 0

    def __call__(self, *args, **kwargs):

        count = 0

        buttonSize = 60
        xBuffer = (self.game.displayW * .8 - (
                self.game.displayW * .8 / self.game.numButtonCol * (self.game.numButtonCol - 1))) / 2 - \
                  buttonSize / 2 + self.game.displayW * .1

        ## takes display height including borders and subtracts that by newdisplay height divided by rows multiplied by
        # row number. divided by 2 (to center it) including button size and offsetting it by the border.
        yBuffer = (self.game.displayH * .8 - (
                self.game.displayH * .8 / self.game.numButtonRow * (self.game.numButtonRow - 1))) \
                  / 2 - buttonSize / 2 + self.game.displayH * .1

        TextSurf, TextRect = self.game.text_objects("Saved Kits", self.game.BiggerText)

        TextRect.center = (int(xBuffer + self.game.displayW * .85 - buttonSize / 5.), (yBuffer - 10))

        self.game.gameDisplay.blit(TextSurf, TextRect)

        savedkitLength= len(self.game.modifyDrumPage.loadpresets.savedkits) - 2
        LoadNum = self.game.modifyDrumPage.loadpresets.activeToggle

        if (self.game.modifyDrumPage.loadpresets.savedkits[LoadNum].savedStatus is not None):
            self.Loadkits.button("Load Preset Kit " +  str(LoadNum + 1) +  " to " + str(self.game.activeMeasure +1) ,
                                 int(xBuffer + (self.game.displayW * .75)),
                                 int(yBuffer  +savedkitLength  * (self.game.displayH * 0.8 / savedkitLength)),
                                 int(buttonSize + buttonSize),
                                 buttonSize/3,
                                 self.game.lightpurple,
                                 self.game.yellow,
                                 "Load " + str(self.game.activeMeasure +1))






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

                LoadNum = self.game.modifyDrumPage.loadpresets.activeToggle

                if (self.game.modifyDrumPage.loadpresets.savedkits[LoadNum].savedStatus is not None):
                    self.game.measures.sounds[self.game.activeMeasure] = \
                        self.game.modifyDrumPage.loadpresets.savedkits[LoadNum].savedStatus


                self.toggleState=0

                # pass #is clicked
                # pygame.mixer_music.play(-1)

                # pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 10)
                # pygame.draw.rect(self.game.gameDisplay, self.game.white, (x, y, w, h))
