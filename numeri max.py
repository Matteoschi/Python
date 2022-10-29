a=input("inserire 1° numero :")
b=input("inserire 2° numero :")
c=input("inserire 3° numero :")
if (a == b == c):
    print("tutti i numeri sono uguali")
else:
    if (a>b) and (a>c):
        print("primo numero maggiore") 
    else:
        if (b>c):
            print("secondo numero maggiore")
        else:
            print("terzo numero maggiore")
    
           