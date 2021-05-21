# nama file : import.py
# mengimport modul geometri2D

from matematika import geometri2D

# persegi panjang
p = 10
l = 8

luas = geometri2D.luaspersegipanjang(p, l)
kel = geometri2D.kelilingpersegipanjang(p, l)

print("PERSEGI PANJANG")
print("panjang\t: ", p)
print("lebar\t: ", l)
print("luas\t: ", luas)
print("keliling\t: ", kel)

# lingkaran
jarijari = 3
luas = geometri2D.luaslingkaran(3)
kel = geometri2D.kelilinglingkaran(3)

print("\nLINGKARAN")
print("jari-jari\t: ", jarijari)
print("luas\t: ", luas)
print("keliling\t: ", kel)