import pygame
from ToggleButtons import toggleBtn


class LoadPreset():
    def __init__(self,game):
        self.game=game

        self.ShowMoreFlag = 0

        self.length = 8
        if self.length > 8:
            self.ShowMoreFlag=1
            self.length = 8


        
        self.savedkits = [0] * self.length

        stock = ['kick', 'snare', 'hhcl', 'hhop', 'ride', 'crash', 'rim', 'shaker']
        for j in range(self.game.numButtonRow):
            stock[j] = 'Sounds/stock/'+ stock[j] +'.wav'

        for i in range(self.length):

            # divides preset sound kits by 6 in n amount of rows until length (PresentCount/6 rows)
            #the rest of the states are zero
            self.savedkits[i] = toggleBtn(self.game,1)

            self.savedkits[i].savedStatus = None

            if i == 0 or i == self.length-1:
                self.savedkits[i].savedStatus=stock

                self.savedkits[i].name="stock"

        self.savedkits[0].toggleState = 1

        self.activeToggle = 0









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


        TextSurf, TextRect = self.game.text_objects("Saved Kits", self.game.BiggerText)



        TextRect.center = (int(xBuffer + self.game.displayW*.85 - buttonSize/5.  ), (yBuffer - 10))

        self.game.gameDisplay.blit(TextSurf, TextRect)

        for i in range(len(self.savedkits)):


            if (self.savedkits[i].savedStatus is None):
                self.savedkits[i].button("",
                                          int(xBuffer + (self.game.displayW * .8)),
                                          int(yBuffer*1.2 + i * (self.game.displayH * 0.8/len(self.savedkits))),
                                          buttonSize,
                                          buttonSize / 3,
                                          self.game.white,
                                          self.game.bright_gray,
                                         "Blank")

            else:

                if self.savedkits[i].name == "stock":
                    kitName = "stock"
                else:
                    kitName ="Kit " + str(i+1)

                self.savedkits[i].button(kitName,
                                          int(xBuffer + (self.game.displayW * .8)),
                                          int(yBuffer*1.2 + i * (self.game.displayH * 0.8/len(self.savedkits))),
                                          buttonSize,
                                          buttonSize / 3,
                                          self.game.white,
                                          self.game.bright_gray,
                                         kitName)




            if self.savedkits[i].toggleState == 1:


                for j in range(len(self.savedkits)):
                    if j != i:
                        self.savedkits[j].toggleState = 0
                        self.activeToggle = i



