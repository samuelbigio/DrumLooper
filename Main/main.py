import pygame


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('belugaremix.mp3')
displayW = 800
displayH = 600

black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)

largeText = pygame.font.Font('freesansbold.ttf',10)

gameDisplay = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption('Never follow their dreams')
clock = pygame.time.Clock()
pygame.mixer_music.play(-1)

def text_objects(text,font, color =black):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def game_loop():
    end = False

    while not end:

        for event in pygame.event.get():
            Buttonstring = str(event)

            if event.type== pygame.QUIT:
                end = True
            print (event)

            gameDisplay.fill(white)

            TextSurf, TextRect = text_objects(Buttonstring, largeText)
            TextRect.center = ((displayW/3),(displayH/2))

            TextSurf2, TextRect2 = text_objects(Buttonstring, largeText, red)
            TextRect2.center = ((displayW *2 / 3), (displayH/ 2))
            gameDisplay.blit(TextSurf,TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)



            pygame.display.update()
            clock.tick(60)

game_loop()
pygame.quit()
quit()