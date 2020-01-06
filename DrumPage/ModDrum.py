### THIS is the menu page to modify the stock drrum kit sounds
from Buttons.PresetSounds import PresetSound
from Buttons.DrumLoopButton import DrumLoopButton
from Buttons.PresetKits import PresetKit
from Buttons.SoundTesterToggle import SoundTestToggle
from Buttons.SetStock import Setstock
from Buttons.SetAllKit import SetAllKit
from Buttons.SaveKit import SaveKit
from Buttons.LoadPresets import LoadPreset
from Buttons.LoadSavedKit import LoadSavedKit



class ModifyDrumLoop():
    def __init__(self,game):
        self.game= game


        self.savedkits = 0


        self.soundtestToggle = SoundTestToggle(self.game)
        self.activeSound = 'Sounds/808/808clap1.wav'

        self.drumLoopBtn = DrumLoopButton(game,self.game.yellow,self.game.bright_yellow)
        self.drumkits = PresetKit(self.game) #pick kits then those kits load the sounds
        self.presetsounds = PresetSound(self.game)
        self.loadpresets= LoadPreset(self.game)

        xBuffer = int(self.game.displayW * 2 / 30)
        yBuffer = int(self.game.displayH * .1)
        buttonsize = self.game.buttonSize
        widthgap= int(self.game.displayW  *.05)

        """
        self.stock = Setstock(self.game,
                              int(xBuffer * 5 + (self.game.numberofmeasures * (4.75) * buttonsize /2)) + widthgap,
                              int(self.game.displayH * .1 / 2 - buttonsize/2),
                              self.game.buttonSize, self.game.buttonSize,
                              self.game.blue,
                              self.game.bright_blue)
        """

        self.setAll = SetAllKit(self.game,
                              int(xBuffer * 6 + (self.game.numberofmeasures * (4.75) * buttonsize /2)) + widthgap,
                              int(self.game.displayH * .1 / 2 - buttonsize/2),
                              self.game.buttonSize, self.game.buttonSize,
                              self.game.blue,
                              self.game.bright_blue)

        self.saveKit = SaveKit(self.game,
                              int(xBuffer * 5 + (self.game.numberofmeasures * (4.75) * buttonsize /2)) + widthgap,
                              int(self.game.displayH * .1 / 2 - buttonsize/2),
                              self.game.buttonSize, self.game.buttonSize,
                              self.game.blue,
                              self.game.bright_blue)

        self.loadsavedkit = LoadSavedKit(self.game)



    def __call__(self, *args, **kwargs):
        self.game.measures()
        self.game.play()
        self.game.play1()
        ###Change sounds to
        self.game.sounds()
        self.saveKit()
        self.drumkits()
        self.presetsounds()
        self.drumLoopBtn()
        self.soundtestToggle()
        self.setAll()
        self.loadpresets()
        self.loadsavedkit()
