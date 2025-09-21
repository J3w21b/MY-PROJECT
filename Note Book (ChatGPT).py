def not_ekle():
    with open("notlar.txt","a", encoding="utf-8") as dosya:
        not_= input("Notunuzu Giriniz: ")
        dosya.write(not_ +"\n")
    print("Not kaydedildi.")

def notlari_goster():
    try:
        with open("notlar.txt","r",encoding="utf-8") as dosya:
            icerik=dosya.readlines()
            if not icerik:
                print("Henüz not yok.")
            else:
                print("===Kaydedilen Notlar===")
                for satir in icerik:
                    print("-",satir.strip())

    except FileNotFoundError:
        print("Henüz not dosyası oluşturulmamış.")

while True:
    print("\n1-Not Ekle")
    print("2-Notları Göster")
    print("3-Çıkış")
    secim=input("Seçimin nedir?: ")

    if secim == "1":
        not_ekle()
    elif secim =="2":
        notlari_goster()
    elif secim=="3":
        print("Görüşürüz.")
        break
    else:
        print("Yanlış seçim yaptınız.")