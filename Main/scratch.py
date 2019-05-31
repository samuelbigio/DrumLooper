import scipy
from pydub import AudioSegment

sound1 = AudioSegment.from_wav('Sounds/kit1/crash.wav')


last_mil = sound1[:1000]


for i in xrange(1000):
    last_mil +=last_mil


last_mil.export('Sounds/kit1/blank.wav', format = "wav")







