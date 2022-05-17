Numero=int(input("Indicare numero"))

for i in range(2, Numero):
    if (Numero % i) == 0:
        Riv = True
    else:
        Riv = False

if Riv:
    print(Numero, "Non è primo")
else:
    print(Numero, "E primo")
