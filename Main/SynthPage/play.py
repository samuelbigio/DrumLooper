from Main.DrumPage.Buttons.ToggleButtons import toggleBtn
from Main.SynthPage.SoundGenerator import getSinSound
import pygame


class PlayBtn():
    def __init__(self,game):
        self.game=game
        self.play = toggleBtn(game)


    def __call__(self, *args, **kwargs):


        #deafultColor, otherColor, onStr ="",fontSize = None, hoverStr= "", whenClicked = None):
        hvrstr = self.game.mainmenu.synthMain.displaynotes.activeNote + \
                 str(self.game.mainmenu.synthMain.displayoctave.activeOctave)

        self.play.button("Play",
                         self.game.displayW/2,
                         self.game.displayH/2.,
                         self.game.buttonSize*8,
                         self.game.buttonSize * 4,
                         self.game.lightpurple,
                         self.game.bright_blue,
                         hoverStr=hvrstr,
                         fontSize=self.game.menuText,
                         whenClicked= lambda: (self.playClick(hvrstr)))


    def playClick(self,note):
        freq = self.game.mainmenu.synthMain.freqs[note]
        sound = getSinSound(freq,1)

        filename = "SynthPage/play.wav"

        sound.export(filename,format = "wav")


        self.playSOUND = pygame.mixer.Channel(5).play(pygame.mixer.Sound(filename))

        self.play.toggleState=0



