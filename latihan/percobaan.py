print('--------gunakan modul-----------')
import myModul
myModul.tambah(5,2)
myModul.kurang(10,3)
myModul.kali(5,6)

print('\n--gunakan modul yg ada dgn alias--')
import myModul as hitung
hitung.bagi(20,2)
hitung.pangkat(2,3)

print('\n--gunakan modul dgn memanggil sebagian fungsinya--')
from myModul import tambah,kurang
tambah(20,30)
kurang(2,3)

print('\n--gunakan modul dgn memanggil seluruh fungsinya--')
from myModul import *
tambah(20,30)
kurang(2,3)
kali(5,6)
bagi(20,2)
pangkat(2,3)
