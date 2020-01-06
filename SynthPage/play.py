from DrumPage.Buttons import toggleBtn
from SynthPage import getSinSound
from SynthPage import getSillence
import pygame


class PlayBtn():
    def __init__(self,game):
        self.game=game
        self.play = toggleBtn(game)


    def __call__(self, *args, **kwargs):
        self.game.synthFlag = 1


        #deafultColor, otherColor, onStr ="",fontSize = None, hoverStr= "", whenClicked = None):
        notename = self.game.mainmenu.synthMain.displaynotes.activeNote + \
                 str(self.game.mainmenu.synthMain.displayoctave.activeOctave)
        hvrstr= "Play"

        notes = self.game.mainmenu.synthMain.melody.notes


        self.play.button("Play",
                         self.game.displayW*.75,
                         0,
                         self.game.buttonSize*6,
                         self.game.buttonSize * 3,
                         self.game.lightpurple,
                         self.game.bright_blue,
                         hoverStr=hvrstr,
                         fontSize=self.game.menuText,
                         whenClicked= lambda: (self.playClick(notes)))


    def playClick(self,list):

        sound = 0


        for i in range(len(list)):
            freq = self.game.mainmenu.synthMain.freqs[list[i][2]]

            if list[i][1] == 1:
                sound += getSinSound(freq,list[i][0], bpm=self.game.bpm)

            else:
                sound +=getSillence(list[i][0],bpm=self.game.bpm)


        filename = "SynthPage/play.wav"

        sound.export(filename,format = "wav")


        self.playSOUND = pygame.mixer.Channel(5).play(pygame.mixer.Sound(filename))

        self.play.toggleState=0



