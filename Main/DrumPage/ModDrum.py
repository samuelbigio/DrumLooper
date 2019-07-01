### THIS is the menu page to modify the stock drrum kit sounds
from Buttons.PresetSounds import PresetSound
from Buttons.DrumLoopButton import DrumLoopButton
from Buttons.PresetKits import PresetKit



class ModifyDrumLoop():
    def __init__(self,game):
        self.game= game
        self.drumLoopBtn = DrumLoopButton(game,self.game.yellow,self.game.bright_yellow)
        self.drumkits = PresetKit(self.game)
        self.presetsounds = PresetSound(self.game)




    def __call__(self, *args, **kwargs):
        self.game.measures()
        ###Change sounds to
        self.game.sounds()
        self.drumkits()
        self.presetsounds()
        self.drumLoopBtn()
