import math

option = int(input("Válassz a lehetőségek közül: "))

while(option!=0):
    if(option == 1):
        print("\tElsőfokú egyenlet (a*x+b=c")

        a = int(input("\tKérem az a együtthatót: "))
        b = int(input("\tKérem a b együtthatót: "))
        c = int(input("\tKérem z c együtthatót: "))

        x1 = (c-b)/a

        txt = "Megoldás: " + str(x1)
        print(txt)
    
