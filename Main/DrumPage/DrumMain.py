import pygame
from MISC.center_circles import CenterDesign
from Main.DrumPage.Buttons.SoundTester import SoundTest
from Buttons.ModDrums import ModifyDrumKit



BORDER = 0
Verbose = 0
DESIGN = 0

class DrumLoop():
    def __init__(self,game):
        self.game= game
        self.game.sounds = SoundTest(self.game)
        self.game.moddrumsBtn = ModifyDrumKit(self.game,self.game.yellow,self.game.bright_yellow)


        ## REPLACE SOON
        self.game.soundNames = ['kick', 'snare', 'hhcl', 'hhop', 'ride', 'crash', 'rim', 'shaker']
        for i in range(len(self.game.soundNames)):
            self.game.soundNames[i] = 'Sounds/kit1/' + self.game.soundNames[i] + '.wav'



        if DESIGN is 1:
            self.game.design = CenterDesign(self.game)

    def __call__(self, *args, **kwargs):



        if DESIGN is 1:
            self.game.design()

        for i in range(self.game.numberofmeasures):
            if i == self.game.activeMeasure:
                self.game.grid[i].readButtons()

        if BORDER == 1:
            # TOP BORDER
            pygame.draw.line(self.game.gameDisplay, self.game.black, (0, self.game.displayH * .1), (self.game.displayW, self.game.displayH * .1), 10)
            # BOTTOM BORDER
            pygame.draw.line(self.game.gameDisplay, self.game.black, (0, self.game.displayH * .9), (self.game.displayW, self.game.displayH * .9), 10)
            pygame.draw.line(self.game.gameDisplay, self.game.black,(self.game.displayW*.1, 0),(self.game.displayW*.1, self.game.displayH),10)
            pygame.draw.line(self.game.gameDisplay, self.game.black, (self.game.displayW * .9, 0),
                             (self.game.displayW * .9, self.game.displayH), 10)



        #todo make sound and kit load auttomatically

        self.game.moddrumsBtn()
        self.game.toolbar()
        self.game.printBPM()
        self.game.string = pygame.time.get_ticks()
        self.game.sounds()




        if Verbose == 1:
            TextSurfDebug, TextRectDebug = self.game.text_objects(str(self.game.string), self.game.largeText)
            TextRectDebug.center = (self.game.displayW / 2, int(self.game.displayH * .9 + self.game.displayH * .05))
            self.game.gameDisplay.blit(TextSurfDebug, TextRectDebug)





def text_objects(self,text, font, color = (0,0,0)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()



