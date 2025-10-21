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

def fel6(templist2):
    i = 0

    while  i < len(templist2):

        diak = templist2[i]

        print(f"Diák {i+1} : diak")

        return diak
