# using pycipher to decrypt

#install pycipher

from pycipher import Caesar

ctf=Caesar(key=19).decipher('VMY{vtxltkvbiaxkbltlnulmbmnmbhgvbiaxk}')

print(ctf.lower())


#ctfcaesarcipherisasubstitutioncipher
