import random
def fel7():
    
    lo = []
    i = 0

    while i < 17:

        z = random.randint(1, 6)

        if z == 6:
            sz = 5

        else:
            sz = z

        lo.append(sz)

    return lo  