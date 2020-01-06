import pygame
from DrumPage.Buttons import toggleBtn
from PlayBoth import PlayAll
from PlayBoth import Stop


class PlayDrumsAndSynth():
    def __init__(self,game):
        self.game = game
        self.playandpause = PlayAll(self.game,"Play",
                                    self.game.displayW*.05,
                                    self.game.displayH*.05,
                                    10,
                                    10,
                                    self.game.white,
                                    self.game.green)

        self.stopbtn = Stop(self.game,"Stop",
                                    self.game.displayW*.05 * 2 + 10,
                                    self.game.displayH*.05,
                                    10,
                                    10,
                                    self.game.white,
                                    self.game.green)

        self.question = toggleBtn(self.game)

        self.EpilepsyQuestion = 0

        self.EpilepticFlag=0

        self.yesBtn = toggleBtn(self.game)
        self.noBtn = toggleBtn(self.game)




    def __call__(self, *args, **kwargs):

        if self.EpilepsyQuestion==0:
            TextSurf, TextRect = self.game.text_objects("Do you Have Epilepsy?", self.game.menuText)

            TextRect.center = (self.game.displayW / 2., self.game.displayH * .1)

            self.game.gameDisplay.blit(TextSurf, TextRect)

            self.yesBtn.button("Yes",self.game.displayW/2. - 100*2,
                               self.game.displayH * .3,
                               100,
                               40,
                               self.game.white,
                               self.game.green,
                               hoverStr="I Am Epileptic",
                               whenClicked=self.yesClick)

            self.noBtn.button("No",self.game.displayW/2. +100,
                               self.game.displayH * .3,
                               100,
                               40,
                               self.game.white,
                               self.game.green,
                               hoverStr="I Am Not Epileptic",
                               whenClicked=self.noClick)



        else:


            self.playandpause()
            if self.playandpause.toggleState==1:
                if self.EpilepticFlag ==0:
                    self.game.design(pygame.time.get_ticks())
                self.stopbtn()
            else:

                self.game.dialUp()
                self.game.dialDown()
                self.game.printBPM()



                self.question.button("?",
                                 self.game.displayW*.9,
                                 self.game.displayH - self.game.buttonSize,
                                 self.game.buttonSize * 4,
                                self.game.buttonSize,
                                 self.game.white,
                                 self.game.green,
                                     whenClicked=self.questionClick)



    def yesClick(self):
        self.EpilepsyQuestion =1
        self.EpilepticFlag = 1
        self.yesBtn.toggleState=0


    def noClick(self):
        self.EpilepsyQuestion =1
        self.EpilepticFlag = 0
        self.noBtn.toggleState = 0

    def questionClick(self):
        self.EpilepsyQuestion = 0
        self.question.toggleState=0
