import pygame
from Main.MainMenuButtons.DrumsMain import DrumsMain
from Main.MainMenuButtons.SynthMain import SynthMain
from Main.DrumPage.Buttons.ToggleButtons import toggleBtn



class MainMenu():
    def __init__(self,game):
        self.game=game
        self.drumButton = toggleBtn(self.game)
        self.synthButton = toggleBtn(self.game)
        self.drummain =  DrumsMain(self.game)
        self.synthMain = SynthMain(self.game)
        self.goBackToMenu = toggleBtn(self.game)
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



        else:

            self.drumButton.button("Make Drums",
                                   self.game.displayW * .2,
                                   self.game.displayH * .2,
                                   int(self.game.displayW * .4),
                                   int(self.game.displayH * .1),
                                   self.game.white,
                                   self.game.bright_gray,
                                   fontSize=self.game.menuText,
                                   hoverStr="Make sick beats",
                                   whenClicked=self.DrumMenu)


            self.synthButton.button("Make Synth",
                                   self.game.displayW * .6,
                                   self.game.displayH * .4,
                                   int(self.game.displayW * .4),
                                   int(self.game.displayH * .1),
                                   self.game.white,
                                   self.game.bright_gray,
                                   fontSize=self.game.menuText,
                                   hoverStr="Make Melodies",
                                   whenClicked=self.SynthMenu)





    def DrumMenu(self):
        self.mainMenuFlag =0
        self.Status = "Drums"

    def SynthMenu(self):
        self.goBackToMenu.toggleState = 0
        self.mainMenuFlag =0
        self.Status = "Synth"

    def goToMenu(self):
        self.drumButton.toggleState =0
        self.synthButton.toggleState =0
        self.mainMenuFlag=1
        self.goBackToMenu.toggleState=0





