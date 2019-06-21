import pygame
import time
from pydub import AudioSegment


class Play:
    def __init__(self,game,name, x, y, w, h, deafultColor, otherColor):
        self.game = game
        self.toggleState=0
        self.name = name
        self.x =x
        self.y=y
        self.w = w
        self.h = h
        self.deafultColor = deafultColor
        self.otherColor = otherColor

    def button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        name = self.name
        x= self.x
        y=self.y
        w =self.w
        h=self.h
        deafultColor = self.deafultColor
        otherColor=self.otherColor


        if self.toggleState ==0:
            #pygame.draw.rect(self.game.gameDisplay, deafultColor, (x, y, w, h))
            pygame.draw.circle(self.game.gameDisplay, deafultColor, (x + w / 2, y + h / 2),20)
            TextSurf, TextRect = self.game.text_objects(name, self.game.largeText)
            TextRect.center = ((x + w / 2), (y + h / 2))
            self.game.gameDisplay.blit(TextSurf, TextRect)
            #pygame.mixer.music.pause()


        else:
            #pygame.draw.rect(self.game.gameDisplay, self.game.green, (x, y, w, h))
            pygame.draw.circle(self.game.gameDisplay, self.game.green, (x + w / 2, y + h / 2), 20)
            TextSurf, TextRect = self.game.text_objects("stop", self.game.largeText)
            TextRect.center = ((x + w / 2), (y + h / 2))

            self.game.gameDisplay.blit(TextSurf, TextRect)

        if (( mouse[0] < (x + w) and mouse[0] > x ) and ( mouse[1] < (y+h) and mouse[1] > y ) ):

            if self.toggleState ==0:
                #pygame.draw.rect(self.game.gameDisplay, otherColor, (x, y, w, h))
                pygame.draw.circle(self.game.gameDisplay, otherColor, (x + w / 2, y + h / 2), 20)
                TextSurf, TextRect = self.game.text_objects("press me", self.game.largeText)
                TextRect.center = ((x + w / 2), (y + h / 2))

                self.game.gameDisplay.blit(TextSurf, TextRect)

            if click[0] == 1:
                self.bpm = self.game.bpm

                self.toggleState ^= 1

                #start_time = time.time()

                if self.toggleState == 1:

                    self.states = [[0 for i in range(self.game.numButtonCol)] for j in
                                                             range(self.game.numButtonRow)]



                    for i in range(len(self.game.ToggleButton)):
                        for j in range(len(self.game.ToggleButton[0])):
                            self.states[j][i] = self.game.ToggleButton[i][j].toggleState


                    beat_in_milli = 60.0 / self.bpm * 1000 /4

                    blankBeat =  AudioSegment.silent(duration=beat_in_milli)



                    sounds = [0] * len(self.states)
                    for i in range (len(self.states)):

                        sounds[i] = AudioSegment.from_wav(self.soundNames[i])
                        if len(sounds[i])>beat_in_milli:
                            sounds[i]= sounds[i][:beat_in_milli]
                        else:
                            blanktime = beat_in_milli - len(sounds[i])
                            blank = AudioSegment.silent(duration=blanktime)
                            sounds[i] += blank


                        newsound =0
                        for j in range(len(self.states[0])):
                            if self.states[i][j] == 0:
                                newsound += blankBeat
                            else:
                                newsound += sounds[i]

                        sounds[i] = newsound

                    for i in range(1,len(sounds)):
                        sounds[0] = sounds[0].overlay(sounds[i],position=0)

                    playFile= 'Sounds/kit1/loop5.wav'
                    pygame.mixer.music.pause()
                    ##ghetto way of loading a new sound so pydub can't overwrite on the file that is loaded.
                    pygame.mixer.music.load(self.soundNames[0])

                    sounds[0].export('Sounds/kit1/loop5.wav', format="wav")

                    #print("--- %s seconds ---" % (time.time() - start_time))
                    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sounds/kit1/loop.wav'))

                    pygame.mixer.music.load(playFile)
                    pygame.mixer.music.play(-1)


                else:
                    pygame.mixer.music.pause()

