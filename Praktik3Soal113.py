#contoh 3.3
a = input("Masukkan bilangan pertama = ")
b = input("Masukkan bilangan kedua = ")
c = input("Masukkan bilangan ketiga = ")
try:
    bilangan_a = int(a)
    bilangan_b = int(b)
    bilangan_c = int(c)
    if a > b and a > c:
        print("Terbesar = " , a)
    elif b > a and b > c:
        print("Terbesar = " , b)
    elif c > a and c > b:
        print("Terbesar = " , c)
    elif a == b and b == a and a == c:
        print("Sama Semua")
except ValueError:
    print("KAMU MENGETIK HURUF!")