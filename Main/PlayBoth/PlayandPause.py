import pygame
#import time
from pydub import AudioSegment
from Main.SynthPage.SoundGenerator import getSinSound
from Main.SynthPage.SoundGenerator import getSillence



PLOT = 0
if PLOT is 1:
    import scipy.io.wavfile
    import matplotlib.pyplot as plt


class PlayAll:
    def __init__(self,game,name, x, y, w, h, defaultColor, otherColor):
        self.game = game
        self.toggleState=0
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)
        self.defaultColor = defaultColor
        self.otherColor = otherColor



    def __call__(self, *args, **kwargs):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        name = self.name
        x= self.x
        y=self.y
        w =self.w
        h=self.h
        defaultColor = self.defaultColor
        otherColor=self.otherColor


        if self.toggleState ==0:
            pygame.draw.circle(self.game.gameDisplay, defaultColor, (x + w / 2, y + h / 2),20)
            TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)
            TextRect.center = ((x + w / 2), (y + h / 2))
            self.game.gameDisplay.blit(TextSurf, TextRect)


        else:
            pygame.draw.circle(self.game.gameDisplay, self.game.green, (x + w / 2, y + h / 2), 20)
            TextSurf, TextRect = self.game.text_objects("", self.game.largeText)
            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        if (( mouse[0] < (x + w) and mouse[0] > x ) and ( mouse[1] < (y+h) and mouse[1] > y ) ):


            if self.toggleState ==0:
                pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 20)
                TextSurf, TextRect = self.game.text_objects(":)", self.game.largeText)
                TextRect.center = ((x + w / 2), (y + h / 2))

                self.game.gameDisplay.blit(TextSurf, TextRect)

            if click[0] == 1:

                self.loadstr= "Loading..."
                TextSurf, TextRect = self.game.text_objects(self.loadstr, self.game.GameText)

                TextRect.center = (self.game.displayW / 2., self.game.displayH * .1)

                self.game.gameDisplay.blit(TextSurf, TextRect)

                self.game.mainmenu.playboth.stopbtn.toggleState = 0



                self.game.string = "Play"

                self.bpm = self.game.bpm

                self.toggleState = 1



                #start_time = time.time()

                res =0
                getSum = 0


                for i in range(len(self.game.measures.measureStates)):
                    getSum += self.game.measures.measureStates[i].toggleState

                if getSum ==0:
                    self.game.measures.measureStates[0].toggleState = 1



                for k in range(len(self.game.measures.measureStates)):
                    self.states = [[0 for i in range(self.game.numButtonCol)] for j in
                                   range(self.game.numButtonRow)]

                    for i in range(len(self.game.grid[0].ToggleButton)):
                        for j in range(len(self.game.grid[0].ToggleButton[0])):
                            self.states[j][i] = self.game.grid[k].ToggleButton[i][j].toggleState




                    res += makeWav(self,k)

                getSynthWav(self)





                playFile = 'SaveFiles/drumsandSynth.wav'
                pygame.mixer.music.pause()
                ##ghetto way of loading a new sound so pydub can't overwrite on the file that is loaded.
                pygame.mixer.music.load('SaveFiles/Dummy.wav')


                synthSound = getSynthWav(self)

                res = res.overlay(synthSound,position=0)

                res.export(playFile, format="wav")

                if PLOT is 1:
                    rate, data = scipy.io.wavfile.read(playFile)
                    plt.clf()
                    plt.figure(1)
                    plt.title('Signal Wave...')
                    plt.plot(data)
                    plt.savefig('test.png')


                self.loadstr= ""
                TextSurf, TextRect = self.game.text_objects(self.loadstr, self.game.GameText)

                TextRect.center = (self.game.displayW / 2., self.game.displayH * .1)

                self.game.gameDisplay.blit(TextSurf, TextRect)

                self.game.mainmenu.playboth.stopbtn.toggleState = 0

                pygame.mixer.music.load(playFile)
                pygame.mixer.music.play(-1)




def makeWav(self,measurenum):
    beat_in_milli = 60.0 / self.bpm * 1000 / 4

    sounds = [0] * len(self.states)
    for i in range(len(self.states)):

        sounds[i] = AudioSegment.from_wav(self.game.measures.sounds[measurenum][i])


        num=1
        statesChart = []
        for j in range(len(self.states[0])):
            if self.states[i][j] == 0:
                num +=1
            else:
                statesChart.append(num)
                num =1





        if statesChart == []:
            res = AudioSegment.silent(duration=beat_in_milli*16)

        else:

            res =  AudioSegment.silent(duration=(statesChart[0] - 1)*beat_in_milli )
            for j in range(1,len(statesChart)):
                length = statesChart[j] * beat_in_milli

                if len(sounds[i]) > length:
                    res +=sounds[i][:length]
                else:
                    missing= length - len(sounds[i])
                    res += sounds[i]
                    res += AudioSegment.silent(duration=missing)

            length = 16*beat_in_milli - len(res)
            if len(sounds[i]) > length:
                res += sounds[i][:length]
            else:
                missing = length - len(sounds[i])
                res += sounds[i]
                res += AudioSegment.silent(duration=missing)

        sounds[i] = res


    for i in range(1, len(sounds)):
        sounds[0] = sounds[0].overlay(sounds[i], position=0)


    return sounds[0]


def getSynthWav(self):
    sound = 0

    list = self.game.mainmenu.synthMain.melody.notes

    for i in range(len(list)):
        freq = self.game.mainmenu.synthMain.freqs[list[i][2]]

        if list[i][1] == 1:
            sound += getSinSound(freq, list[i][0], bpm=self.game.bpm)

        else:
            sound += getSillence(list[i][0], bpm=self.game.bpm)

    return sound


class Stop():
    def __init__(self,game,name, x, y, w, h, defaultColor, otherColor):
        self.game = game
        self.toggleState=0
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)
        self.defaultColor = defaultColor
        self.otherColor = otherColor
        self.toggleState=0

    def __call__(self, *args, **kwargs):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        name = self.name
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        defaultColor = self.defaultColor
        otherColor = self.otherColor

        pygame.draw.circle(self.game.gameDisplay, defaultColor, (x + w / 2, y + h / 2), 20)
        TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)
        TextRect.center = ((x + w / 2), (y + h / 2))
        self.game.gameDisplay.blit(TextSurf, TextRect)



        if ((mouse[0] < (x + w) and mouse[0] > x) and (mouse[1] < (y + h) and mouse[1] > y)):

            if self.toggleState == 0:
                pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 20)
                TextSurf, TextRect = self.game.text_objects(":)", self.game.largeText)
                TextRect.center = ((x + w / 2), (y + h / 2))

                self.game.gameDisplay.blit(TextSurf, TextRect)

            if click[0] == 1:
                self.game.mainmenu.playboth.playandpause.toggleState=0

                self.toggleState=1
                pygame.mixer.music.stop()


