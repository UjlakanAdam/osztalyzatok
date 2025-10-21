def feladat1(szamok):
    cv=0
    osszeg=0
    while(cv<len(szamok)):
        osszeg+=szamok[cv]
        cv+=1
    print(f"Jegyek átlaga: {osszeg/len(szamok)}")

def feladat2(szamok):
    cv=0
    otos=0
    while(cv<len(szamok)):
        lista=szamok[cv]
        if lista==5:
            otos+=1
        cv+=1
    print(f"Ötösök száma: {otos}")

def feladat3(szamok):
    cv=0
    egyes=0
    while(cv<len(szamok)):
        lista=szamok[cv]
        if lista==1:
            egyes+=1
        cv+=1
    print(f"Elégtelenek száma: {egyes}")

def feladat4(szamok):
    cv=0
    diak=0
    while diak!=1:
        (cv<len(szamok))
        lista=szamok[cv]
        if lista==1:
            diak+=1
        cv+=1
    print(f"Ez a diák kapott elégtelent: {cv}")


    

    
