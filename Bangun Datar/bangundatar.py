import math

def l_persegi(sisi) :
    luas = sisi * sisi
    keliling = sisi + sisi + sisi + sisi
    print(f"Luas Persegi : {sisi} x {sisi} = {luas}")
    print(f"Kelilig Persegi : {keliling}")

def l_persegi_panjang(panjang, lebar) :
    luas = panjang * lebar
    keliling = (2 * panjang) + (2 * lebar)
    print(f"Luas Persegi Panjang : {panjang} x {lebar} = {luas}")
    print(f"Kelilig Persegi Panjang : 2 * ({panjang} + {lebar}) = {keliling}")

def l_segita(alas, tinggi) :
    luas = 0.5 * alas * tinggi
    print(f"Luas Segitiga : 1/2 x {alas} x {tinggi} = {luas}")

def l_lingkaran(jari) :
    luas = 3.14 * jari * jari
    print(f"Luas Lingkaran : 3,14 x {jari} x {jari} = {luas}")

def l_jajar_genjang(alas, tinggi) :
    luas = alas * tinggi
    print(f"Luas Jajar Genjang : {alas} x {tinggi} = {luas}")

def l_trapesium(sisiA, sisiB, tinggi) :
    luas = 1/2 * (sisiA + sisiB) * tinggi
    print(f" luas Trapesium : 1/2 x ({sisiA} + {sisiB}) * {tinggi}= {luas}")

def l_belah_ketupat(D1, D2) :
    luas = 0.5 * D1 * D2
    print(f"Luas Belah Ketupat : 1/2 x {D1} x {D2} = {luas}")

def l_layang_layang(D1, D2) :
    luas = 0.5 * D1 * D2
    print(f"Luas Layang-Layang : 1/2 x {D1} x {D2} = {luas}")

