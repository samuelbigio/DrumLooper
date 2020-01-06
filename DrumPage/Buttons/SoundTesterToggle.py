import pygame
from ToggleButtons import toggleBtn


class SoundTestToggle():
    def __init__(self, game):
        self.game = game

        self.btnStates = [0] * self.game.numButtonRow

        for i in range(len(self.btnStates)):
            self.btnStates[i] = toggleBtn(self.game)

        self.activeToggle = -1




    def __call__(self, *args, **kwargs):
        yBuffer = (self.game.displayH * .8 - (
                self.game.displayH * .8 / self.game.numButtonRow * (self.game.numButtonRow - 1))) \
                  / 2 - self.game.buttonSize / 2 + self.game.displayH * .1


        for i in range(self.game.numButtonRow):
            self.btnStates[i].button("load",
                                     int(self.game.displayW * .0125 ),
                                     int(yBuffer + i * (self.game.displayH * 0.8 / self.game.numButtonRow) + self.game.buttonSize/4),
                                     self.game.buttonSize,
                                     self.game.buttonSize/3 * 2 ,
                                     self.game.lightpurple,
                                     self.game.orangehue)

            if self.btnStates[i].toggleState==1:
                for j in range(self.game.numButtonRow):
                    if j != i:
                        self.btnStates[j].toggleState = 0
                        self.activeToggle = i
                    if j == i:
                        #self.btnStates[i].toggleState = 0
                        #self.game.modifyDrumPage.soundtestToggle.activeToggle = -1
                        sound = self.game.modifyDrumPage.activeSound
                        self.game.measures.sounds[self.game.activeMeasure][i] = sound
                        self.activeToggle = -1
                        self.btnStates[i].toggleState = 0



        sumBtn = 0
        for j in range (self.game.numButtonRow):
            sumBtn += self.btnStates[j].toggleState

        if sumBtn == 0:
            self.activeToggle= -1







