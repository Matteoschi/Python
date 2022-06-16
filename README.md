# Projects with python
In this repository dedicated to physics you will find various python codes to calculate  for example:
- [Binary code](#Binary-code)
- [Password generator](#Password-generator)
- [Prime numbers](#Prime-numbers)
- [How to do QR code](#How-to-do-QR-code)
- [Quiz app](#Quiz-app)

## Binary code
<a name="Binary-code"></a>
The binary code consists of two digits: 0 and and is a positional type number system. It is used in computer science for the representation of true and false logical values
How you do it? We start from the number we have chosen, for example 12, and divide by two until we obtain the cancellation of the quotient. For instance:

- 12:2=6    resto 0
- 6:2=3     resto 0
- 3:2=1     resto 1
- 1:2=0     resto 1
- 0:2=0

```
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
```
## Password generator
<a name="Password-generator"></a>
Use our password generator to instantly create a secure and random password  as desired by the customer. Infact the costumer can decide how the password should be:
```
indicare= input(" alfanumerico, minuscole+maiuscole , alfanumerico+caratteri speciali ")
```
## Prime numbers
<a name="Prime-numbers"></a>
Prime numbers are those natural numbers greater than one that are divisible only by themselves and by one. For example, 2 (the only even number, among other things, to be prime), 3, 5 and 7. But not 6, which is divisible by 2 and 3
```
for i in range(2, Numero):
    if (Numero % i) == 0:
        primo = False
```
## How to do QR code
<a name="How-to-do-QR-code"></a>
first of all we have to import libraries.
```
import time
import qrcode
from pyzbar.pyzbar import decode
import cv2
```
infact most of the code work is done by library presets
```
img=qrcode.make(codice)
```
## Quiz app
<a name="Quiz-app"></a>
first of all you have to write what the questions are
```
DOMANDE = []
```
then set the score and how many righ answers you do
```
Punti = 1
punti_corretti = 0
```

