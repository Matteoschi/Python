import random

caratteri_minuscole = "abcdefghilmnopqrstuvz"
caratteri_maiuscoli = " ABCDEFGHILMNOPQRSTUVZ"
caratteri_speciali = "\|!£$%&/()=?^é*§°ç;:_[]@#"
numeri = "1234567890"
indicare= input(" alfanumerico, minuscole+maiuscole , alfanumerico+caratteri speciali")

if indicare == ("alfanumerico"):
    Join1 = caratteri_minuscole + caratteri_maiuscoli + numeri
    password = "".join(random.sample(Join1, 11))
    print(password)
if indicare == ("minuscole+maiuscole"):
    Join2 = caratteri_minuscole + caratteri_maiuscoli
    password = "".join(random.sample(Join2, 11))
    print(password)
if indicare == ("alfanumerico+caratteri speciali"):
    Join3 = caratteri_minuscole + caratteri_maiuscoli + numeri + caratteri_speciali
    password = "".join(random.sample(Join3, 11))
    print(password)

#by maatteo



