#soal 3 case 1 & 2

x=int(input("Masukkan alas atap : "))
y=int(input("Masukkan tinggi atap : "))
z=int(input("Masukkan tinggi tembok : "))

segitiga = 0.5 * (x * y)
persegi = z * z

print(float(segitiga + persegi) / 5)