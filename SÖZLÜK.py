sozluk= {
    "elma":"Bu bir meyve.",
    "git":"Ordan HEMEN UZAKLAŞ",
    "MEMATİ BAŞ":"G.Ö"
}

arama=input("Bir kelime arayınız:")
if arama in sozluk:
    print(f"{arama}:{sozluk[arama]}")
else:
    print("Hadi lan köyüne")