import pygame
from Main.MISC.center_circles import CenterDesign
from MainMenu import MainMenu


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.synthFlag = 0
        #todo: prompt size
        self.displayW = 800#800
        self.displayH = 600#600

        self.getColors()
        self.buttonSize = 20
        self.string = "innit"
        self.FLAG=0
        self.design = CenterDesign(self)




        self.largeText = pygame.font.Font('freesansbold.ttf', 10)
        self.BiggerText = pygame.font.Font('freesansbold.ttf', 15)

        self.menuText = pygame.font.Font('freesansbold.ttf', 25)

        self.GameText = pygame.font.Font('freesansbold.ttf', 115)

        self.gameDisplay = pygame.display.set_mode((self.displayW, self.displayH))

        pygame.display.set_caption('Samuel Bigio - DrumLooper')

        self.clock = pygame.time.Clock()

        #todo check how many soundnames there are



        self.mainmenu = MainMenu(self)


    def game_loop(self):
        end = False

        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True

                self.gameDisplay.fill(self.lightpurple)

                self.mainmenu()

            pygame.display.update()
            #self.clock.tick_busy_loop()
            self.clock.tick(60)



    def text_objects(self,text, font, color = (0,0,0)):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()



    def printBPM(self):
        TextSurf, TextRect = self.text_objects(str(self.bpm), self.largeText)
        TextRect.center = (self.dialCenter)
        self.gameDisplay.blit(TextSurf, TextRect)


    def getColors(self):
        self.black = (0, 0, 0)
        self.blue = (50, 100, 220)
        self.bright_blue = (0, 0, 255)
        self.white = (255, 255, 255)
        self.lightpurple = (205, 205, 255)
        self.redhue = (160, 0, 10)
        self.red = (200, 0, 0)
        self.yellow = (247, 217, 15)
        self.bright_yellow = (255, 255, 0)
        self.bright_gray = (230, 230, 230)
        self.green = (0, 255, 0)
        self.bright_red = (255, 0, 0)
        self.orange = (255, 115, 0)
        self.orangehue = (255, 90, 10)