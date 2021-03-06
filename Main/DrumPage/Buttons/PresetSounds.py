import pygame
from ToggleButtons import toggleBtn


class PresetSound():

    def __init__(self,game):
        self.game=game

        self.ShowMoreFlag = 0

        self.length = 24 #20
        self.cols = 8  # 8
        self.rows = self.length/self.cols +1

        self.presets = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.length):

            # divides preset sound kits by 6 in n amount of rows until length (PresentCount/6 rows)
            #the rest of the states are zero
            self.presets[i/self.cols][i % self.cols] = toggleBtn(self.game,1)

            if i ==0:
                self.presets[i][i].toggleState=1







        count = self.length % self.cols
        self.presets[-1] = self.presets[-1][:count]
        self.activePreset = (0, 0)




    def __call__(self, *args, **kwargs):

        activei = self.game.modifyDrumPage.drumkits.activePreset[0] *6
        activej = self.game.modifyDrumPage.drumkits.activePreset[1]
        count =0
        buttonSize = 80
        xBuffer = ((self.game.displayW *.8 - (
                    self.game.displayW *.8/ self.game.numButtonCol * (self.game.numButtonCol - 1))) / 2 - \
                  buttonSize / 2 + self.game.displayW * .1) + self.game.displayW*.3

        ## takes display height including borders and subtracts that by newdisplay height divided by rows multiplied by
        # row number. divided by 2 (to center it) including button size and offsetting it by the border.
        yBuffer = ((self.game.displayH * .8 - (
                    self.game.displayH * .8 / self.game.numButtonRow * (self.game.numButtonRow - 1))) \
                  / 2 - buttonSize / 2 + self.game.displayH * .1) + self.game.displayH*.1

        TextSurf, TextRect = self.game.text_objects("Drumkit Sounds", self.game.BiggerText)
        if  len(self.game.drumSounds[activei+activej]) > self.cols*2.:
            TextRect.center = ((xBuffer + self.game.displayW*.1 + self.rows *self.game.displayW*1./60), (yBuffer - 10))
        elif len(self.game.drumSounds[activei+activej]) > self.cols:
            TextRect.center = ((xBuffer + self.game.displayW * .1 + buttonSize/3.), (yBuffer - 10))
        else:
            TextRect.center = ((xBuffer + self.game.displayW * .1 - buttonSize/2.), (yBuffer - 10))
        self.game.gameDisplay.blit(TextSurf, TextRect)





        self.soundNames = [0] * len(self.game.drumSounds[activei+activej])



        soundnameNum=0
        for i in range(len(self.soundNames)):
            test = self.game.drumSounds[activei+activej][i].split('/')
            test = test[2].split('.')
            if test[1] == 'wav':
                self.soundNames[soundnameNum] = test[0]
                soundnameNum +=1



        for i in range(len(self.presets)):
            for j in range(len(self.presets[i])):
                if count< soundnameNum:
                    self.presets[i][j].button(str(self.soundNames[count  ]),
                                              int(xBuffer + i * (self.game.displayW*.8/self.cols + buttonSize/4)),
                                                        int(yBuffer+j*(self.game.displayH * 0.8 / self.cols)),
                                                        buttonSize,
                                                        buttonSize/4,
                                                        self.game.white,
                                                        self.game.bright_gray,
                                                        str(self.soundNames[count % len(self.soundNames)]),
                                                        whenClicked= lambda : self.whenClicked(str(self.soundNames[count  ])))



                count +=1

                if self.presets[i][j].toggleState == 1:
                    for row in range(len(self.presets)):
                        for col in range(len(self.presets[row])):
                            if i != row or j != col:
                                self.presets[row][col].toggleState = 0

                    self.activePreset = (i,j)


    def whenClicked(self,name):
        activei = self.game.modifyDrumPage.drumkits.activePreset[0] * 6
        activej = self.game.modifyDrumPage.drumkits.activePreset[1]

        sound = self.game.drumSounds[activej + activei][0].split('/')
        sound = str(sound[0]) + '/' + str(sound[1]) + '/' + name + ".wav"

        self.game.modifyDrumPage.activeSound = sound
        self.playSOUND = pygame.mixer.Channel(0).play(pygame.mixer.Sound(sound))

        num = self.game.modifyDrumPage.soundtestToggle.activeToggle
        if num != -1:
            self.game.measures.sounds[self.game.activeMeasure][num] = sound
