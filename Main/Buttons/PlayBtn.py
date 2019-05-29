import pygame


class Play:

    def __init__(self,game):
        self.game = game
        self.toggleState=0



    def button(self,name, x, y, w, h, deafultColor, otherColor):


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()



        if self.toggleState ==0:
            #pygame.draw.rect(self.game.gameDisplay, deafultColor, (x, y, w, h))
            pygame.draw.circle(self.game.gameDisplay, deafultColor, (x + w / 2, y + h / 2),20)

            TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)

            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        else:
            #pygame.draw.rect(self.game.gameDisplay, self.game.green, (x, y, w, h))
            pygame.draw.circle(self.game.gameDisplay, self.game.green, (x + w / 2, y + h / 2), 20)
            TextSurf, TextRect = self.game.text_objects("stop", self.game.largeText)
            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        if (( mouse[0] < (x + w) and mouse[0] > x ) and ( mouse[1] < (y+h) and mouse[1] > y ) ):

            if self.toggleState ==0:
                #pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))
                pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 20)
                TextSurf, TextRect = self.game.text_objects("press me", self.game.largeText)
                TextRect.center = ((x + w / 2), (y + h / 2))

                self.game.gameDisplay.blit(TextSurf, TextRect)


            #pygame.draw.circle(self.game.gameDisplay,otherColor,(x+ w/2,y+ h/2),10)
            if click[0] == 1:



                self.toggleState ^= 1

                if self.toggleState == 1:

                    self.states = [[0 for i in range(self.game.numButtonCol)] for j in
                                                             range(self.game.numButtonRow)]



                    for i in range(len(self.game.ToggleButton)):
                        for j in range(len(self.game.ToggleButton[0])):
                            self.states[j][i] = self.game.ToggleButton[i][j].toggleState
                           #print self.game.ToggleButton[i][j]

                    print self.states



