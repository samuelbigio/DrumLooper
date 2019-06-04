import pygame



# ESTABLISH PL AS A LIST FROM THE CENTER [ [(R/2, R), (R/2, -R), (0, R/2 + R)],
#                                        [(-R/2, R), (-R/2, -R), (0, -R/2 - R)]

# if bpm is toggled on check if up and then self.game.BPM +=1 or -=1


# create a display for bpm

class DialBtn:
    def __init__(self,game,up, PL, colors):
        self.game = game
        self.up = up
        self.colors = colors
        self.pointlist=PL



    def getMove(self):
        deafultColor =  self.colors[0]
        otherColor = self.colors[1]

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.toggleState ==0:

            if self.up:  # going up
                pygame.draw.polygon(self.game.gameDisplay, deafultColor, self.pl[0])
            else:   # going down
                pygame.draw.polygon(self.game.gameDisplay, deafultColor, self.pl[1])

            """
            #IF go up/If go down
            TextSurf, TextRect = self.game.text_objects("", self.game.largeText)

            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)
            """

        else:
            #pygame.draw.rect(self.game.gameDisplay, self.game.green, (x, y, w, h))


            pygame.draw.polygon(self.game.gameDisplay, deafultColor, self.pl[0])


        if (( mouse[0] < (x + w) and mouse[0] > x ) and ( mouse[1] < (y+h) and mouse[1] > y ) ):

            if self.toggleState ==0:
                #pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))
                pygame.draw.polygon(self.game.gameDisplay, deafultColor, self.pl[0])


            if click[0] == 1:

                self.toggleState ^= 1



