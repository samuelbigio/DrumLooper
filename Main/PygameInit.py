import pygame
from Buttons import toggleButton


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('belugaremix.mp3')

        self.displayW = 800
        self.displayH = 600

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
        self.numButtonCol=  4

        self.makeButtons()




    def game_loop(self):
        end = False

        while not end:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    end = True
                # print (event)

                self.gameDisplay.fill(self.lightpurple)
                self.readButtons()



    
                #TextSurf, TextRect = self.text_objects(str(event), self.largeText,self.bright_red)
                #TextRect.center = ((self.displayW / 10), (self.displayH * .9))
                #self.gameDisplay.blit(TextSurf, TextRect)



            """
            
            
                self.butt1.button("", 20, 20, 200, 200, self.red, self.bright_red)
                self.butt2.button("", 300, 300, 60, 60, self.red, self.bright_red)

                self.butt3.button("", 650, 500, 100, 20, self.red, self.bright_red)

            TextSurf2, TextRect2 = text_objects(Buttonstring, largeText, red)
            TextRect2.center = ((displayW *2 / 3), (displayH/ 2))

            gameDisplay.blit(TextSurf2, TextRect2)
            """

            pygame.display.update()
            self.clock.tick(60)

    def text_objects(self,text, font, color = (0,0,0)):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()



    def makeButtons(self):
        self.ToggleButton = [[0 for i in range(self.numButtonCol)] for j in range(self.numButtonRow)]

        for i in range(self.numButtonRow):
            for j in range(self.numButtonCol):
                ## Button Innit
                self.ToggleButton[i][j] = toggleButton(self)




    def readButtons(self):


        for i in range(self.numButtonRow):
            for j in range(self.numButtonCol):
                ## Button Innit


                self.ToggleButton[i][j].button("", int(self.displayW*.1 + i* (self.displayW/self.numButtonRow)),
                                               int(self.displayH*.1 + j*(self.displayH/self.numButtonCol)) , 20 , 20,
                                               self.red,
                                               self.bright_red)

                ## make button
