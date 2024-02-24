#Buatlah sebuah program yang dapat menampilkan jumlah hari dalam suatu bulan di tahun2020.
#Program meminta pengguna memasukkan nomor bulan(1-12),kemudian program akan menampilkan jumlah hari pada bulan tersebut.
# Sebagai contoh, perhatikan input dan output berikutini:
# Masukkanbulan (1-12): 7
# Jumlah hari: 31
# Lengkapi program tersebut dengan penanganan kesalahan jika pengguna memasukkan bulan yang salah.
# Penanganan kesalahan dalam bentuk memunculkan pesan bahwa bulan yang diinputkan oleh pengguna tersebut tidak valid.

nomorbulan = input("Masukkan bulan (dalam angka [1-12]) = ")
try:
    bulan = int(nomorbulan)
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print(f"JUMLAH HARI PADA BULAN KE-{nomorbulan} ADALAH 31 HARI ")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print(f"JUMLAH HARI PADA BULAN KE-{nomorbulan} ADALAH 30 HARI ")
    elif bulan == 2:
        print(f"JUMLAH HARI PADA BULAN KE-{nomorbulan} ADALAH 29 HARI ")
    else:
        print(f"JUMLAH BULAN ADA 12! KAMU MALAH MENGETIK {nomorbulan}!")
except:
    print("EROR KAMU SALAH KETIK EROR")