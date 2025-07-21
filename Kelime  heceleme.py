sesliler="aeıioöuü"

def hecele(kelime):
    heceler=[]
    hece=""
    for harf in kelime:
        hece+=harf
        if harf in sesliler:
            heceler.append(hece)
            hece=""

    if hece:
        heceler.append(hece)
    return heceler

kelime=input("Bir kelime giriniz:")
heceler=hecele(kelime)
print("Heceler:",heceler)