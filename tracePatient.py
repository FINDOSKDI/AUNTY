#we assume that no single RR interval will last more than 1 minute
from wfdb import *
import numpy as np
ann = np.concatenate((rdann('108','atr',pb_dir='mitdb').sample/360, [0]))
samp = rdsamp('108',pb_dir='mitdb')
age = int(samp[1]['comments'][0][0:2])
minute = [0]*30
lastminute = 0
for i in range(len(ann)):
    if ann[i] > (lastminute+1)*60:
        minute[lastminute] = i
        lastminute += 1
assert lastminute == 30
# minute_{i-1} ends up having the index of the first beat of minute i+1
# minute_0 is the number of beats of minute 1
# minute_i - minute_{i-1} is the number of beats of minute i+1
# the beats of minute 1 are ann[:minute[0]]
# the beats of minute i are ann[minute[i-2]:minute[i-1]]
print("""?checkGender(1),?checkAge({}),!recordAgeRange60to69(),
""".format(age), end='')
print("""?minute({}), ?readBPM({}),
""".format(1,minute[0]), end='')
for j in range(minute[0]):
    print("?readRR({:d}),".format(int((ann[j]-ann[j-1])*1000)),
          end='' if (j+1)%4 else '\n')
if (minute[0])%4:
    print('')
print('?noMorePendingRR(),')
print("!ok(),") # EXPECTED RESULT    
for i in range(1,lastminute):
    print("""?minute({}), ?readBPM({}),
""".format(i+1,minute[i]-minute[i-1] ), end= '')
    for j in range(minute[i]-minute[i-1]):
        print("?readRR({}),".format(int((
            ann[minute[i-1]+j] - ann[minute[i-1]+j-1] )*1000)
        ), end='' if (j+1)%4 else '\n')
    if (minute[i]-minute[i-1])%4:
        print('')
    print('?noMorePendingRR(),')
    print("!ok(),") # EXPECTED RESULT    
print('?minute({}),?endOfRecord()'.format(lastminute+1))
