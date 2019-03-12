#we assume that no single RR interval will last more than 1 minute
from wfdb import *
import numpy as np
ann = np.concatenate((rdann('124','atr',pb_dir='mitdb').sample/360, [0]))
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


print("""?checkGender(1), 1; ?checkAge(77), 0.33; !ageRange60(), 0.33;
""", end='')
print("""?minute(1), 0.33; ?readBPM({}), 0.33;
""".format(minute[0]), end='')
print("?readRR(277), 0;")

