import pygame


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('belugaremix.mp3')
displayW = 800
displayH = 600

black = (0,0,0)
white = (255, 255, 255)
red = (180,30,30)
bright_red = (255,0,0)

largeText = pygame.font.Font('freesansbold.ttf',10)

gameDisplay = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption('Never follow their dreams')
clock = pygame.time.Clock()
pygame.mixer_music.play(-1)

def text_objects(text,font, color =black):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def button(name,x,y,w,h,deafultColor,otherColor):


    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(gameDisplay, deafultColor, (x,y,w,h))
    TextSurf, TextRect = text_objects(name, largeText)
    TextRect.center = ((x + w/2), (y+h/2))
    gameDisplay.blit(TextSurf, TextRect)

    if mouse[0] < (x+w) and (y+h > mouse[1]):
        pygame.draw.rect(gameDisplay, otherColor, (x, y, w, h))
        if click[0] == 1:
            #pass #is clicked
            pygame.draw.rect(gameDisplay, white, (x, y, w, h))




def game_loop():
    end = False

    while not end:

        for event in pygame.event.get():


            if event.type== pygame.QUIT:
                end = True
            #print (event)

            gameDisplay.fill(white)

            button("Start",20,20,200,200,red,bright_red)
            button("", 300, 300, 20, 20, red, bright_red)


            """
            TextSurf, TextRect = text_objects(Buttonstring, largeText)
            TextRect.center = ((displayW/3),(displayH/2))

            TextSurf2, TextRect2 = text_objects(Buttonstring, largeText, red)
            TextRect2.center = ((displayW *2 / 3), (displayH/ 2))
            gameDisplay.blit(TextSurf,TextRect)
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