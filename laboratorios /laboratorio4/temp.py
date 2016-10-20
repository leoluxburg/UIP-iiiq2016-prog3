try :
    css = "y"
    while css == 'y' :
        t = float(input("Temperatura: "))
        if t >= 37.5 :
            print ("Fiebre")
            db = open('temp.dat','a')
            db.write(str(t) + " Fiebre\n")
            css = (input("Para continuar precione y: "))
            if css != 'y' :
                print ("Adios")
        elif t <= 30 and t > 5 :
            print ("Enfermo")
            db = open('temp.dat','a')
            db.write(str(t) + " Enfermo\n")
            css = (input("Para continuar precione y: "))
            if css != 'y' :
                print ("Adios")
        elif t <= 5 :
            print ("FATALITY")
            db = open('temp.dat','a')
            db.write(str(t) + " Fatality\n")
            css = (input("Para continuar precione y: "))
            if css != 'y' :
                print ("Adios")
        else :
            print ("Tas cool")
            db = open('temp.dat','a')
            db.write(str(t) + "  Sano\n")
            css = (input("Para continuar precione y: "))
            if css != 'y' :
                print ("Adios")

except ValueError:
    print("Dato no valido")
