from DrumPage.Buttons import toggleBtn
import pygame

#self.game.mainmenu.synthMain.
class DisplayOctaves():
    def __init__(self,game):
        self.game = game
        octavenum = 9
        self.octavebutton = [0] * octavenum
        for i in range(octavenum):
            self.octavebutton[i] = toggleBtn(self.game,1)

        self.octavebutton[4].toggleState=1

        self.activeOctave = 4


    def __call__(self, *args, **kwargs):

        TextSurf, TextRect = self.game.text_objects("Octaves", self.game.BiggerText)

        TextRect.center = ( ((self.game.displayW * .01 + 9*self.game.buttonSize) / 2),
                             self.game.displayH * .75 - self.game.buttonSize/2.)

        self.game.gameDisplay.blit(TextSurf, TextRect)

        for i in range(len(self.octavebutton)):
            self.octavebutton[i].button(str(i),
            self.game.displayW * .01 + i*self.game.buttonSize,
            self.game.displayH * .75,
            self.game.buttonSize,
            self.game.buttonSize,
            self.game.white,
            self.game.bright_gray,
            onStr =str(i),
            whenClicked = (lambda: self.octaveClicked(i)))


        self.keysSet()



    def octaveClicked(self,num):
        for i in range(len(self.octavebutton)):
            if i !=num:
                self.octavebutton[i].toggleState = 0

        self.activeOctave = num


    def keysSet(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[0].toggleState = 1
            self.activeOctave=0

        elif keys[pygame.K_2]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[2].toggleState = 1
            self.activeOctave = 2

        elif keys[pygame.K_1]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[1].toggleState = 1
            self.activeOctave = 1

        elif keys[pygame.K_3]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[3].toggleState = 1
            self.activeOctave = 3

        elif keys[pygame.K_4]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[4].toggleState = 1
            self.activeOctave = 4
        elif keys[pygame.K_5]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[5].toggleState = 1
            self.activeOctave = 5
        elif keys[pygame.K_6]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[6].toggleState = 1
            self.activeOctave = 6
        elif keys[pygame.K_7]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[7].toggleState = 1
            self.activeOctave = 7


        elif keys[pygame.K_8]:
            self.octavebutton[self.activeOctave].toggleState = 0
            self.octavebutton[8].toggleState = 1
            self.activeOctave = 8


