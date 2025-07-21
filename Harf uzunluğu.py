cumle=input("Bir cümle gir ağam: ")
cumle=cumle.lower()

import string
for noktalama in string.punctuation:
    cumle=cumle.replace(noktalama,"")

kelimeler=cumle.split()

print("Toplam kelime uzunluğu:",len(kelimeler))

for kelime in kelimeler:
    print(f"'{kelime}' kelimesi {len(kelime)} harfli.")

bes_harfli=[k for k in kelimeler if len(k)==5]
print("5 harfli kelimeler:",bes_harfli)

a_ile_baslıyanlar=[k for k in kelimeler if k.startswith("a")]
print("A ile başlayan kelimeler:",a_ile_baslıyanlar)

en_uzun=max(kelimeler,key=len)
print("En uzun kelime",en_uzun)

print("Kelimelerin tersi:")
for kelime in kelimeler:
    print(kelime[::-1])

l_ile_baslayanlar=[k for k in kelimeler if k.startswith("l")]
print("L ile başlayanlar:",l_ile_baslayanlar)