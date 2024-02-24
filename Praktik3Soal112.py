#contoh 3.2 Positif atau Negatif?
bilangankali = input("Masukkan Bilangan Bulat: ")
try:
    bilangan = int(bilangankali)
    if bilangan > 0:
        print("BILANGAN POSITIF")
    elif bilangan <0:
        print("BILANGAN NEGATIF")
    elif bilangan == 0:
        print("ZERO")
except:
    print("KAMU NGETIK ANGKA BUKAN HURUF/SIMBOL!")