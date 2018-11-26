#we assume that no single RR interval will last more than 1 minute
from wfdb import *
import numpy as np
from fuzzy import *
ann = np.concatenate((rdann('108','atr',pb_dir='mitdb').sample/360, [0]))
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

branchGoC = fuzzyinterval(69, 60, 13)(87) # 87 years
GoC1 = branchGoC # RAMA 60... MAAAAAL
GoC2 = branchGoC
bpm = minute[0]
rr = [int((ann[j]-ann[j-1])*1000) for j in range(bpm)]
#783, 931, 74
print()

for i in range(1,lastminute):
    GoC1 = branchGoC
    GoC2 = branchGoC
    bpm = minute[i]-minute[i-1]
    rr = [int((ann[minute[i-1]+j] - ann[minute[i-1]+j-1] )*1000) for
             j in range(bpm)]
    print("!ok(),") # EXPECTED RESULT    

