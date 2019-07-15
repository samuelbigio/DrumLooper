from Main.SynthPage.SynthDisplayNotes import DisplayNotes
from Main.SynthPage.DisplayScale import DisplayScale
from Main.SynthPage.DisplayRoot import DisplayRoot
from Main.SynthPage.SoundGenerator import getScales
from Main.SynthPage.DisplayOctaves import DisplayOctaves
from Main.SynthPage.SoundGenerator import getFreqs
from Main.SynthPage.play import PlayBtn

VERBOSE = 1

#self.game.mainmenu.synthMain.
class SynthMain():
    def __init__(self,game):
        self.game= game
        self.scales = getScales()
        self.freqs = getFreqs()
        self.displaynotes = DisplayNotes(self.game)
        self.displayscale = DisplayScale(self.game)
        self.displayroot = DisplayRoot(self.game)
        self.displayoctave =DisplayOctaves(self.game)
        self.synthPlay = PlayBtn(self.game)





    def __call__(self, *args, **kwargs):

        ### might move, might not
        self.game.printBPM()
        self.game.dialUp()
        self.game.dialDown()
        self.displaynotes()
        self.displayscale()
        self.displayroot()
        self.displayoctave()
        self.synthPlay()


        if VERBOSE == 1:
            printstr = str(self.game.mainmenu.synthMain.displayscale.activeScale)
            TextSurfDebug, TextRectDebug = self.game.text_objects(printstr, self.game.largeText)
            TextRectDebug.center = (self.game.displayW / 2, int(self.game.displayH * .9 + self.game.displayH * .05))
            self.game.gameDisplay.blit(TextSurfDebug, TextRectDebug)





