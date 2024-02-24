#Implementasikan percabangan pada Contoh 3.2 (Positif-Negatif) menggunakan ternary operator.
bilangankali = input("Masukkan Bilangan Bulat: ")
try:
    bilangan = int(bilangankali)
    print("BILANGAN POSITIF" if bilangan > 0 else ("BILANGAN NEGATIF" if bilangan < 0 else "ZERO"))
except ValueError:
    print("KAMU NGETIK ANGKA BUKAN HURUF/SIMBOL!")