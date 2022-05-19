import time
Numero = int(input("Indicare numero "))
N = True
for i in range(2, Numero):
    if (Numero % i) == 0:
        primo = False
for i in range(2, Numero):
    if (Numero % i) > 0:
        b = True
        a = False

if N: 
 print (Numero," è un numero primo")
else:
 print (Numero," non è un numero primo")

time.sleep(10)

