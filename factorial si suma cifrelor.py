import math

valoare = input ("Dati valoare numarului pentru care facem calculul: ")
nr = valoare

factorial = 1

while nr>0:
    factorial=factorial * nr
    nr = nr - 1
print " "

print " Valoarea lui " + repr(valoare) + "! este " + repr(factorial)

print " "

Suma = 0

while factorial>0:
    Suma = Suma + (factorial%10)
    factorial = factorial/10
print " Valoarea sumei cifrelor este " + repr(Suma)
print " "

raw_input ("Press <ENTER> to exit.    by adipetrasca@yahoo.com")
