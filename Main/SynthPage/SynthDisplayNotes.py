import pygame
from Main.DrumPage.Buttons.ToggleButtons import toggleBtn


#self.game.mainmenu.synthMain.displaynotes
class DisplayNotes():
    def __init__(self,game):
        self.game= game
        self.notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        self.notesButtons = [0] * len(self.notes)
        for i in range(len(self.notes)):
            self.notesButtons[i] = toggleBtn(self.game,1)

        self.notesButtons[0].toggleState=1

        self.activeNote = "C"






    def __call__(self, *args, **kwargs):
        for i in range(len(self.notes)):
#def button(self, name, x, y, w, h, deafultColor, otherColor, onStr ="",fontSize = None, hoverStr= "", whenClicked = None):
            self.notesButtons[i].button(self.notes[i],
                                        self.game.displayW * .1,
                                        self.game.displayH * .1 + i * self.game.buttonSize *1.5,
                                        self.game.buttonSize,
                                        self.game.buttonSize,
                                        self.game.lightpurple,
                                        self.game.bright_gray,
                                        onStr = self.notes[i],
                                        hoverStr = self.notes[i],
                                        whenClicked = (lambda: self.noteclicked(i)) #pass a function with argument as a
                                        #function call back
                                        )

        if self.game.mainmenu.synthMain.displayscale.activeScale != -1:
            for i in range(len(self.notesButtons)):
                PL = [(self.game.displayW * .1,
                       self.game.displayH * .1 + i * self.game.buttonSize *1.5),



                      (self.game.displayW * .1 +self.game.buttonSize,
                       self.game.displayH * .1 + i * self.game.buttonSize * 1.5),



                      (self.game.displayW * .1 +self.game.buttonSize,
                       self.game.displayH * .1 + i * self.game.buttonSize * 1.5 + self.game.buttonSize),

                      (self.game.displayW * .1,
                       self.game.displayH * .1 + i * self.game.buttonSize * 1.5 + self.game.buttonSize),
                      ]

                if self.game.mainmenu.synthMain.displayscale != -1:
                    note = self.game.mainmenu.synthMain.displaynotes.notes[i]
                    if self.game.mainmenu.synthMain.displayroot.rootDict is not None and \
                            self.game.mainmenu.synthMain.displayscale.activeScale != -1  \
                            and self.game.mainmenu.synthMain.displayroot.rootDict[note] == 1:
                        pygame.draw.polygon(self.game.gameDisplay, self.game.black,PL,1 )



    def noteclicked(self,num):
        for i in range(len(self.notesButtons)):
            if i != num:
                self.notesButtons[i].toggleState=0

        self.notesButtons[num].toggleState =1

        self.activeNote = self.notes[num]



