import pygame


class Btn:

    def __init__(self,game):
        self.game = game



    def button(self,name, x, y, w, h, deafultColor, otherColor):


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(self.game.gameDisplay, deafultColor, (x, y, w, h))
        TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)
        TextRect.center = ((x + w / 2), (y + h / 2))
        self.game.gameDisplay.blit(TextSurf, TextRect)

        if mouse[0] < (x + w) and (y + h > mouse[1]):
            pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))
            # pygame.draw.circle(gameDisplay,otherColor,(x+w/2,y+h/2),10)
            if click[0] == 1:
                # pass #is clicked
                pygame.mixer_music.play(-1)
                pygame.draw.rect(self.game.gameDisplay, self.game.white, (x, y, w, h))