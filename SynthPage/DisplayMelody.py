import pygame
from SynthPage import getSquarePL
from DrumPage.Buttons import toggleBtn
from MISC import getFileNames


BORDER = 0
REST = -1
NOTE = 1

# 4 beats in a measure
WHOLE = 1.0
DOTTEDWHOLE= WHOLE*1.5
HALF = 1 / 2.
DOTTEDHALF = HALF * 1.5
QUARTER = 1 / 4.
DOTTEDQUARTER = QUARTER*1.5
EIGHTH = 1 / 8.
DOTTEDEIGTH= EIGHTH*1.5
SIXTEENTH = 1 / 16.
DOTTEDSIXTEENTH = SIXTEENTH * 1.5


class DisplayMelody():
    def __init__(self, game):
        self.game = game

        self.width = self.game.displayW * .65
        self.height = self.game.displayH * .575
        self.x = (self.game.displayW - self.width) / 2. + self.game.displayW * .05
        self.y = self.game.displayH * .1

        # divides the grid by height and width into 16 and takes the smallest then rounds to the lowest 10th.
        self.buttonSize = int(min(self.width / 16., self.height / 16.)) / 10 * 10

        # this would only happen if user can modify screen size and there is no minimum
        if self.buttonSize == 0:
            self.buttonSize = 5

        self.xbuffer = (self.width - self.buttonSize * 16) / 4.
        self.ybuffer = (self.height - self.buttonSize * 4) / 8.

        self.testImg = pygame.image.load('SynthPage/Sprits/5RN.png')

        self.smallImg = pygame.transform.scale(self.testImg, (self.game.buttonSize, self.game.buttonSize))
        self.BigImg = pygame.transform.scale(self.testImg, (self.game.buttonSize * 2, self.game.buttonSize * 2))

        self.notes = startState()

        self.btns = [0] * 16 * 4

        for i in range(len(self.btns)):
            self.btns[i] = toggleBtn(self.game)

        self.imgDict =self.parseFileNames(getFileNames('SynthPage/Sprits'),"SynthPage/Sprits/")
        self.activeToggle = -1


    def __call__(self, *args, **kwargs):

        self.showGrid()

        if BORDER == 1:
            self.displayBorder()

        self.showStates()


    def showStates(self):
        i = 0
        noteCount = 0
        while i < (len(self.btns)):
            beat,noteBool = self.notes[noteCount][0]*1.0,self.notes[noteCount][1]

            xbuffer,newI = self.getxbufferNewI(i)

            ybuffer, image = self.getybufferImg(beat,noteBool)

            textX,textY = self.textBuffer(abs(beat))






            self.game.gameDisplay.blit(image,
                                           (self.x + xbuffer + self.buttonSize*newI,
                                            self.y  + ybuffer + self.height*.25*int(i/16)))



            if self.notes[noteCount][1] == NOTE:
                addstr = ""
                if len(self.notes[noteCount]) == 4:
                    if self.notes[noteCount][3] == "Left":
                        addstr = " <-"
                    elif self.notes[noteCount][3] == "Right":

                        addstr = " ->"
                    elif self.notes[noteCount][3] == "BOTH":
                        addstr = " <->"


                TextSurf, TextRect = self.game.text_objects(self.notes[noteCount][2] + addstr, self.game.largeText)

                TextRect.center = (self.x + xbuffer + self.buttonSize * newI + textX,
                                   self.y + ybuffer + self.height * .25 * int(i / 16) + textY)

                self.game.gameDisplay.blit(TextSurf, TextRect)

            i += int(beat * 16)
            noteCount+=1


    def textBuffer(self,notelen):

        x = 0
        y =0

        if notelen< EIGHTH: #MUST BE SIXTEENTH
            x = self.buttonSize/3
            y = self.buttonSize*2.295

        elif notelen == EIGHTH:
            x = self.buttonSize/2.352 +4
            y = self.buttonSize*3

        else:
            x = self.buttonSize * 2
            y = self.buttonSize*4


        return x,y


    def showGrid(self):
        mouse = pygame.mouse.get_pos()
        for j in range(4):
            for i in range(16):
                if i < 4:
                    xbuffer = 0
                elif i < 8:
                    xbuffer = self.xbuffer

                elif i < 12:
                    xbuffer = self.xbuffer * 2

                else:
                    xbuffer = self.xbuffer * 3

                xbuffer += self.xbuffer / 2.

                x = self.x + xbuffer + self.buttonSize * i
                y = self.y + self.ybuffer + self.height * .25 * j

                buttonSize = self.buttonSize
                self.btns[(i + 16 * j)].button("", x, y, buttonSize, buttonSize, self.game.lightpurple, self.game.white,

                                               whenClicked=(lambda: self.whenGridClicked(i + 16 * j)))

                #pl = getSquarePL(0,x,y,buttonSize,buttonSize)
                #pygame.draw.polygon(self.game.gameDisplay, self.game.white,pl,1)
                #pygame.draw.rect(self.game.gameDisplay,self.game.white,(x,y,buttonSize,buttonSize),1)

                if ((mouse[0] < (self.width+ self.x) and mouse[0] > self.x) and
                        (mouse[1] < (self.y + self.height/4. *(j+1)) and mouse[1] > self.y + self.height/4. *j)):

                    pygame.draw.rect(self.game.gameDisplay, self.game.white, (x, y, buttonSize, buttonSize), 1)


                if i==0:
                    pygame.draw.line(self.game.gameDisplay,self.game.black,(x,y+buttonSize*1.5),(x,y-buttonSize/2.),4)
                if i == 15:
                    pygame.draw.line(self.game.gameDisplay, self.game.black, (x +buttonSize, y + buttonSize*1.5),
                                     (x+buttonSize, y - buttonSize/2.), 4)

    def whenGridClicked(self, num):
        for i in range(len(self.btns)):
            if i != num:
                self.btns[i].toggleState = 0

            else:
                if self.btns[num].toggleState == 1:
                    self.activeToggle = num
                else:
                    self.activeToggle = -1

    def displayBorder(self):
        i = 0
        pl = getSquarePL(i, self.x, self.y, self.width, self.height)

        pygame.draw.polygon(self.game.gameDisplay, self.game.black, pl, 4)

        pygame.draw.line(self.game.gameDisplay, self.game.black, (self.game.displayW / 2., 0),
                         (self.game.displayW / 2., self.game.displayH), 5)

        pygame.draw.line(self.game.gameDisplay, self.game.black,
                         (0, self.game.displayH / 2.),
                         (self.game.displayW, self.game.displayH / 2.), 5)

    def getxbufferNewI(self,i):
        newI = int(i) / 16

        if newI == 0:
            newI=i

        elif newI == 1:
            newI = i - 16

        elif newI == 2:
            newI = i - 32

        else:
            newI = i - 48

        if newI < 4:
            xbuffer = 0
        elif newI < 8:
            xbuffer = self.xbuffer

        elif newI < 12:
            xbuffer = self.xbuffer * 2

        else:
            xbuffer = self.xbuffer * 3

        xbuffer += self.xbuffer / 2.

        return xbuffer,newI

    def getybufferImg(self,beat,noteBool):

        unscaledImage = self.imgDict[str(beat * noteBool *1.0)]





        if beat == SIXTEENTH:
            image = pygame.transform.scale(unscaledImage, (self.game.buttonSize, self.game.buttonSize))
            ybuffer = self.ybuffer

        elif beat == EIGHTH:
            ybuffer = self.ybuffer / 2.
            image = pygame.transform.scale(unscaledImage, (self.game.buttonSize * 2, self.game.buttonSize * 2))

        else:  # beat >= QUARTER:
            ybuffer = 0
            image = pygame.transform.scale(unscaledImage, (self.game.buttonSize * 4, self.game.buttonSize * 4))

        return ybuffer,image


    def parseFileNames(self,files, dir):

        notevalues = dict()
        noteList = [WHOLE,HALF,QUARTER,EIGHTH,SIXTEENTH]
        for i in range(5):
            notevalues[str(i+1)] = noteList[i]

        imagedict=dict()
        for file in files:
            if file[-3:] != "png":
                #print file[-3:]
                continue



            if file[2] == "N":
                imagedict[str(file[:3])] =notevalues[file[0]]
                if file[1] == "R":
                    imagedict[str(file[:3])] *= -1

            else:
                imagedict[str(file[:3])] =notevalues[file[0]] *1.5
                if file[1] == "R":
                    imagedict[str(file[:3])] *= -1


        res =dict()
        for i in imagedict:

            #if imagedict[i] == 1:



            res[str(imagedict[str(i)])] = pygame.image.load(dir + i + '.png')


        return res



def startState():
    res = []

    # first measure
    res.append((WHOLE, REST,"C1"))

    # second measure
    for i in range(2):
        res.append((HALF, REST,"C2"))

    # third measure
    for i in range(4):
        res.append((QUARTER, REST,"C3"))

    # fourth measure
    for i in range(4):
        res.append((EIGHTH, REST,"C4"))

    for i in range(8):
        res.append((SIXTEENTH, REST,"C5"))


    #checkStatesBool = checkStates(res)
    #if checkStatesBool:
    return res

def checkStates( list):
    checksum = 0
    for i in range(len(list)):
        checksum += abs(list[i][0])

    if checksum == 4:
        return True

    return False

