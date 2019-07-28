from pydub.generators import Sine
from pydub.generators import Square
from pydub.generators import Sawtooth

from pydub import AudioSegment


filename2 = 'Test.wav'

majorScale = [2,2,1,2,2,2,1,1]
minorScale = [2,1,2,2,1,3,1,1]
bluesScale = [3,2,1,1,3,2,2]


def getScales():
    scales = dict()
    scales["Major"] = [2,2,1,2,2,2,1,1]
    scales["Minor"] = [2,1,2,2,1,2,2,1]
    scales["Blues"] = [3,2,1,1,3,2,2]
    scales["Penatonic"] = [2,2,3,2,3,3]
    return scales


def getFreqs():
    notedict = dict()
    noteLetters = ['C','C#','D','D#','E','F','F#','G', 'G#','A','A#','B']
    #C0 to C8
    for i in range(-48,60):
        notedict[str(noteLetters[(i+48) % len(noteLetters)] + str( (i + 48 )/len(noteLetters)))] = 440 * 2 **((i - 9.)/12)
    return notedict

def getSillence(beat, bpm = 60):
    length = (60. / bpm) * 1000. / 4 * beat * 16

    return AudioSegment.silent(duration=length )

def getSinSound(freq,beat, bpm = 60):



    beat_in_mili = (60. / bpm) * 1000. /4 * beat*16



    sin = Sine(freq)
    sound = sin.to_audio_segment(beat_in_mili)
    sound = sound.fade_in(int(beat_in_mili*.05))
    sound = sound.fade_out(int(beat_in_mili*.05))
    return sound

def getSquareSound(freq,beat,subdivison, bpm=60):
    beat_in_mili = (60. / bpm) * 1000. /subdivison * beat
    square = Square(freq)
    sound = square.to_audio_segment(beat_in_mili)
    sound = sound.fade_in(int(beat_in_mili*.05))
    sound = sound.fade_out(int(beat_in_mili*.05))
    return sound

def getSawSound(freq,beat,subdivison, bpm=60):
    beat_in_mili = (60. / bpm) * 1000. /subdivison *beat
    saw = Sawtooth(freq)
    sound = saw.to_audio_segment(beat_in_mili)
    sound = sound.fade_in(int(beat_in_mili*.05))
    sound = sound.fade_out(int(beat_in_mili*.05))
    return sound



def makeMajorScale(root):

    if len(root) == 1:
        root = root + str(4)

    noteLetters = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    base=0
    for i in range(len(notes)):
        if notes[i][0] == str(root[0]):
            if len(root) == 2 and len(notes[i]) ==1:
                break
            elif len(root) ==3 and len(notes[i]) == 2:
                break

        base +=1
    octave = int(root[-1])
    if octave >6:
        octave=6

    originalOctave =octave

    res =0
    step =0
    scaleWord = [0] * (len(majorScale))
    #scaleWord[0] = root
    for i in range(len(majorScale)):
        #res += Sine(scale[(step + base) % len(noteLetters)])
        scaleWord[i] = str(noteLetters[(step + base ) % len(noteLetters)] + str(octave))
        if noteLetters[(step + base ) % len(noteLetters)][0] == 'B':

            if (octave-originalOctave)==0:
                octave +=1

        elif noteLetters[(step + base ) % len(noteLetters)] == 'A#':
            if i <len(majorScale)-2:
                octave +=1


        step += majorScale[i]

    reversescaleWord = scaleWord[::-1]
    del reversescaleWord[0]

    scaleWord = scaleWord + reversescaleWord


    print scaleWord

    """
    for i in scaleWord:
        if i[0] == root[0] and len(i) == len(root):
            res +=getSinSound(scale[i],2)
        else:
            res += getSinSound(scale[i], 4)

    return res
    
    """

def makeBluesScale(root):

    if len(root) == 1:
        root = root + str(4)

    noteLetters = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    base=0
    for i in range(len(notes)):
        if notes[i][0] == str(root[0]):
            if len(root) == 2 and len(notes[i]) ==1:
                break
            elif len(root) ==3 and len(notes[i]) == 2:
                break

        base +=1
    octave = int(root[-1])
    if octave >6:
        octave=6

    originalOctave =octave

    res =0
    step =0
    scaleWord = [0] * (len(bluesScale))
    #scaleWord[0] = root
    for i in range(len(bluesScale)):
        #res += Sine(scale[(step + base) % len(noteLetters)])
        scaleWord[i] = str(noteLetters[(step + base ) % len(noteLetters)] + str(octave))
        if noteLetters[(step + base ) % len(noteLetters)][0] == 'B':

            if (octave-originalOctave)==0:
                octave +=1

        elif noteLetters[(step + base ) % len(noteLetters)] == 'A#':
            if i <len(bluesScale)-2:
                octave +=1


        step += bluesScale[i]




    print scaleWord
    for i in scaleWord:
        if i[0] == root[0] and len(i) == len(root):
            res +=getSinSound(scale[i],2)
        else:
            res += getSinSound(scale[i], 4)

    return res

noteLetters = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def makeScale(root,scale):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    base = 0
    for i in range(len(notes)):
        if notes[i] == root:
                break
        base += 1

    step = 0
    scale_word = [0] * (len(scale))
    for i in range(len(scale)):
        scale_word[i] = str(notes[(step + base) % len(notes)])

        step += scale[i]

    return scale_word



