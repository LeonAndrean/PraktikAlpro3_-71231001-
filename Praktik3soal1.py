#Contoh 3.1 Demam atau tidak?
suhubadan = input("Suhu Badan Kamu Sekarang: ")
try:
    suhu = int(suhubadan)
    if suhu >= 32 and suhu <= 37:
        print("KAMU SEHAT :)")
    elif suhu >= 38 and suhu <= 45:
        print("KAMU DEMAM :(")
except ValueError:
    print("KAMU SALAH KETIK!")