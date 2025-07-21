ekler =["lar","ler","bey","cano","mi"]

def kok_bul(kelime):
    for ek in ekler:
        if kelime.endswith(ek):
            return kelime[:-len(ek)]
    return kelime

kelime=input("Bir kelime giriniz:")
kok=kok_bul(kelime)
print("Kelime Kökü:",kok)
