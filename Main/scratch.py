import scipy
from pydub import AudioSegment
import time


sound1 = AudioSegment.from_wav('Sounds/kit1/blank.wav')

start_time = time.time()
#last_mil = sound1[-10:]



#last_mil.export('Sounds/kit1/blank.wav', format = "wav")



#for i in range(10):
 #   sound1 +=sound1

sound1.export('Sounds/kit1/blank2.wav', format = "wav")



print("--- %s seconds ---" % (time.time() - start_time))

