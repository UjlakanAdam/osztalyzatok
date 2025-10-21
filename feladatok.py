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
    

    
