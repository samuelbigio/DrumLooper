import pygame
from ToggleButtons import toggleBtn

class Measures():
    def __init__(self,game,x,y, num = 4):
        self.game = game
        self.numberofmeasures = num
        self.x = x
        self.y = y
        self.measure = [0] * self.game.numberofmeasures
        self.measureStates = [0] * self.game.numberofmeasures
        for i in range(self.numberofmeasures):
            self.measure[i] = toggleBtn(self.game,1)
            self.measureStates[i] = toggleBtn(self.game)
        self.measure[0].toggleState= self.game.activeMeasure


    def __call__(self, *args, **kwargs):



        for i in range(self.numberofmeasures):
            self.measure[i].button(str(i+1),
                                    self.x + i * self.game.buttonSize*2,
                                    self.y - self.game.buttonSize,
                                    self.game.buttonSize*2,
                                    (self.game.buttonSize*2),
                                    self.game.white,
                                    self.game.bright_gray

                                    , str(i +1))

            self.measureStates[i].button("",
                                         self.x + i * self.game.buttonSize*2  + self.game.buttonSize *19/20,
                                         self.y +self.game.buttonSize + self.game.buttonSize/4,
                                         self.game.buttonSize/3,
                                         self.game.buttonSize/3,
                                         self.game.white,
                                         self.game.orangehue)


            if self.measure[i].toggleState==1:
                for j in range(self.numberofmeasures):
                    if j != i:
                        self.measure[j].toggleState = 0

                self.game.activeMeasure= i












        #find which measure and clear all other measures

        ##make a button above is able to be clicked for loops.



