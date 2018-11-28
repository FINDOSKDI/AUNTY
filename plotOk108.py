from generateVectorsNobranch import *
from fuzzy import *
import matplotlib.pyplot as plt

agerel = {}
agerel[90] = fuzzygeq(90, 0.2*90)
agerel[80] = fuzzyinterval(89, 80, 0.2*80)
agerel[70] = fuzzyinterval(79, 70, 0.2*70)
agerel[60] = fuzzyinterval(69, 60, 0.2*60)

b70 = agerel[70](87)
b80 = agerel[80](87)
b90 = agerel[90](87)
ok70 = genOk(108, 70)
ok80 = genOk(108, 80)
ok90 = genOk(108, 90)

i = [i for i in range(31)]
p70 = [b70]
p80 = [b80]
p90 = [b90]
for ii in i[1:]:
    p70 = p70 + [Hama(p70[ii-1], ok70[ii-1])]
    p80 = p80 + [Hama(p80[ii-1], ok80[ii-1])]
    p90 = p90 + [Hama(p90[ii-1], ok90[ii-1])]

ax = plt.axes()
ax.plot(i, p70, '-', label='70-79')
#ax.legend(['70-79'])
ax.plot(i, p80, '--', label='80-89')
#ax.legend(['80-89'])
ax.plot(i, p90, '-.', label='>90')
#ax.legend(['>90'])
ax.legend()
plt.grid(True)
plt.xticks(i)
plt.show()
