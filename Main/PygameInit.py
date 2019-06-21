import pygame
from Main.DrumPage.Buttons.ToggleButtons import Grid
from Main.DrumPage.ToolBar import Tool


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

        self.toolbar = Tool(self)

        self.bpm = 95


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

                self.toolbar()
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

