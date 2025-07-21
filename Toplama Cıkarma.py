while True:
 print("Ağam Hesap Makinesine Hoş Geldin")
 print("1 - Toplama")
 print("2 - Çıkarma")
 print("3 - Çarpma")
 print("4 - Bölme")

 secim = input("Ne yapmak istersin ağam (1-4): ")

 sayi1 = float(input("Birinci sayıyı gir: "))
 sayi2 = float(input("İkinci sayıyı gir: "))

 if secim == "1":
     print("Sonuç:", sayi1 + sayi2)
 elif secim == "2":
     print("Sonuç:", sayi1 - sayi2)
 elif secim == "3":
     print("Sonuç:", sayi1 * sayi2)
 elif secim == "4":
     if sayi2 != 0:
         print("Sonuç:", sayi1 / sayi2)
     else:
         print("Sıfıra bölünmez ağam.")
 else:
     print("Yanlış seçim yaptın ağam.")


 devam = input("Devam etmek istermisiniz beyim ? (e/h): ")
 if devam.lower() !="e":
     print("Allaha emanat ortak.")
     break