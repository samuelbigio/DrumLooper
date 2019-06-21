import pygame
from Main.DrumPage.Buttons import Play
from Main.DrumPage.Buttons import Grid
from Main.DrumPage.Buttons import DialBtn
from Main.DrumPage.Buttons.Clear import Clearbtn


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # will this work if there is no loopfile?
        playFile = 'Sounds/kit1/loop.wav'
        pygame.mixer.music.load(playFile)

        #todo: prompt size
        self.displayW = 800#00
        self.displayH = 600#600

        self.black = (0, 0, 0)
        self.blue = (50,100,220)
        self.bright_blue = (0,0,255)
        self.white = (255, 255, 255)
        self.lightpurple = (205, 205, 255)
        self.redhue = (160, 0, 10)
        self.red = (200,0,0)
        self.green = (0,255,0)
        self.bright_red = (255, 0, 0)
        self.orange = (255,115,0)
        self.orangehue = (255, 90, 10)

        self.largeText = pygame.font.Font('freesansbold.ttf', 10)

        self.gameDisplay = pygame.display.set_mode((self.displayW, self.displayH))

        pygame.display.set_caption('Samuel Bigio - DrumLooper')

        self.clock = pygame.time.Clock()

        #todo check how many soundnames there are
        self.numButtonRow = 8
        self.numButtonCol=  16

        self.grid = Grid(self)

        self.grid2 = Grid(self)


        self.play = Play(self,"play", self.displayW/2,self.displayH/2, 20,20, self.red,self.bright_red)
        self.clear = Clearbtn(self,"clear", self.displayW / 2 +50, self.displayH / 2 , 20, 20, self.blue,
                                  self.bright_blue)

        dialColors = [self.orange, self.orangehue]

        #integrate with toolbar
        self.dialCenter = (self.displayW/2,self.displayH*.1/2 )
        self.dialRadius = 20

        self.dialUp = DialBtn(self, 1, self.dialCenter,self.dialRadius, dialColors)
        self.dialDown = DialBtn(self, 0, self.dialCenter,self.dialRadius, dialColors)

        self.bpm = 95
        #'Sounds/kit1/kick.wav'

        #todo make sound and kit load auttomatically
        self.play.soundNames = ['kick','snare','hhcl','hhop','ride','shaker','rim','shaker']
        for i in range(len(self.play.soundNames)):
            self.play.soundNames[i] = 'Sounds/kit1/' +self.play.soundNames[i] + '.wav'

    def game_loop(self):
        end = False

        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                # print (event)




                self.gameDisplay.fill(self.lightpurple)
                self.grid.readButtons()

                # TOP BORDER
                pygame.draw.line(self.gameDisplay,self.black,(0,self.displayH *.1),(self.displayW,self.displayH *.1), 10)

                # BOTTOM BORDER
                pygame.draw.line(self.gameDisplay, self.black, (0, self.displayH * .9), (self.displayW, self.displayH * .9), 10)

                self.play.button()
                #todo: center
                self.clear.button()


                self.dialUp.getMove()
                self.dialDown.getMove()
                self.printBPM()

                #todo: loop beat


            pygame.display.update()
            self.clock.tick(60)




    def text_objects(self,text, font, color = (0,0,0)):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()




    def printBPM(self):
        TextSurf, TextRect = self.text_objects(str(self.bpm), self.largeText)
        TextRect.center = (self.dialCenter)
        self.gameDisplay.blit(TextSurf, TextRect)

