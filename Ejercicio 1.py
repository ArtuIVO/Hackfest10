#Usare el municipio de mixco que es el 08 y el de la ciudad de guatemala que es el 01
#Usare el municipio de Chiantla que es el 02 y el de malacatancito que es el 03 y 
#el de nenton que es el 05
print("Bienvenido al programa para conteo de votos")
while True:
    print("Que deseas hacer ?")
    print("1. Ingresar al sentro de votaciones")
    print("2. Salir")
    datoprim = input()
    if datoprim == "1":
        while True:
            print("Ingrese su fecha de nacimiento en base a DDMMAAAA, ejemplo: 180220005")
            datop = input()
            datop2=(datop[4:])
            if datop2 <= "2005":
                while True:
                    print("Por favor ingrese el código único de identificación (CUI)")
                    a = input()
                    mesa = (a[0:4])
                    centro = (a[4:9])
                    departamento = (a[9:11])
                    municipio = (a[11:13])
                    a2 = (len(a))
                    if len(a) < a2 or len(a) > a2:
                        print("Usted ingreso un CUI erroneo, por favor vuelva a intentarlo")
                    elif len(a) == a2:
                        print("Verifiquemos que estos datos sean los correctos:")
                        print("Departamento: ")
                        if departamento == "01":
                            print("Guatemala")
                        elif departamento == "02":
                            print("El Progreso")
                        elif departamento == "03":
                            print("Sacatepeques")
                        elif departamento == "04":
                            print("Chimaltenango")
                        elif departamento == "05":
                            print("Escuintla")
                        elif departamento == "06":
                            print("Santa Rosa")
                        elif departamento == "07":
                            print("Sololá")
                        elif departamento == "08":
                            print("Totonicapán")
                        elif departamento == "09":
                            print("Quetzaltenango")
                        elif departamento == "10":
                            print("Suchitepequez")
                        elif departamento == "11":
                            print("Retalhuleu")
                        elif departamento == "12":
                            print("San Marcos")
                        elif departamento == "13":
                            print("Huehuetenango")
                        elif departamento == "14":
                            print("Quiché")
                        elif departamento == "15":
                            print("Baja Verapaz")
                        elif departamento == "16":
                            print("Alta Verapaz")
                        elif departamento == "17":
                            print("Petén")
                        elif departamento == "18":
                            print("Izabal")
                        elif departamento == "19":
                            print("Zacapa")
                        elif departamento == "20":
                            print("Chiquimula")
                        elif departamento == "21":
                            print("Jalapa")
                        elif departamento == "22":
                            print("Jutiapa")
                        print("Municipio: ")
                        if municipio == "01":
                            print("Ciudad de Guatemala")
                        elif municipio == "02":
                            print("Chiantla")
                        elif municipio == "03":
                            print("Malacatancito")
                        elif municipio == "05":
                            print("Nentón")
                        elif municipio == "08":
                            print("Mixco")
                        print("Centro de votación:")
                        print(centro)
                        print("Mesa:")
                        print(mesa)
                        break
            print("Desea hacer otra consulta? (S/N)")
            b2 = input()
            if b2 == "S" or b2 == "s":
                break
            elif b2 == "N" or b2 == "n":
                break
            elif datop2 > "2005":
                print("Usted es menor de edad, aún no puede votar")
                print("Desea hacer otra consulta? (S/N) ")
                b = input()
                if b == "S" or b == "s":
                    break
                elif b == "N" or b == "n":
                    break
    elif datoprim == "2":
        print("Gracias por usar el programa :D")
        break
    else:
        print("Ingreso un dato erroneo, vuelva a intentarlo, recuerde que es el número a la par de la categoria")
        