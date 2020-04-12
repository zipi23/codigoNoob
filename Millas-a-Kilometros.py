print ("1 milla = 1609.344 metros.")
print ("1 galón = 3.785411784 litros.")

litros = float(input("cuantos litros consume tu coche a los 100: "))
millas = float(input("cuantas millas recorre tu coche por galon: "))

def l100kmtompg(litros):
    millas = 100 * 1000 / 1609.344
    galones = litros / 3.785411784
    return millas/galones


def mpgtol100km(millas):
    cienkm = millas * 1609.344 / 1000 / 100
    litros = 3.785411784
    return litros / cienkm

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

print(l100kmtompg(litros))
print(mpgtol100km(millas))
