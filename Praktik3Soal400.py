#Sebuah program meminta pengguna memasukkan ketiga panjang sisi suatu segitiga (berarti pengguna memasukkan tiga bilangan).
#Jika ketiga sisi segitiga tersebut semuanya sama, tampilkan pesan:"3 sisi sama". Jika hanya ada dua sisi yang sama panjang,
#tampilkan pesan "2 sisi sama". Jika tidak ada yang sama maka tampilkan pesan: "Tidak ada yang sama".
#Lengkapi program tersebut dengan penanganan kesalahan jika pengguna memasukkan input yang tidak valid.

a1 = (input("Masukkan sisi 1 = "))
b2 = (input("Masukkan sisi 2 = "))
c3 = (input("Masukkan sisi 3 = "))
try:
    A = int(a1)
    B = int(b2)
    C = int(c3)
    if A == B == C:
        print("KETIGA SISI SAMA")
    elif A == B or A == C or B == C:
        print("KEDUA SISI SAMA")
    else:
        print("GAK ADA YANG SAMA")
except ValueError:
    print("BUKAN ANGKA YANG KAMU INPUT!")
