from Main.DrumPage.Buttons.ToggleButtons import toggleBtn


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

    def octaveClicked(self,num):
        for i in range(len(self.octavebutton)):
            if i !=num:
                self.octavebutton[i].toggleState = 0

        self.activeOctave = num




