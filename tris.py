#tetris
import random 
import time
verde = '\u001b[92m'
rosso = '\u001b[31m'
Ped_bot=" "
Ped_us=str(input("che pedina scegli @ o X?"))
while (Ped_us != "@" and Ped_us != "X" and Ped_us != "x" ):
    print("scegliere @ o X")
    Ped_us=str(input("che pedina scegli @ o X?"))
if (Ped_us == "@"):
    Ped_bot = "X"
else:
    Ped_bot="@"

Unavailable_Cell=0
Pl_turn=True

p1="1"
p2="2"
p3="3"
p4="4"
p5="5"
p6="6"
p7="7"
p8="8"
p9="9"

def label():
    print("")
    print(" ",p1," | ",p2," | ",p3," ")
    print("-----------------")
    print(" ",p4," | ",p5," | ",p6," ")
    print("-----------------")
    print(" ",p7," | ",p8," | ",p9," ")
    print("")
label()

while Unavailable_Cell < 8:
    while Pl_turn == True:
        print("turno tuo digita i numeri per mettere la tua pedina")
        Pl_position=str(input())
    
        if Pl_position == "1":
            if p1 != Ped_bot and p1 != Ped_us:
                p1=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "2":
            if p2 != Ped_bot and p2 != Ped_us:
                p2=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "3":
            if p3 != Ped_bot and p3 != Ped_us:
                p3=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "4":
            if p4 != Ped_bot and p4 != Ped_us:
                p4=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "5":
            if p5 != Ped_bot and p5 != Ped_us:
                p5=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "6":
            if p6 != Ped_bot and p6 != Ped_us:
                p6=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "7":
            if p7 != Ped_bot and p7 != Ped_us:
                p7=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "8":
            if p8 != Ped_bot and p8 != Ped_us:
                p8=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
        if Pl_position == "9":
            if p9 != Ped_bot and p9 != Ped_us:
                p9=Ped_us
                Unavailable_Cell +=1
                Pl_turn=False
                Op_turn=True
            else:
                print("seleziona posto disponibile")
    
    while Op_turn == True:
        Op_position=random.randint(1,9)
        Op_position=str(Op_position)
        if Op_position == "1":
            if(p1 != Ped_us and p1 != Ped_bot):
                p1=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        if Op_position == "2":
            if(p2 != Ped_us and p2 != Ped_bot):
                p2=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        if Op_position == "3":
            if(p3 != Ped_us and p3 != Ped_bot):
                p3=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
                Pl_turn = True
        if Op_position == "4":
            if(p4 != Ped_us and p4 != Ped_bot):
                p4=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        if Op_position == "5":
            if(p5 != Ped_us and p5 != Ped_bot):
                p5=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        if Op_position == "6":
            if(p6 != Ped_us and p6 != Ped_bot):
                p6=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        if Op_position == "7":
            if(p7 != Ped_us and p7 != Ped_bot):
                p7=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        if Op_position == "8":
            if(p8 != Ped_us and p8 != Ped_bot):
                p8=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        if Op_position == "9":
            if(p9 != Ped_us and p9 != Ped_bot):
                p9=Ped_bot
                Unavailable_Cell +=1
                Op_turn=False
                Pl_turn = True
            else:
                Op_position=random.randint(1,9)
                Op_position=str(Op_position)
                Pl_turn= False
        label()
    
    if ((p1 == p5 and p1 == p9) or (p3 == p5 and p3 == p7) or (p1 == p4 and p1 == p7) or (p2 == p5 and p2 == p8) or (p3 == p6 and p3 == p9) or (p1 == p2 and p1 == p3) or (p4 == p5 and p4 == p6) or (p7 == p8 and p7 == p9)):
        Unavailable_Cell = 10
        print(rosso+"ABBIAMO UN VINCITORE","tu avevi carattere",Ped_us)
        time.sleep(10)
if Unavailable_Cell == 8:
    print(verde+"PARITà")
    time.sleep(10)


        


