import pygame
from Main.DrumPage.Buttons.ToggleButtons import toggleBtn
from Main.SynthPage.SoundGenerator import makeScale

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
        keys = pygame.key.get_pressed()
        for i in range(len(self.notes)):
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


                note = self.game.mainmenu.synthMain.displaynotes.notes[i]

                self.rootNote = self.game.mainmenu.synthMain.displayroot.rootNote

                self.rootDict = dict()

                scale = self.game.mainmenu.synthMain.scales[self.game.mainmenu.synthMain.displayscale.activeScale]
                ms = makeScale(self.rootNote, scale)

                for i in ms:
                    self.rootDict[i] = 1

                for i in self.game.mainmenu.synthMain.displaynotes.notes:
                    if i not in self.rootDict:
                        self.rootDict[i] = -1




                if self.rootDict[note] == 1:
                    pygame.draw.polygon(self.game.gameDisplay, self.game.black,PL,1 )


            self.keyPressed(self.rootDict,keys)

        else:
            self.keyPressed(None,keys)




    def noteclicked(self,num):
        for i in range(len(self.notesButtons)):
            if i != num:
                self.notesButtons[i].toggleState=0

        self.notesButtons[num].toggleState =1

        self.activeNote = self.notes[num]


    def keyPressed(self, dix,keys):


        notesums=-1
        activeNote = -1
        if dix is None:
            notesums = -1

        count =0
        for i in self.notes:

            if i == self.activeNote:
                activeNote=count
                break

            count +=1


        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.notesButtons[activeNote].toggleState = 0

            if dix== None: # no scale -> free to go to any note

                if keys[pygame.K_w]:
                    #print activeNote
                    newNote = (activeNote-1) % len(self.notes)

                else:
                    newNote =(activeNote+1) % len(self.notes)




                #pass any

            else:
                newNote=-1
                if keys[pygame.K_w]:

                    while newNote ==-1:
                        activeNote -= 1
                        newNote = (activeNote) % len(self.notes)

                        if dix[self.notes[newNote]] ==-1:
                            newNote =-1

                else:

                    while newNote == -1:
                        activeNote +=1
                        newNote = (activeNote) % len(self.notes)

                        #print newNote, self.notes[newNote], dix[self.notes[newNote]]

                        #print newNote
                        if dix[self.notes[newNote]] ==-1:
                            newNote = -1



            self.notesButtons[newNote].toggleState=1

            self.activeNote = self.notes[newNote]




