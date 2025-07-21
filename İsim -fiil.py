isimler=["kebap","ayran","çakır"]
fiiler=["git","gel","naber"]

isim=input("Bir kelime giriniz:")

if isim in  isimler:
    print("Bu bir isim.")
if isim in fiiler:
    print("Bu bir fiil.")
else:
    print("Böyle bir değer tanımlanmadı.")