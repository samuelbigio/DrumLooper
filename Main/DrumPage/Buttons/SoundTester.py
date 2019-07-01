import pygame

class SoundTest():
    def __init__(self,game):
        self.game = game

        self.game.soundButton= [0] * self.game.numButtonRow




        yBuffer = (self.game.displayH * .8 - (
                    self.game.displayH * .8 / self.game.numButtonRow * (self.game.numButtonRow - 1))) \
                  / 2 - self.game.buttonSize / 2 + self.game.displayH * .1
        for i in range(self.game.numButtonRow):
            self.game.soundButton[i] =SoundCircle(self.game,
                                                  self.game.yellow,
                                                  self.game.bright_yellow,
                                                  int(self.game.displayW*.1/2),
                                                  int(yBuffer + i * (self.game.displayH * 0.8 / self.game.numButtonRow) + 5),
                                                  10,
                                                  i,
                                                  5)


    def __call__(self, *args, **kwargs):

        for i in range(self.game.numButtonRow):
            self.game.soundButton[i]()





class SoundCircle():
    def __init__(self,game,Color,otherColor,x,y,r,num,w=0):
        self.game = game

        self.Color = Color
        self.otherColor = otherColor
        self.x=x
        self.y=y
        self.r=r
        self.w=w
        self.id=num




    def __call__(self, *args, **kwargs):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        x= self.x
        y=self.y
        w = self.w
        r=self.r
        deafultColor = self.Color
        otherColor=self.otherColor




        pygame.draw.circle(self.game.gameDisplay, deafultColor, (x + r / 2, y + r / 2), r,w)


        if ((mouse[0] < (x + r) and mouse[0] > x) and (mouse[1] < (y + r) and mouse[1] > y)):

            pygame.draw.circle(self.game.gameDisplay, otherColor, (x + r / 2, y + r / 2), r)


            if click[0] == 1:
                self.playSOUND = pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.game.soundNames[self.id]))

