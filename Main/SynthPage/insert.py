from Main.DrumPage.Buttons.ToggleButtons import toggleBtn
from Main.SynthPage.DisplayMelody import checkStates
from Main.SynthPage.DisplayMelody import startState
import copy
import pygame

REST = -1
NOTE = 1

# 4 beats in a measure
WHOLE = 1
DOTTEDWHOLE= WHOLE*1.5
HALF = 1 / 2.
DOTTEDHALF = HALF * 1.5
QUARTER = 1 / 4.
DOTTEDQUARTER = QUARTER*1.5
EIGHTH = 1 / 8.
DOTTEDEIGTH= EIGHTH*1.5
SIXTEENTH = 1 / 16.
DOTTEDSIXTEENTH = SIXTEENTH * 1.5





##shift button

#insert
class InsertNote():
    def __init__(self,game):
        self.game = game
        self.insertBtn = toggleBtn(self.game)
        self.undoBtn = toggleBtn(self.game)
        self.redoBtn = toggleBtn(self.game)
        self.FLAG = 0
        self.undo = []
        self.redo = []

    def __call__(self, *args, **kwargs):

        insertKey = self.game.mainmenu.synthMain.melody.activeToggle
        width = self.game.buttonSize*3
        state,newNote = self.getState()
        if insertKey>=0 and state>=0:

            self.insertBtn.button("Insert",
                              self.game.displayW - width - self.game.buttonSize*2,
                              self.game.buttonSize*3,
                              self.game.buttonSize*4,
                              self.game.buttonSize,
                              self.game.white,
                              self.game.bright_gray,
                              fontSize=self.game.BiggerText,
                              hoverStr="Insert",
                              whenClicked= (lambda: self.whenClickedInsert(insertKey,newNote)))

            if self.undo !=[]:

                self.undoBtn.button("Undo",
                                      self.game.displayW - width - self.game.buttonSize * 2,
                                      self.game.buttonSize * 3 * 2,
                                      self.game.buttonSize * 4,
                                      self.game.buttonSize,
                                      self.game.white,
                                      self.game.bright_gray,
                                      fontSize=self.game.BiggerText,
                                      hoverStr="Undo",
                                      whenClicked=self.whenClickedUndo)

            if self.redo !=[]:
                self.redoBtn.button("Redo",
                                    self.game.displayW - width - self.game.buttonSize * 2,
                                    self.game.buttonSize * 3 * 3,
                                    self.game.buttonSize * 4,
                                    self.game.buttonSize,
                                    self.game.white,
                                    self.game.bright_gray,
                                    fontSize=self.game.BiggerText,
                                    hoverStr="Redo",
                                    whenClicked=self.whenClickedRedo)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.whenClickedInsert(insertKey, newNote)



    def whenClickedUndo(self):
        undopop = self.undo.pop(-1)
        curentclone = copy.deepcopy(self.game.mainmenu.synthMain.melody.notes)
        self.game.mainmenu.synthMain.melody.notes = undopop


        self.redo.append(curentclone)




        self.undoBtn.toggleState = 0

    def whenClickedInsert(self,noteposition,notelen):

        note = self.game.mainmenu.synthMain.displaynotes.activeNote
        octave = self.game.mainmenu.synthMain.displayoctave.activeOctave
        statenotes = copy.deepcopy(self.game.mainmenu.synthMain.melody.notes)
        noteName = note + str(octave)

        undocopy = copy.deepcopy(statenotes)
        # add current state to undo, create a copy so the values won't get changed.




        # Check what the note is interrupting and cut it off accordingly.
        # state notes = (NOTE, REST, NOTENAME, TIE)
        notesum = 0

        if notelen < 0:
            notebool = REST
        else:
            notebool = NOTE

        overflow = (noteposition) / 16. + abs(notelen)

        newnotes = []
        if overflow >4:
            #print "OVERFLOW",(noteposition) / 16.

            amount = 4 - (noteposition) / 16.

            for i in range(len(statenotes)):
                notesum +=abs(statenotes[i][0])


                if notesum>(noteposition) / 16.:
                    break


                newnotes.append(statenotes[i])

            newnotes.append((amount,notebool,noteName))

            status = checkStates(newnotes)
            if status is False:

                newnoteposition = notesum - (noteposition) / 16.

                popnotes = newnotes.pop(-1)

                newnotes.append((statenotes[i][0] -  newnoteposition, statenotes[i][1],statenotes[i][2]))
                newnotes.append(popnotes)

                #newnotes.append(statenotes[i])


                #newnotes.append((statenotes[i][0] -  newnoteposition, notebool,noteName))

                status = checkStates(newnotes)

                if status:
                    self.game.mainmenu.synthMain.melody.notes = newnotes
                #else:
                    #print  newnotes
            else:

                #print "status: ", status

                self.game.mainmenu.synthMain.melody.notes = newnotes

        else: #no overflow
            noteposition = (noteposition) / 16.


            #print "note position:", noteposition
            for i in range(len(statenotes)):

                notesum += abs(statenotes[i][0])

                if notesum> noteposition:
                    break

                else:
                    newnotes.append(statenotes[i])

            newnoteposition = notesum  -abs(statenotes[i][0])

            ### CHECK NEXT NOTE
            add = None
            newi = i
            newnotesum = 0
            for i in range(newi, len(statenotes)):

                if i> newi or noteposition == newnoteposition:
                    newnotesum += abs(statenotes[i][0])

                else:
                    overlap =  noteposition - newnoteposition

                    newnotesum = abs(statenotes[i][0]) - overlap
                    newnotes.append((overlap,statenotes[i][1],statenotes[i][2])) #should be states[i][2]


                if newnotesum > abs(notelen):


                    checksum = newnotesum - statenotes[i][0]

                    if checksum < abs(notelen):

                        leaving = abs(statenotes[i][0]) - abs(notelen) + checksum

                        add = (leaving,statenotes[i][1],statenotes[i][2])# Should be third/
                        i +=1

                    break

            newi = i


            newnotes.append((abs(notelen),notebool,noteName))


            if add is not None:
                newnotes.append(add)

            if newi != len(statenotes)-1:
                for i in range(newi,len(statenotes)):
                    newnotes.append(statenotes[i])
            else:
                if checkStates(newnotes):
                    pass
                else:
                    newnotes.append(statenotes[-1])


            status = checkStates(newnotes)

            if status:
                self.game.mainmenu.synthMain.melody.notes = newnotes


        #print newnotes
        res = self.makeTies(newnotes)
        #print res

        if res != None and checkStates(res):
            self.game.mainmenu.synthMain.melody.notes = res

            if res != undocopy:
                self.undo.append(undocopy)





        else:
            print "res failed"
            print res

            exit()







        self.insertBtn.toggleState=0
        self.redo = []

    def whenClickedRedo(self):


        redopop = self.redo.pop(-1)
        self.game.mainmenu.synthMain.melody.notes = redopop

        clone = copy.deepcopy(redopop)

        self.undo.append(clone)


        self.redoBtn.toggleState=0

    def getState(self):
        self.restgrid = self.game.mainmenu.synthMain.sprits.restgrid
        self.restDgrid = self.game.mainmenu.synthMain.sprits.restDgrid
        self.notegrid = self.game.mainmenu.synthMain.sprits.notegrid
        self.noteDgrid = self.game.mainmenu.synthMain.sprits.noteDgrid
        dotted = self.game.mainmenu.synthMain.sprits.dottedBtn.toggleState
        rest = self.game.mainmenu.synthMain.sprits.noteBtn.toggleState

        newnote = -1
        state = -1
        if dotted and rest:  # dotted rest
            for i in range(len(self.restDgrid) - 1):
                if self.restDgrid[i].toggleState == 1:
                    state = i



        elif dotted and rest == 0:  # dotted note
            for i in range(len(self.noteDgrid) - 1):
                if self.noteDgrid[i].toggleState == 1:
                    state = i


        elif dotted == 0 and rest:  # normal rest
            for i in range(len(self.restgrid)):
                if self.restgrid[i].toggleState == 1:
                    state = i

        else:  # dotted ==0 and rest ==0 normal note
            for i in range(len(self.notegrid)):
                if self.notegrid[i].toggleState == 1:
                    state = i


        if state >= 0:
            # STATE 0 equal 1
            # STATE 1 equal .5, state 2 = .25, state 3 = 1/8., state 4 = 1/16.
            if state is 0:
                newnote = 1
            elif state is 1:
                newnote = 1 / 2.
            elif state is 2:
                newnote = 1 / 4.
            elif state is 3:
                newnote = 1 / 8.
            elif state is 4:
                newnote = 1 / 16.

            if dotted:
                newnote *= 1.5

            if rest:
                newnote *= -1

        return state, newnote


    def makeTies(self, list):

        orglist = copy.deepcopy(list)
        list =  copy.deepcopy(list)



        sum=0
        newlist = []
        for i in range(len(list)):
            sum += list[i][0]

            if sum==1:
                sum=0
                #print "yes"

            elif sum>=2:
                #print "panic"
                left = 2 - (sum - list[i][0])
                if left<1:
                    newlist.append((left, list[i][1], list[i][2], "Right"))  ### tie to the right
                else:
                    newlist.append((left -1, list[i][1], list[i][2], "Right"))  ### tie to the right


                nextline = sum % 1

                if sum > 2:
                    newlist.append((1.0, list[i][1], list[i][2], "BOTH"))
                else:
                    newlist.append((1.0, list[i][1], list[i][2], "Left"))


                newlist.append((nextline, list[i][1], list[i][2], "Left"))  # tie comes from the right
                sum = nextline
                #print left, 1, nextline, sum, left + 1 + nextline
                continue

            elif sum>1:
                #print "NO", i, list[i]
                left = 1 - (sum  - list[i][0])
                newlist.append((left, list[i][1],list[i][2], "Right")) ### tie to the right
                nextline =  sum%1
                newlist.append((nextline, list[i][1], list[i][2], "Left")) # tie comes from the right
                sum = nextline
                continue



            newlist.append(list[i])

        if newlist != []:
            list = newlist

        res = []



        NoteLen = [DOTTEDHALF, HALF, DOTTEDQUARTER, QUARTER, DOTTEDEIGTH, EIGHTH, SIXTEENTH]
        for i in range(len(list)):
            if str(list[i][0] * 1.0) not in self.game.mainmenu.synthMain.melody.imgDict:
                total = list[i][0]
                new = []
                j = 0
                while total>0:

                    if total>=NoteLen[j]:
                        new.append(NoteLen[j])
                        total-=NoteLen[j]
                        continue

                    j +=1

                    #print total




                #print list
                addList = []
                for j in range(len(new)):
                    if j == 0:
                        addList.append((new[j],list[i][1],list[i][2],"Right"))

                    elif j == len(new) -1:
                        addList.append((new[j], list[i][1], list[i][2], "Left"))

                    else:
                        addList.append((new[j], list[i][1], list[i][2], "BOTH"))




                #list = list[:i] + addList + list[i+1:]

                res +=  addList

            else:

                res.append(list[i])










        status = checkStates(res)

        if status:

            #self.game.mainmenu.synthMain.melody.notes = list
            return res
        else:
            #print "ERROR \n", res

            print orglist
            print res

            return  None


