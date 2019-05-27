import pygame


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('belugaremix.mp3')
displayW = 800
displayH = 600

black = (0,0,0)
white = (205, 205, 255)
red = (180,30,30)
bright_red = (255,0,0)

largeText = pygame.font.Font('freesansbold.ttf',30)

gameDisplay = pygame.display.set_mode((displayW, displayH))
#gameDisplay2 = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption('Never follow their dreams')

clock = pygame.time.Clock()


def text_objects(text,font, color =black):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()






def game_loop():
    end = False

    while not end:

        for event in pygame.event.get():


            if event.type== pygame.QUIT:
                end = True
            #print (event)

            gameDisplay.fill(white)


            button("Beluga Whale dolphin",20,20,200,200,red,bright_red)
            button("", 300, 300, 60, 60, red, (100,50,255))

            TextSurf, TextRect = text_objects(str(event), largeText)
            TextRect.center = ((displayW/10),(displayH * .9))
            gameDisplay.blit(TextSurf,TextRect)



            """

            TextSurf2, TextRect2 = text_objects(Buttonstring, largeText, red)
            TextRect2.center = ((displayW *2 / 3), (displayH/ 2))
            
            gameDisplay.blit(TextSurf2, TextRect2)
            """


            pygame.display.update()
            clock.tick(60)

game_loop()
pygame.quit()
quit()



"""

Moving forward i want to create a dynamic grid for each instrument
each instrument should have a picture and then eight buttons
the grid should be dynamic with how many instruments/buttons

i want the instruments buttons to be pressable and then add bits for the state
if the bits are on i want that to play in tempo
if the bits are off nothing happens

i wantt a marker to follow the bpm (this is optional)

if i have enough time i want a drop down to pick instruments (this wont matter in hardware so it might be waste of time)



"""