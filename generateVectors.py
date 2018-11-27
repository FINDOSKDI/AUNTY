#we assume that no single RR interval will last more than 1 minute
from wfdb import *
import numpy as np
from fuzzy import *
bpminf = {80: 62.5, 90: 64.4, 60: 60.4, 70: 61.4}
bpmsup = {80: 83.5, 90: 87.6, 60: 79.6, 70: 80.6}
rrinf = {80: 747.9, 90: 715.4, 60: 783.1, 70: 771}
rrsup = {80: 895.9, 90: 863.4, 60: 931.1, 70: 919}

bpmdelta = {80: 10.5, 90: 11.6, 60: 9.6, 70: 9.6}

ages = {124: 77, 108: 87}
agerel = {}
agerel[90] = fuzzygeq(90, 0.2*90)
agerel[80] = fuzzyinterval(89, 80, 0.2*80)
agerel[70] = fuzzyinterval(79, 70, 0.2*70)
agerel[60] = fuzzyinterval(69, 60, 0.2*60)

def genOk(number, agebranch):
    ann = np.concatenate((rdann(str(number),'atr',pb_dir='mitdb').sample/360, [0]))
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

    res = []
    branchGoC = agerel[agebranch](ages[number])
    bpm = minute[0]
    GoC1 = Hama(branchGoC, max([fuzzyleq(bpminf[agebranch], bpmdelta[agebranch])(bpm),fuzzygeq(bpmsup[agebranch], bpmdelta[agebranch])(bpm)]))
    GoC2 = Hama(branchGoC, fuzzyinterval(bpmsup[agebranch], bpminf[agebranch], bpmdelta[agebranch])(bpm))
    #60.4, 79.6, 9.6
    rr = [int((ann[j]-ann[j-1])*1000) for j in range(bpm)]
    for u in rr:
        GoC1 = Hama(GoC1, fuzzyinterval(rrsup[agebranch], rrinf[agebranch], 74)(u))
    #783, 931, 74
    res = res + [max([GoC1,GoC2])]

    for i in range(1,lastminute):
        bpm = minute[i]-minute[i-1]
        GoC1 = Hama(branchGoC, max([fuzzyleq(bpminf[agebranch], bpmdelta[agebranch])(bpm),fuzzygeq(bpmsup[agebranch], bpmdelta[agebranch])(bpm)]))
        GoC2 = Hama(branchGoC, fuzzyinterval(bpmsup[agebranch], bpminf[agebranch], bpmdelta[agebranch])(bpm))
        #60.4, 79.6, 9.6
        rr = [int((ann[minute[i-1]+j] - ann[minute[i-1]+j-1] )*1000) for
        j in range(bpm)]
        for u in rr:
            GoC1 = Hama(GoC1, fuzzyinterval(rrsup[agebranch], rrinf[agebranch], 74)(u))
        #783, 931, 74
        res = res + [max([GoC1,GoC2])]
    return res


def genAlarm(number, agebranch):
    ann = np.concatenate((rdann(str(number),'atr',pb_dir='mitdb').sample/360, [0]))
    minute = [0]*30
    lastminute = 0
    for i in range(len(ann)):
        if ann[i] > (lastminute+1)*60:
            minute[lastminute] = i
            lastminute += 1
    assert lastminute == 30

    res = []
    branchGoC = agerel[agebranch](ages[number])
    bpm = minute[0]
    GoC1 = Hama(branchGoC, max([fuzzyleq(bpminf[agebranch], bpmdelta[agebranch])(bpm),fuzzygeq(bpmsup[agebranch], bpmdelta[agebranch])(bpm)]))

    #60.4, 79.6, 9.6
    rr = [int((ann[j]-ann[j-1])*1000) for j in range(bpm)]
    GoC2 = max([max([fuzzygeq(rrsup[agebranch],74)(u) for u in rr]),
                max([fuzzyleq(rrinf[agebranch],74)(u) for u in rr])])
    #783, 931, 74
    res = res + [Hama(GoC1,GoC2)]

    for i in range(1,lastminute):
        bpm = minute[i]-minute[i-1]
        GoC1 = Hama(branchGoC, max([fuzzyleq(bpminf[agebranch], bpmdelta[agebranch])(bpm),fuzzygeq(bpmsup[agebranch], bpmdelta[agebranch])(bpm)]))
        #60.4, 79.6, 9.6
        rr = [int((ann[minute[i-1]+j] - ann[minute[i-1]+j-1] )*1000) for
             j in range(bpm)]
        GoC2 = max([max([fuzzygeq(rrsup[agebranch],74)(u) for u in rr]),
                max([fuzzyleq(rrinf[agebranch],74)(u) for u in rr])])
        #783, 931, 74
        res = res + [Hama(GoC1,GoC2)]
    return res
