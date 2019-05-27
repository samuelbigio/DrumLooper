import pygame


class Buttons:
    def button(self,name, x, y, w, h, deafultColor, otherColor):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, deafultColor, (x, y, w, h))
        TextSurf, TextRect = text_objects(name, largeText)
        TextRect.center = ((x + w / 2), (y + h / 2))
        gameDisplay.blit(TextSurf, TextRect)

        if mouse[0] < (x + w) and (y + h > mouse[1]):
            pygame.draw.rect(gameDisplay, otherColor, (x, y, w, h))
            # pygame.draw.circle(gameDisplay,otherColor,(x+w/2,y+h/2),10)
            if click[0] == 1:
                # pass #is clicked
                pygame.mixer_music.play(-1)
                pygame.draw.rect(gameDisplay, white, (x, y, w, h))