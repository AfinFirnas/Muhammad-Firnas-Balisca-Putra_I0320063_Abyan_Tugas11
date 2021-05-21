# Nama file : paket.py
# Mengimpor modul geometri2D
# Yang berada di dalam paket matematika
import matematika.geometri2D

def main():
    #bujur sangkar
    sisi = 5

    luas = matematika.geometri2D.luasbujursangkar(5)

    print("BUJUR SANGKAR")
    print("panjang sisi\t: ", sisi)
    print("luas\t\t: ", luas)

if __name__== "__main__":
    main()