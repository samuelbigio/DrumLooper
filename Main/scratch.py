import scipy
from pydub import AudioSegment
import time


sound1 = AudioSegment.from_wav('Sounds/kit1/blank.wav')
kick = sound1 = AudioSegment.from_wav('Sounds/kit1/kick.wav')
print len(kick)


exit()
start_time = time.time()

#for i in range(3):
 #   sound1 +=sound1

#sound1.export('Sounds/kit1/blank2.wav', format = "wav")



print("--- %s seconds ---" % (time.time() - start_time))

