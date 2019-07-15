from Main.DrumPage.Buttons.ToggleButtons import toggleBtn
from Main.SynthPage.SoundGenerator import makeScale


#self.game.mainmenu.synthMain.displaynotes
class DisplayRoot():
    def __init__(self,game):
        self.game= game

        self.rootButton = toggleBtn(self.game)
        self.rootNote = "C"

        self.rootDict = None



        #self.game.mainmenu.synthMain.noteFreqs = getFreqs()









    def __call__(self, *args, **kwargs):


        hoverstr = self.game.mainmenu.synthMain.displaynotes.activeNote

        if self.game.mainmenu.synthMain.displayscale.activeScale != -1:
            hoverstr = hoverstr + " " + str(self.game.mainmenu.synthMain.displayscale.activeScale)


        self.rootButton.button("Root " + self.rootNote,
                                    self.game.displayW * .02,
                                    self.game.displayH * .05 ,
                                    self.game.buttonSize *3,
                                    self.game.buttonSize,
                                    self.game.lightpurple,
                                    self.game.bright_gray,
                                    onStr = "Pick Root",
                                    hoverStr = hoverstr,
                                    whenClicked = self.noteclicked,
                                    fontSize= self.game.BiggerText)




    def noteclicked(self):

        self.rootNote = self.game.mainmenu.synthMain.displaynotes.activeNote
        self.rootButton.toggleState = 0
        if self.game.mainmenu.synthMain.displayscale.activeScale != -1:

            self.rootDict = dict()
            scale = self.game.mainmenu.synthMain.scales[self.game.mainmenu.synthMain.displayscale.activeScale]
            ms = makeScale(self.game.mainmenu.synthMain.displaynotes.activeNote,scale)
            for i in ms:
                self.rootDict[i] = 1

            for i in self.game.mainmenu.synthMain.displaynotes.notes:
                if i not in self.rootDict:
                    self.rootDict[i] = -1

            #print self.rootDict
        else:
            self.rootDict = None

