import pygame
from Main.MISC.getFiles import getFileNames
from Main.DrumPage.Buttons.ToggleButtons import toggleBtn
from math import *

BORDER =0

VERBOSE = 1

class DisplayRhythmSprits:
    def __init__(self,game):
        self.game = game
        self.restList,self.restDList,self.noteList,self.noteDList =parseFileNames(getFileNames('SynthPage/Sprits'),
                                                                                  "SynthPage/Sprits/")

        self.dottedBtn = toggleBtn(self.game)
        self.noteBtn = toggleBtn(self.game)

        self.width = self.game.displayW * .6
        self.height = self.game.displayH * .3
        self.x = int((self.game.displayW - self.width)/2 + self.width*.1)
        self.y = self.game.displayH - self.height

        self.buttonSize = 80
        self.restSprits = self.getSprits(self.restList)
        self.restDSprits = self.getSprits(self.restDList)
        self.noteSprits = self.getSprits(self.noteList)
        self.noteDSprits = self.getSprits(self.noteDList)

        self.restgrid = [0] * len(self.restList)
        self.restDgrid = [0] * len(self.restList)
        self.notegrid = [0] * len(self.restList)
        self.noteDgrid = [0] * len(self.restList)

        for i in range(len(self.restList)):
            self.restgrid[i] = toggleBtn(self.game)
            self.restDgrid[i] = toggleBtn(self.game)
            self.notegrid[i] = toggleBtn(self.game)
            self.noteDgrid[i] = toggleBtn(self.game)


        self.printstr = ""



    def __call__(self, *args, **kwargs):

        keys = pygame.key.get_pressed()

        #self, name, x, y, w, h, deafultColor, otherColor, onStr ="",fontSize = None, hoverStr= "",


        self.dottedBtn.button(
                              "Dotted Notes",
                              self.x + self.width,
                              self.y,
                              self.buttonSize,
                              self.buttonSize,
                              self.game.yellow,
                              self.game.lightpurple,
                                onStr="Dot Off",
                                onColor=self.game.blue,
                                hoverStr="Change")

        self.noteBtn.button(
                              "Rest",
                              self.x +self.width ,
                              self.y+self.height -  self.buttonSize,
                              self.buttonSize,
                              self.buttonSize,
                              self.game.yellow,
                              self.game.lightpurple,
                                onStr="Note",
                                onColor=self.game.blue,
                                hoverStr="Change")

        if BORDER is 1:
            i = 0
            PL = getSquarePL(i, self.x, self.y, self.width, self.height)
            pygame.draw.polygon(self.game.gameDisplay, self.game.black, PL, 4)


        if self.dottedBtn.toggleState is 1 and self.noteBtn.toggleState is 0: #Dotted Note
            for i in range(len(self.noteDList)-1): # - 1 because a dotted 16th would need a 32nd note
                self.noteDgrid[i].button("",
                                        self.x + i *self.buttonSize,
                                        self.y + self.buttonSize / 2.,
                                        self.buttonSize,
                                        self.buttonSize,
                                        self.game.lightpurple,
                                        self.game.white,
                                        whenClicked= (lambda : self.whenClicked(i,self.noteDgrid))
                )

                self.game.gameDisplay.blit(self.noteDSprits[i], (self.x + i *self.buttonSize, self.y +self.buttonSize/2.))


            self.gridKeys(self.noteDgrid,keys, 1)





        elif self.dottedBtn.toggleState is 0 and self.noteBtn.toggleState is 0: #Note
            for i in range(len(self.noteDList)):
                self.notegrid[i].button("",
                                        self.x + i *self.buttonSize,
                                        self.y + self.buttonSize / 2.,
                                        self.buttonSize,
                                        self.buttonSize,
                                        self.game.lightpurple,
                                        self.game.white,
                                        whenClicked= (lambda : self.whenClicked(i,self.notegrid))
                )
                self.game.gameDisplay.blit(self.noteSprits[i], (self.x + i *self.buttonSize, self.y +self.buttonSize/2.))

            self.gridKeys(self.notegrid, keys)

        elif self.dottedBtn.toggleState is 0 and self.noteBtn.toggleState is 1:  # Rest
            for i in range(len(self.noteDList)):
                self.restgrid[i].button("",
                                        self.x + i *self.buttonSize,
                                        self.y + self.buttonSize / 2.,
                                        self.buttonSize,
                                        self.buttonSize,
                                        self.game.lightpurple,
                                        self.game.white,
                                        whenClicked= (lambda : self.whenClicked(i,self.restgrid))
                )
                self.game.gameDisplay.blit(self.restSprits[i],
                                           (self.x + i * self.buttonSize, self.y + self.buttonSize / 2.))

            self.gridKeys(self.restgrid, keys)

        elif self.dottedBtn.toggleState is 1 and self.noteBtn.toggleState is 1:  # Dotted Rest
            for i in range(len(self.noteDList)-1):# - 1 because a dotted 16th would need a 32nd note
                self.restDgrid[i].button("",
                                        self.x + i *self.buttonSize,
                                        self.y + self.buttonSize / 2.,
                                        self.buttonSize,
                                        self.buttonSize,
                                        self.game.lightpurple,
                                        self.game.white,
                                        whenClicked= (lambda : self.whenClicked(i,self.restDgrid))
                )
                self.game.gameDisplay.blit(self.restDSprits[i],
                                           (self.x + i * self.buttonSize, self.y + self.buttonSize / 2.))

            self.gridKeys(self.restDgrid, keys, 1)


        if VERBOSE == 1:
            printstr = str(self.game.mainmenu.synthMain.displayscale.activeScale)
            TextSurfDebug, TextRectDebug = self.game.text_objects(self.printstr, self.game.largeText)
            TextRectDebug.center = (self.game.displayW / 2, int(self.game.displayH * .9 + self.game.displayH * .05))
            self.game.gameDisplay.blit(TextSurfDebug, TextRectDebug)




        if keys[pygame.K_PERIOD]:
            self.dottedBtn.toggleState ^=1

        elif keys[pygame.K_r]:
            self.noteBtn.toggleState ^=1





    def whenClicked(self,num,grid):
        for i in range(len(grid)):
            if i !=num:
                grid[i].toggleState = 0







    def getSprits(self,list):
        res = []
        for i in list:
            img = pygame.image.load(i)
            res.append(pygame.transform.scale(img,(self.buttonSize,self.buttonSize)))

        return res

    def gridKeys(self,grid,keys,minuslen=0):
        activeState =-1

        if keys[pygame.K_a] or keys[pygame.K_d]:
            for i in range(len(grid)-minuslen):
                if grid[i].toggleState:
                    activeState=i
                    break

            if activeState ==-1:
                grid[0].toggleState = 1

            else:
                grid[activeState].toggleState = 0
                if keys[pygame.K_a]:
                    grid[(activeState - 1) %(len(grid ) -minuslen )].toggleState=1

                else: ## d
                    grid[(activeState + 1) % (len(grid) - minuslen)].toggleState = 1


def parseFileNames(files, dir):

    rest = []
    restD = []
    note = []
    noteD = []

    for file in files:
        if file[-3:] != "png":
            #print file[-3:]
            continue


        if file[1:3] == "ND":
            noteD.append(dir +file)
        elif file[1:3] == "NN":
            note.append(dir +file)
        elif file[1:3] == "RD":
            restD.append(dir + file)
        elif file[1:3] == "RN":
            rest.append(dir +file)

        #else:
            #print file, "NO GOOD"

    return [rest,restD,note,noteD]




def getSquarePL(i,xpos,ypos,xleg,yleg):

    # print (xpos,ypos),leg

    PL = [(xpos,
           ypos + i * yleg * 1.5),

          (xpos + xleg,
           ypos + i * yleg * 1.5),

          (xpos + xleg,
           ypos + i * yleg * 1.5 + yleg),

          (xpos,
           ypos + i * yleg * 1.5 + yleg)]

    return PL
