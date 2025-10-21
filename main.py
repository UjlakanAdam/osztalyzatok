#[5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3,]
import feladatok
import feladatok2

lista = [5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3]


osszeg, szamok=feladatok.feladat1(lista)
print(f"Jegyek átlaga: {osszeg/len(szamok)}")

otos=feladatok.feladat2(lista)
print(f"Ötösök száma: {otos}")

egyes=feladatok.feladat3(lista)
print(f"Elégtelenek száma: {egyes}")

cv=feladatok.feladat4(lista)
print(f"Ez a diák kapott elégtelent: {cv}")

asd = feladatok2.feladat51(lista)
feladatok.feladat5(asd)

dsa = feladatok2.fel6(lista)
print(dsa)