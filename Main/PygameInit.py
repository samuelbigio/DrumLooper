import pygame
from Buttons import  Btn


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('belugaremix.mp3')

        self.displayW = 800
        self.displayH = 600

        self.black = (0, 0, 0)
        self.white = (205, 205, 255)
        self.red = (180, 30, 30)
        self.bright_red = (255, 0, 0)

        self.largeText = pygame.font.Font('freesansbold.ttf', 30)

        self.gameDisplay = pygame.display.set_mode((self.displayW, self.displayH))

        pygame.display.set_caption('Never follow their dreams')

        self.clock = pygame.time.Clock()

        self.butt = Btn(self)






    def game_loop(self):
        end = False

        while not end:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    end = True
                # print (event)

                self.gameDisplay.fill(self.white)

                self.butt.button("Beluga Whale dolphin", 20, 20, 200, 200, self.red, self.bright_red)
                self.butt.button("", 300, 300, 60, 60, self.red, (100, 50, 255))
    
                TextSurf, TextRect = self.text_objects(str(event), self.largeText,self.bright_red)
                TextRect.center = ((self.displayW / 10), (self.displayH * .9))
                self.gameDisplay.blit(TextSurf, TextRect)



            """

            TextSurf2, TextRect2 = text_objects(Buttonstring, largeText, red)
            TextRect2.center = ((displayW *2 / 3), (displayH/ 2))

            gameDisplay.blit(TextSurf2, TextRect2)
            """

            pygame.display.update()
            self.clock.tick(60)

    def text_objects(self,text, font, color = (0,0,0)):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()



