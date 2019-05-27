import pygame


class toggleButton:

    def __init__(self,game):
        self.game = game
        self.toggleState=0



    def button(self,name, x, y, w, h, deafultColor, otherColor):


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        TextSurf2, TextRect2 = self.game.text_objects(str(mouse), self.game.largeText)
        self.game.gameDisplay.blit(TextSurf2, TextRect2)
        TextRect2.center = ((self.game.displayW/ 2), (self.game.displayH / 2))
        self.game.gameDisplay.blit(TextSurf2, TextRect2)
        if self.toggleState ==0:
            pygame.draw.rect(self.game.gameDisplay, deafultColor, (x, y, w, h))

            TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)

            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        if (    ( mouse[0] < (x + w) or mouse[0] > x ) and ( mouse[1] < (y+h) or mouse[1] > y ) ):
            pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 10)
            #pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))
            # pygame.draw.circle(gameDisplay,otherColor,(x+w/2,y+h/2),10)
            if click[0] == 1  :

                self.toggleState = self.toggleState ^ 1
                # pass #is clicked
                #pygame.mixer_music.play(-1)

                #pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 10)
                #pygame.draw.rect(self.game.gameDisplay, self.game.white, (x, y, w, h))