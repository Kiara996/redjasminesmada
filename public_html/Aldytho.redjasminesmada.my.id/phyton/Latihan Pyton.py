nilai=int(input('Nilai:'))
if nilai >= 90 and nilai <= 100:
    print("A")
elif nilai >= 80 and nilai <= 89:
    print("B")
elif nilai >= 70 and nilai <= 79:
    print("C")
elif nilai >=0 and nilai <=69:
    print("E")
else:
    print("Kesalahan memasukkan nilai !")