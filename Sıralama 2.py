sinif=[]

for i in range(3):
    isim=input(f"{i+1}. Öğrencinin ismini giriniz:")
    notu=input(f"{isim} için geçerli olan notu girin efendim: ")
    sinif.append([isim,notu])

print("\n----SINIF LİSTESİ----")
for ogrenci in sinif:
    print(f"{ogrenci[0]} - {ogrenci[1]} puan")

en_iyi=sinif[0]
for ogrenci in sinif:
    if ogrenci[1] > en_iyi[1]:
        en_iyi=ogrenci

print(f"\nEn yüksek not alan: {en_iyi[0]} - {en_iyi[1]} puan")