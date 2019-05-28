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

        self.numButtonRow = 40
        self.numButtonCol=  30

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


                self.ToggleButton[i][j].button("", int( i* (self.displayW/self.numButtonRow)),
                                               int( j*(self.displayH/self.numButtonCol)) , 20 , 20,
                                               self.red,
                                               self.bright_red)

                ## make button
