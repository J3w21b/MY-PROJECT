sayilar=[]
for i in range(5):
    sayi=int(input(f"{i+1}.sayıyı gir ağam:"))
    sayilar.append(sayi)

sayilar.sort()
print("Sıralı sayılar:",sayilar)

print("En küçük sayı:",sayilar[0])
print("En büyük sayı:", sayilar[-1])

ters_liste=list(reversed(sayilar))
print("Tersden sıralanmış hali:",ters_liste)
