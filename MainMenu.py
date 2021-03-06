import pygame
from MainMenuButtons import DrumsMain
from MainMenuButtons import SynthMain
from DrumPage.Buttons import toggleBtn
from MainMenuButtons import PlayDrumsAndSynth


class MainMenu():
    def __init__(self,game):
        self.game=game
        self.drumButton = toggleBtn(self.game)
        self.synthButton = toggleBtn(self.game)
        self.allButton = toggleBtn(self.game)
        self.drummain =  DrumsMain(self.game)
        self.synthMain = SynthMain(self.game)
        self.goBackToMenu = toggleBtn(self.game)
        self.playboth = PlayDrumsAndSynth(self.game)
        self.mainMenuFlag=1



        self.Status="None"







    def __call__(self, *args, **kwargs):

        if self.mainMenuFlag is 0:
            self.goBackToMenu.button("Back To Menu",
                                     0,
                                     self.game.displayH* 18.5/20.,
                                     self.game.displayW*.2,
                                     int(50),
                                     self.game.white,
                                     self.game.bright_gray,
                                     fontSize=self.game.BiggerText,
                                     whenClicked=self.goToMenu)

            if self.Status == "Drums":
                self.drummain()

            elif self.Status == "Synth":
                self.synthMain()

            elif self.Status == "Both":
                self.playboth()




        else:

            TextSurf, TextRect = self.game.text_objects("DrumLooper", self.game.GameText)

            TextRect.center = (self.game.displayW/2.,self.game.displayH * .1 )

            self.game.gameDisplay.blit(TextSurf, TextRect)

            self.drumButton.button("Make Drums",
                                   (self.game.displayW/2.)- int(self.game.displayW * .35)/2. ,
                                   self.game.displayH * .2,
                                   int(self.game.displayW * .35),
                                   int(self.game.displayH * .1),
                                   self.game.white,
                                   self.game.bright_gray,
                                   fontSize=self.game.menuText,
                                   hoverStr="Make sick beats",
                                   whenClicked=self.DrumMenu)


            self.synthButton.button("Make Synth",
                                   (self.game.displayW/2.) - int(self.game.displayW * .35)/2.  ,
                                   self.game.displayH * .2 +int(self.game.displayH * .15) ,
                                   int(self.game.displayW * .35),
                                   int(self.game.displayH * .1),
                                   self.game.white,
                                   self.game.bright_gray,
                                   fontSize=self.game.menuText,
                                   hoverStr="Make Melodies",
                                   whenClicked=self.SynthMenu)

            if self.game.synthFlag:

                self.allButton.button("Play Drums + Synth",
                                        (self.game.displayW / 2.) - int(self.game.displayW * .35) / 2.,
                                        self.game.displayH * .2 + int(self.game.displayH * .15 * 2),
                                        int(self.game.displayW * .35),
                                        int(self.game.displayH * .1),
                                        self.game.white,
                                        self.game.bright_gray,
                                        fontSize=self.game.BiggerText,
                                        hoverStr="",
                                        whenClicked=self.BothMenu)



    def BothMenu(self):
        self.allButton.toggleState=0
        self.mainMenuFlag =0
        self.Status = "Both"

    def DrumMenu(self):
        self.mainMenuFlag =0
        self.Status = "Drums"


    def SynthMenu(self):
        self.goBackToMenu.toggleState = 0
        self.mainMenuFlag =0
        self.Status = "Synth"

    def goToMenu(self):
        pygame.mixer.music.stop()
        self.playboth.playandpause.toggleState=0
        self.game.play.toggleState=0
        self.game.play1.toggleState=0
        self.drumButton.toggleState =0
        self.synthButton.toggleState =0
        self.mainMenuFlag=1
        self.goBackToMenu.toggleState=0





