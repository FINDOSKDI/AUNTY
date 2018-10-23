def fuzzyleq(y,delta):
    return lambda x: 1 if x <= y else \
	0 if x > y + delta else \
	1 - (x - y) / delta

def fuzzyor(lam1, lam2):
    return lambda x: max([lam1(x), lam2(x)])

def fuzzyand(lam1, lam2):
    return lambda x: min([lam1(x), lam2(x)])

def fuzzynot(lam1):
    return lambda x: 1 - lam1(x)
def fuzzyeq(x,y,delta):
    return min([fuzzyleq(y,delta)(x), fuzzyleq(x,delta)(y)])
def fuzzygeq(z,delta):
    return fuzzynot(fuzzyleq(z-delta,delta))

def fuzzyinterval(y,z,delta):
    return fuzzyand(fuzzyleq(y,delta),fuzzygeq(z,delta))

def Hama(a,b):                  #           FALTAN LAS OTRAS TNORMAS
    return (a*b)/(a+b-a*b)
