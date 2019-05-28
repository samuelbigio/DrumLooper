import pygame


class toggleButton:

    def __init__(self,game):
        self.game = game
        self.toggleState=0



    def button(self,name, x, y, w, h, deafultColor, otherColor):


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()



        if self.toggleState ==0:
            pygame.draw.rect(self.game.gameDisplay, deafultColor, (x, y, w, h))

            TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)

            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        else:
            pygame.draw.rect(self.game.gameDisplay, self.game.green, (x, y, w, h))


        if (( mouse[0] < (x + w) and mouse[0] > x ) and ( mouse[1] < (y+h) and mouse[1] > y ) ):

            if self.toggleState ==0:
                pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))


            #pygame.draw.circle(self.game.gameDisplay,otherColor,(x+ w/2,y+ h/2),10)
            if click[0] == 1:

                self.toggleState ^= 1


                # pass #is clicked
                #pygame.mixer_music.play(-1)

                #pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 10)
                #pygame.draw.rect(self.game.gameDisplay, self.game.white, (x, y, w, h))