import pygame
from ToggleButtons import toggleBtn

###LOAD col that has all kits that were saved

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
                                 "Load " + str(self.game.activeMeasure +1),
                                 whenClicked= self.whenClicked)


    def whenClicked(self):
        LoadNum = self.game.modifyDrumPage.loadpresets.activeToggle

        if (self.game.modifyDrumPage.loadpresets.savedkits[LoadNum].savedStatus is not None):
            newstr = []
            for i in self.game.modifyDrumPage.loadpresets.savedkits[LoadNum].savedStatus:
                newstr.append(i)
            self.game.measures.sounds[self.game.activeMeasure] = newstr
            # self.game.modifyDrumPage.loadpresets.savedkits[LoadNum].savedStatus[:] same thing but i had a bug


        self.Loadkits.toggleState = 0






