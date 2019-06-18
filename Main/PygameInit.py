import pygame
import Buttons
from Buttons.ToggleButtons import toggleBtn
from Buttons.PlayBtn import Play
from Buttons.dial import DialBtn
from Buttons.Clear import Clearbtn


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
        self.numButtonRow = 4
        self.numButtonCol=  16

        self.makeGridButtons()


        self.play = Play(self)
        self.clear = Clearbtn(self)

        dialColors = [self.orange, self.orangehue]

        #integrate with toolbar
        self.dialCenter = (25,30)
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
                self.readButtons()

                self.play.button("play", self.displayW/2,self.displayH/2, 20,20, self.red,self.bright_red)


                #todo: center
                self.clear.button("clear", self.displayW / 2 +50, self.displayH / 2 , 20, 20, self.blue,
                                  self.bright_blue)


                self.dialUp.getMove()
                self.dialDown.getMove()
                self.printBPM()

                #todo: loop beat


            pygame.display.update()
            self.clock.tick(60)




    def text_objects(self,text, font, color = (0,0,0)):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()



    def makeGridButtons(self):
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


                if i % 4 == 0: #make 1st beats stand out
                    self.ToggleButton[i][j].button("", int(xBuffer + i* (self.displayW/self.numButtonCol)),
                                                   int(yBuffer+   j*(self.displayH/self.numButtonRow)) , buttonSize , buttonSize,
                                                   self.red,
                                                   self.bright_red)

                else:
                    self.ToggleButton[i][j].button("", int(xBuffer + i * (self.displayW / self.numButtonCol)),
                                                   int(yBuffer + j * (self.displayH / self.numButtonRow)), buttonSize,
                                                   buttonSize ,
                                                   self.redhue,
                                                   self.bright_red)

                ## make button





    def printBPM(self):
        TextSurf, TextRect = self.text_objects(str(self.bpm), self.largeText)
        TextRect.center = (self.dialCenter)
        self.gameDisplay.blit(TextSurf, TextRect)

