ask = input("(1) convertire decimale in binario (2) binario in decimale (3) convertire parola :")
if ask =="1":
        a = int(input("numero da convertire :"))
        def ConvertiInBinario(b):
                binString = []

                while b > 0:
                        if b % 2 == 0:
                                binString.append(0)
                        else:
                                binString.append(1)
                        b = int(b / 2)

                binString.reverse()
                return "".join(str(el) for el in binString)
        print(ConvertiInBinario(a))

if ask == "2":
        binario = input("inserire numero da convertire in base 2 ")
        decimale = int( binario , base=2)
        print(decimale,"numero decimale di ",binario)

if ask == "3":
       parola = input("inserisci parola da convertire: ")
       convertito = " 0".join(format(ord(c), 'b') for c in parola)
       print("rappresentazione", "0" + convertito)