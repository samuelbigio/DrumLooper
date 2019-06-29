import os


"""
for filename in os.listdir('Sounds'):
    print filename

self.game.soundNames = ['kick', 'snare', 'hhcl', 'hhop', 'ride', 'crash', 'rim', 'shaker']
for i in range(len(self.game.soundNames)):
    self.game.soundNames[i] = 'Sounds/kit1/' + self.game.soundNames[i] + '.wav'

"""


def GetSoundNames(dir):
    soundnames = []
    dir = 'Sounds'
    count = 0
    for filename in os.listdir(dir):
        soundnames.append([])
        for j in os.listdir(dir + '/' + filename):
            soundnames[count].append(dir + '/' + filename + '/' + j)
        count += 1
    return soundnames