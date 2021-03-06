import pygame
from Buttons.PlayBtn import PlayAll
from Buttons.PlayBtn import PlayOne
from Buttons.dial import DialBtn
from Buttons.Clear import Clearbtn
from Buttons.SelectMeasure import Measures
from Buttons.CopyBtn import Copy
from Buttons.PasteBtn import Paste

class Tool():
    def __init__(self,game):
        self.game= game
        self.xBuffer = int(self.game.displayW* 2/30)
        self.yBuffer= int(self.game.displayH * .1)
        buttonsize = 20
        widthgap= int(self.game.displayW  *.05)

        self.game.play = PlayAll(game,"Play", widthgap,self.yBuffer/4 +buttonsize/4, buttonsize,buttonsize, self.game.red,
                              self.game.bright_red)


        self.game.play1 = PlayOne(game,"play", widthgap + self.xBuffer,self.yBuffer/4 +buttonsize/4, buttonsize,
                                  buttonsize, self.game.red, self.game.bright_red)

        self.game.copy = Copy(game,"Copy", widthgap + self.xBuffer *2 , self.yBuffer/4 +buttonsize/4,
                                   buttonsize, buttonsize,self.game.blue, self.game.bright_blue)

        self.game.paste = Paste(game,"Paste", widthgap + self.xBuffer *3 , self.yBuffer/4 +buttonsize/4,
                                   buttonsize, buttonsize,self.game.blue, self.game.bright_blue)

        self.game.clear = Clearbtn(game,"Clear", widthgap + self.xBuffer *4 , self.yBuffer/4 +buttonsize/4,
                                   buttonsize, buttonsize,self.game.blue, self.game.bright_blue)


        self.game.measures = Measures(self.game,self.xBuffer *5 + widthgap,self.game.displayH*.1/2,
                                      self.game.numberofmeasures)
        dialColors = [self.game.orange, self.game.orangehue]

        #integrate with toolbar

        self.game.dialCenter = (int(self.xBuffer * 5 + (self.game.numberofmeasures * (4.45) * buttonsize/2)) + widthgap,self.game.displayH*.1/2)

        self.game.dialRadius = buttonsize

        self.game.dialUp = DialBtn(game, 1, self.game.dialCenter,self.game.dialRadius, dialColors)
        self.game.dialDown = DialBtn(game, 0, self.game.dialCenter,self.game.dialRadius, dialColors)

        #'Sounds/kit1/kick.wav'



    def __call__(self, *args, **kwargs):

        self.game.play()
        self.game.play1()
        self.game.copy()
        self.game.paste()
        self.game.clear()
        self.game.measures()
        self.game.dialUp()
        self.game.dialDown()

    def getToolBarCoordinates(self):
        result = [(0,0)]
        return result