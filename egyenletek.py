
egyenletek = ["Elsőfokú","másodfokú"]
választás = ["első", "másod"]


def f1(label):
    print(label)


    prompt = "\tElsőfokú(írd:első), vagy másodfokú(írd:másod) egyenletet szeretnél megoldani? : "
    első= input(prompt)
    x = 0

    for i in range(0, len(egyenletek),1):
        if(egyenletek[i] == első):
            prompt = "\tAdd meg az a értékét: "
            number1 = int(input(prompt))

            prompt = "\tAdd meg az b értékét: "
            number2 = int(input(prompt))

            txt = "\t"+str(number1*x+number2)
            print(txt)
            
            
        










f1("")
