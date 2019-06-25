import pygame
from Buttons.PlayBtn import PlayAll
from Buttons.PlayBtn import PlayOne
from Buttons.dial import DialBtn
from Buttons.Clear import Clearbtn
from Buttons.SelectMeasure import  Measures

class Tool():
    def __init__(self,game):
        self.game= game
        self.xBuffer = int(self.game.displayW* 2/30)
        self.yBuffer= int(self.game.displayH * .1)
        buttonsize = 20
        widthgap= int(self.game.displayW * .05)

        self.game.play = PlayAll(game,"play", widthgap,self.yBuffer/4 +buttonsize/4, buttonsize,buttonsize, self.game.red,
                              self.game.bright_red)


        self.game.play1 = PlayOne(game,"play", widthgap + self.xBuffer,self.yBuffer/4 +buttonsize/4, buttonsize,
                                  buttonsize, self.game.red, self.game.bright_red)

        self.game.clear = Clearbtn(game,"clear", widthgap + self.xBuffer *2 , self.yBuffer/4 +buttonsize/4,
                                   buttonsize, buttonsize,self.game.blue, self.game.bright_blue)

        self.game.measures = Measures(self.game,self.xBuffer *3 + widthgap,self.game.displayH*.1/2,
                                      self.game.numberofmeasures)
        dialColors = [self.game.orange, self.game.orangehue]

        #integrate with toolbar

        self.game.dialCenter = (int(self.xBuffer * 3 + (self.game.numberofmeasures * (4.45) * buttonsize/2)) + widthgap,self.game.displayH*.1/2)

        self.game.dialRadius = buttonsize

        self.game.dialUp = DialBtn(game, 1, self.game.dialCenter,self.game.dialRadius, dialColors)
        self.game.dialDown = DialBtn(game, 0, self.game.dialCenter,self.game.dialRadius, dialColors)

        #'Sounds/kit1/kick.wav'

        #todo make sound and kit load auttomatically
        self.game.soundNames = ['kick','snare','hhcl','hhop','ride','shaker','rim','shaker']
        for i in range(len(self.game.soundNames)):
            self.game.soundNames[i] = 'Sounds/kit1/' +self.game.soundNames[i] + '.wav'

    def __call__(self, *args, **kwargs):

        self.game.play.button()
        self.game.play1.button()
        self.game.clear.button()
        self.game.measures()
        self.game.dialUp.getMove()
        self.game.dialDown.getMove()

    def getToolBarCoordinates(self):
        result = [(0,0)]
        return result