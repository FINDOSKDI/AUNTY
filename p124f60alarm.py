#we assume that no single RR interval will last more than 1 minute
from wfdb import *
import numpy as np
from fuzzy import *
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

branchGoC = fuzzyinterval(69, 60, 12)(77) # 77 years
bpm = minute[0]
GoC1 = Hama(branchGoC, max([fuzzyleq(60.4, 9.6)(bpm),fuzzygeq(79.6, 9.6)(bpm)]))

#60.4, 79.6, 9.6
rr = [int((ann[j]-ann[j-1])*1000) for j in range(bpm)]
GoC2 = max([max([fuzzygeq(931,74)(u) for u in rr]),
            max([fuzzyleq(783,74)(u) for u in rr])])
    #783, 931, 74
print('{:.2f}'.format(Hama(GoC1,GoC2)))

for i in range(1,lastminute):
    bpm = minute[i]-minute[i-1]
    GoC1 = Hama(branchGoC, max([fuzzyleq(60.4, 9.6)(bpm),fuzzygeq(79.6, 9.6)(bpm)]))
    #60.4, 79.6, 9.6
    rr = [int((ann[minute[i-1]+j] - ann[minute[i-1]+j-1] )*1000) for
             j in range(bpm)]
    GoC2 = max([max([fuzzygeq(931,74)(u) for u in rr]),
                max([fuzzyleq(783,74)(u) for u in rr])])
    #783, 931, 74
    print('{:.2f}'.format(Hama(GoC1,GoC2)))



