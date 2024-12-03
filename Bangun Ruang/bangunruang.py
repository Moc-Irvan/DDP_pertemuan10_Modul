import math

def kubus(sisi):
    volume = sisi * sisi * sisi
    luas = 6 * (sisi ** 2)
    print(f"volume Kubus : {sisi} x {sisi} x {sisi} = {volume}")    
    print(f"Luas Kubus : 6 x ({sisi} x {sisi}) = {luas}")

def balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print(f"volume Balok : {panjang} * {lebar} * {tinggi} = {volume} ")    
    print(f"Luas Balok : 2 x (({panjang} x {lebar}) + ({panjang} x {tinggi}) + ({lebar} x {tinggi})) = {luas}")

def tabung(jari, tinggi):
    volume = 3.14 * (jari**2) * tinggi
    luas = 2 * 3.14 * jari * (jari + tinggi)
    print(f"volmue Tabung : 3.14 x {jari}^2 x {tinggi} = {volume}")    
    print(f"Luas Tabung : 2 x 3.14 x {jari} x ({jari} + {tinggi}) = {luas}")

def kerucut(jari, tinggi):
    volume = 1/3 * 3.14 * (jari**2) * tinggi
    luas = (3.14 * jari**2) + (3.14 * jari * tinggi)
    print(f"Volume Kerucut : 1/3 x 3.14 x {jari}^2 x {tinggi} = {volume}")
    print(f"Luas Kerucut : (3.14 x {jari}^2) + (3.14 x {jari} x {tinggi}) = {luas}")

def bola(jari):
    volume = 4/3 * 3.14 * (jari**3)
    luas = 4 * 3.14 * (jari ** 2)
    print(f"Volume Bola : 4/3 x 3.14 x {jari}^3 = {volume}")
    print(f"Luas Bola : 4 x 3.14 x ({jari} x {jari}) = {luas}")

def limas (sisi, tinggi, luassisitegak):
    volume = 1/3 * (sisi * sisi) * tinggi
    luas = (sisi * sisi) + (4 * luassisitegak)
    print(f"Volume Limas Segi Empat : 1/3 x ({sisi} x {sisi}) x {tinggi} = {volume}")
    print(f"Luas Limas Segi Empat : ({sisi} x {sisi}) + (4 x {luassisitegak}) = {luas}")

def prisma (alas, tinggi, luasalas):
    volume = (1/2 * alas * tinggi) * tinggi
    luas = (2 * alas) + (luasalas * tinggi)
    print(f"Volume Prisma Segi Tiga : (1/2 x {alas} x {tinggi}) x {tinggi} = {volume}")
    print(f"Luas Prisma Segi Tiga : (2 x {alas}) + ({luasalas} x {tinggi}) = {luas}")