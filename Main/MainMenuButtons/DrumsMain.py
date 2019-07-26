
from Main.DrumPage.ModDrum import ModifyDrumLoop
from Main.DrumPage.Buttons.ToggleButtons import Grid
from Main.DrumPage.ToolBar import Tool
from Main.DrumPage.DrumSequencerMain import DrumLoop
from Main.MISC.getFiles import getFilesFromFolder as getSoundNames


class DrumsMain():
    def __init__(self,game):
        self.game = game
        self.game.numButtonRow = 8
        self.game.numButtonCol = 16
        self.game.numberofmeasures = 4
        self.game.activeMeasure = 1

        self.game.drumSounds = getSoundNames('Sounds')

        self.game.drumloopFlag = 1
        self.game.moddrumFlag = 0

        self.game.modifyDrumPage = ModifyDrumLoop(self.game)


        self.game.grid = [0] * self.game.numberofmeasures

        for i in range(self.game.numberofmeasures):
            self.game.grid[i] = Grid(self.game)


        self.game.toolbar = Tool(self.game)

        self.game.bpm = 95


        self.game.drumMain = DrumLoop(self.game)



    def __call__(self, *args, **kwargs):
        if self.game.drumloopFlag == 1:
            self.game.drumMain()

        if self.game.moddrumFlag == 1:
            self.game.modifyDrumPage()




