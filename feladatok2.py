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

        print(f"Diák {i+1} : {diak}")

        i += 1

    return diak

def feladat51(szamok):
    cv=0

    egyes=0

    ketes=0

    harmas=0

    neyges=0

    otot=0

    while cv<len(szamok):

        lista=szamok[cv]

        if lista==1:
            egyes+=1

        elif lista == 2:
            ketes += 1

        elif lista == 3:
            harmas += 1

        elif lista == 4:
            neyges += 1

        else:
            otot +=1

        cv+=1

    listi = []
    listi.append(egyes)
    listi.append(ketes)
    listi.append(harmas)
    listi.append(neyges)
    listi.append(otot)
    return listi