from SynthPage import DisplayNotes
from SynthPage import DisplayScale
from SynthPage import DisplayRoot
from SynthPage import getScales
from SynthPage.DisplayOctaves import DisplayOctaves
from SynthPage import getFreqs
from SynthPage.play import PlayBtn
from SynthPage import DisplayRhythmSprits
from SynthPage import DisplayMelody
from SynthPage.insert import InsertNote

VERBOSE = 0

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
        self.sprits = DisplayRhythmSprits(self.game)
        self.melody = DisplayMelody(self.game)
        self.insertNote = InsertNote(self.game)





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
        self.sprits()
        self.melody()
        self.insertNote()


        if VERBOSE == 1:
            printstr = str(self.game.mainmenu.synthMain.displayscale.activeScale)
            TextSurfDebug, TextRectDebug = self.game.text_objects(printstr, self.game.largeText)
            TextRectDebug.center = (self.game.displayW / 2, int(self.game.displayH * .9 + self.game.displayH * .05))
            self.game.gameDisplay.blit(TextSurfDebug, TextRectDebug)





