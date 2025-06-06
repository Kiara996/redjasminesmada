print("Gento group \nJL.Aung Timur No.14 Mojosongo")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("Nomor Nota: S/230507/1/151")
print("Makan di tempat")
Pelanggan=float(input('Pelanggan:'))
Waitrees=str(input("Waitrees:"))
Kasir=str(input('kasir:'))
print("perangkat ke-1")
import datetime
x= datetime.datetime.now()
print(x)

cocacola=12000
sprite=11000
fanta=10000
marjan=15000
natadecoco= 14500

print("\ncocacola")
a=3*cocacola
print(a)
print("\nsprite")
b=2*sprite
print(b)

print("\nmarjan")
c=1*marjan
print(c)
print("\nfanta")
d=2*fanta
print(d)

print("\n")

total= (a+b+c+d)
total_str= str(total)
print("total",total)

bayar=int(input("bayar tunai:"))
kembali=total-bayar
kembali_str=str(kembali)
print("kembali:" +kembali_str)
print("-------------------------------")
print("          Terima Kasih         ")
print("-------------------------------")