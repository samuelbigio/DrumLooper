import pygame
import Buttons
from Buttons.ToggleButtons import toggleBtn
from Buttons.PlayBtn import Play
import sys





class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()



        #pygame.mixer.music.load('belugaremix.mp3')
        pygame.mixer.music.load('Sounds/kit1/FLS_Kick 01.wav')
        pygame.mixer.music.play(-1)

        self.displayW = 800#00
        self.displayH = 600#600

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.lightpurple = (205, 205, 255)
        self.red = (180, 30, 30)
        self.green = (0,255,0)
        self.bright_red = (255, 0, 0)

        self.largeText = pygame.font.Font('freesansbold.ttf', 10)

        self.gameDisplay = pygame.display.set_mode((self.displayW, self.displayH))

        pygame.display.set_caption('Never follow their dreams')

        self.clock = pygame.time.Clock()

        self.numButtonRow = 4
        self.numButtonCol=  8

        self.makeButtons()
        self.play = Play(self)




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
