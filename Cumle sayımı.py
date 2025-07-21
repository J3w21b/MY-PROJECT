cumle=input("Bir cümle gir:")
cumle=cumle.lower()

harf_sayilar={}

for harf in cumle:
    if harf!=" ":
        if harf in harf_sayilar:
            harf_sayilar[harf] +=1

        else:
            harf_sayilar[harf] =1

print("Harf sayıları:")
for harf,adet in harf_sayilar.items():
    print(f"{harf}: {adet}")