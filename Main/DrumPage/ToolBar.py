import pygame
from Buttons.PlayBtn import Play
from Buttons.dial import DialBtn
from Buttons.Clear import Clearbtn

class Tool():
    def __init__(self,game):
        self.game= game
        self.xBuffer = int(self.game.displayW*.05)
        self.yBuffer= int(self.game.displayH * .1)
        self.game.play = Play(game,"play", 10,int(self.yBuffer/4), 20,20, self.game.red,self.game.bright_red)
        self.game.clear = Clearbtn(game,"clear", 10 + self.xBuffer, int(self.yBuffer/4), 20, 20, self.game.blue,
                                  self.game.bright_blue)

        dialColors = [self.game.orange, self.game.orangehue]

        #integrate with toolbar
        self.game.dialCenter = ((self.xBuffer *2 + 10),self.game.displayH*.1/2 )
        self.game.dialRadius = 20

        self.game.dialUp = DialBtn(game, 1, self.game.dialCenter,self.game.dialRadius, dialColors)
        self.game.dialDown = DialBtn(game, 0, self.game.dialCenter,self.game.dialRadius, dialColors)

        #'Sounds/kit1/kick.wav'

        #todo make sound and kit load auttomatically
        self.game.play.soundNames = ['kick','snare','hhcl','hhop','ride','shaker','rim','shaker']
        for i in range(len(self.game.play.soundNames)):
            self.game.play.soundNames[i] = 'Sounds/kit1/' +self.game.play.soundNames[i] + '.wav'

    def __call__(self, *args, **kwargs):
        self.game.play.button()
        self.game.clear.button()
        self.game.dialUp.getMove()
        self.game.dialDown.getMove()

    def getToolBarCoordinates(self):
        result = [(0,0)]
        return result