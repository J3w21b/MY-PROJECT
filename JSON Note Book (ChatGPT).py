import json

def kayit_ekle():
    
    try:
        with open("kayitlar.json","r",encoding="utf-8") as dosya:
            kayitlar = json.load(dosya)
    except FileNotFoundError:
        kayitlar = []

    isim=input("İsim giriniz:")
    yas = int(input("Yaşınızı giriniz:"))

    kayitlar.append({"isim":isim, "yas": yas})

    with open("kayitlar.json","w",encoding="utf-8") as dosya:
        json.dump(kayitlar,dosya,ensure_ascii=False,indent=4)
    print("Kayıt eklendi.")

def kayitlari_goster():
    try:
        with open("kayitlar.json","r",encoding="utf-8") as dosya:
            kayitlar = json.load(dosya)
            if not kayitlar:
                print("Hiç kayıt yok.")
            else:
                print("===Kayıtlar===")
                for k in kayitlar:
                    print(f"isim: {k['isim']}, Yaş: {k['yas']}")

    except FileNotFoundError:
        print("Kayit dosyası bulunamadı.")

while True:
    print("\n1-Kayıt Ekle")
    print("2-Kayıtları Göster")
    print("3-Çıkış")
    secim=input("Seçim yapınız:")

    if secim =="1":
        kayit_ekle()
    elif secim =="2":
        kayitlari_goster()
    elif secim =="3":
        print("Görüşürüz!")
        break

    else:
        print("Yanlış seçim yaptınız.")