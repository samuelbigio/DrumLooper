import pygame
from ToggleButtons import toggleBtn


class PresetKit():
    def __init__(self,game):
        self.game=game

        self.ShowMoreFlag = 0

        self.length = len(self.game.drumSounds)
        if self.length > 18:
            self.ShowMoreFlag=1
            self.length = 18
        self.cols = 6
        self.rows = self.length/self.cols + 1

        self.presets = [[0 for i in range(self.cols)]  for j in range(self.rows)]

        for i in range(self.length):

            # divides preset sound kits by 6 in n amount of rows until length (PresentCount/6 rows)
            #the rest of the states are zero
            self.presets[i/self.cols][i % self.cols] = toggleBtn(self.game,1)


            if i ==0:
                self.presets[i][i].toggleState=1



        count = self.length % self.cols
        self.presets[-1] = self.presets[-1][:count]


        self.soundKits = [0] * len(self.game.drumSounds)

        for i in range(len(self.soundKits)):
            test = self.game.drumSounds[i][0].split('/')
            self.soundKits[i] = test[1]
            self.activePreset = (0, 0)








    def __call__(self, *args, **kwargs):

        count =0

        buttonSize = 60
        xBuffer = (self.game.displayW *.8 - (
                    self.game.displayW *.8/ self.game.numButtonCol * (self.game.numButtonCol - 1))) / 2 - \
                  buttonSize / 2 + self.game.displayW * .1

        ## takes display height including borders and subtracts that by newdisplay height divided by rows multiplied by
        # row number. divided by 2 (to center it) including button size and offsetting it by the border.
        yBuffer = (self.game.displayH * .8 - (
                    self.game.displayH * .8 / self.game.numButtonRow * (self.game.numButtonRow - 1))) \
                  / 2 - buttonSize / 2 + self.game.displayH * .1


        TextSurf, TextRect = self.game.text_objects("Drumkits", self.game.BiggerText)

        if len(self.presets)<2:
            TextRect.center = (int(xBuffer + self.game.displayW*.1 - buttonSize/3 ), (yBuffer - 10))
        else:
            TextRect.center = ((xBuffer + self.game.displayW * .1+ buttonSize/3), (yBuffer - 10))
        self.game.gameDisplay.blit(TextSurf, TextRect)


        for i in range(len(self.presets)):
            for j in range(len(self.presets[i])):

                if  len(self.presets)>2:
                    self.presets[i][j].button(str(self.soundKits[count % len(self.soundKits)]),
                                              int(xBuffer + i * (self.game.displayW*.8 / self.rows/2)),
                                                        int(yBuffer+j*(self.game.displayH * 0.8 / self.cols)),
                                                        buttonSize,
                                                        buttonSize/2,
                                                        self.game.white,
                                                        self.game.bright_gray,
                                                        str(self.soundKits[count % len(self.soundKits)]))
                else:
                    self.presets[i][j].button(str(self.soundKits[count % len(self.soundKits)]),
                                              int(xBuffer + i * (self.game.displayW * .8 / self.rows / 3)),
                                              int(yBuffer + j * (self.game.displayH * 0.8 / self.cols)),
                                              buttonSize,
                                              buttonSize / 2,
                                              self.game.white,
                                              self.game.bright_gray,
                                              str(self.soundKits[count % len(self.soundKits)]))




                count +=1

                if self.presets[i][j].toggleState == 1:
                    for row in range(len(self.presets)):
                        for col in range(len(self.presets[row])):
                            if i != row or j != col:
                                self.presets[row][col].toggleState = 0

                    self.activePreset = (i,j)

