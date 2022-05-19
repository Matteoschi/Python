import time
Numero = int(input("Indicare numero "))
primo = True
for i in range(2, Numero):
    if (Numero % i) == 0:
        primo = False


if primo: 
 print (Numero," è un numero primo")
else:
 print (Numero," non è un numero primo")

time.sleep(10)
