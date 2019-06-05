import pygame
import Buttons
from Buttons.ToggleButtons import toggleBtn
from Buttons.PlayBtn import Play
from Buttons.dial import DialBtn


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()



        #pygame.mixer.music.load('belugaremix.mp3')
        #pygame.mixer.music.load('Sounds/kit1/kick.mp3')
        #pygame.mixer.music.play(-1)


        self.displayW = 800#00
        self.displayH = 600#600

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.lightpurple = (205, 205, 255)
        self.red = (180, 30, 30)
        self.green = (0,255,0)
        self.bright_red = (255, 0, 0)
        self.orange = (255,115,0)
        self.orangehue = (255, 90, 10)

        self.largeText = pygame.font.Font('freesansbold.ttf', 10)

        self.gameDisplay = pygame.display.set_mode((self.displayW, self.displayH))

        pygame.display.set_caption('Samuel Bigio - Drum Looper')

        self.clock = pygame.time.Clock()


        #todo check how many soundnames there are
        self.numButtonRow = 4
        self.numButtonCol=  16

        self.makeButtons()
        self.play = Play(self)

        dialCenter = (25,30)
        dialColors = [self.orange,self.orangehue]
        dialPL = self.getDialPL(dialCenter,20)


        self.dialUp = DialBtn(self, 1, dialPL[0], dialColors)
        self.dialDown = DialBtn(self, 0, dialPL[1], dialColors)

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
                self.readButtons()

                self.play.button("play", self.displayW/2,self.displayH/2, 20,20, self.red,self.bright_red)

                self.dialUp.getMove()
                self.dialDown.getMove()

                #todo: loop beat


            pygame.display.update()
            self.clock.tick(60)




    def text_objects(self,text, font, color = (0,0,0)):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()



    def makeButtons(self):
        self.ToggleButton = [[0 for i in range(self.numButtonRow)] for j in range(self.numButtonCol)]




        for i in range(self.numButtonCol):
            for j in range(self.numButtonRow):
                ## Button Innit
                self.ToggleButton[i][j] = toggleBtn(self)




    def readButtons(self):

        buttonSize = 20
        # grabs half the white space left and centers it
        xBuffer = (self.displayW  - (self.displayW/self.numButtonCol* (self.numButtonCol-1)))/2 - buttonSize/2
        yBuffer = (self.displayH - (self.displayH / self.numButtonRow * (self.numButtonRow - 1))) / 2 - buttonSize/2



        #yBuffer= (self.displayH - self.numButtonCol * buttonSize)/2




        for i in range(self.numButtonCol):
            for j in range(self.numButtonRow):
                ## Button Innit


                self.ToggleButton[i][j].button("", int(xBuffer + i* (self.displayW/self.numButtonCol)),
                                               int(yBuffer+   j*(self.displayH/self.numButtonRow)) , buttonSize , buttonSize,
                                               self.red,
                                               self.bright_red)

                ## make button


    def getDialPL(self,center,R):
        resUp = [(0,0),(0,0),(0,0)]
        resDown = [(0,0),(0,0),(0,0)]


        resDown[0]= (center[0] + R/2., R/4 + center[1])
        resDown[1]= (center[0] - R/2., R/4 + center[1])
        resDown[2]= (center[0],  R*5/4. + center[1])

        resUp[0] = (center[0] + R/2., center[1] - R/4)
        resUp[1] = (center[0] - R/2., center[1] - R/4 )
        resUp[2] = (center[0], center[1] - R*5./4)

        res = [resUp, resDown]
        return res



# ESTABLISH PL AS A LIST FROM THE CENTER [ [(R/2, R), (R/2, -R), (0, R/2 + R)],
#                                        [(-R/2, R), (-R/2, -R), (0, -R/2 - R)]