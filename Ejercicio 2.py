import csv
partidos = []
print("Bienvenido al programa de conteo rápido de Elecciones Generales 2023")
while True:
    print("Que desea hacer?")
    print("1. Ingresar partidos políticos")
    print("2. Salir")
    datop = input()
    if datop == "1":
        while True:
            try:
                print("Ingrese el código, nombre y siglas del partido politico")
                codigo = input()
                print("Ingrese el nombre")
                nombre = input()
                print("Ingrese las siglas")
                siglas = input()
                partidos.append({"Código: ",codigo, "Nombre: ", nombre, "Siglas: ",siglas, "Votos validos: ", 0})
            except:
                print("Ingreso un dato erroneo, por favor vuelva a intentarlo")
            print(partidos)
            print("Desea ingresar otros partidos? (S/N)")
            a = input()
            if a == "S" or a == "s":
                print("Muy bien volvas a color los datos")
                print()
            elif a == "N" or a == "n":
                print("Muy bien sigamos con lo demás")
                print()
                print("Ingrese el código del partido al cual se le agregara el número de mesa, departamento, municipio y votos validos")
                a2 = input()
                for j in partidos:
                    if j["Código"] == a2:
                        print("El partido escogido fue:",j["Cógido"],j["Nombre"],j["Siglas"],j["Votos validos"])
                        print("Es este tu partido? (S/N)")
                        a3 = input()
                        if a3 == "S" or a3 == "s":
                            while True:
                                print("Perfecto vamos a darles un valor al número de mesa, departamento, municipio y votos validos")
                                print()
                                print("Por favor coloque el número de mesa en número enteros")
                                try:
                                    a4 = int(input())
                                except:
                                    print("Dato invalido vuelva a intentarlo")
                                print("Ingrese el departamento")
                                a5 = input()
                                print("Ingrese el municipio")
                                a6 = input()
                                partidos.append({"Número de mesa: ",a4, "Departamento: ",a5, "Municipio: ",a6})
                                print("Coloque los votos validos por favor (Unicamente en números enteros)")
                                a7 = int(input())
                                j["Votos validos"] = a7
                                print(partidos,"estos serian sus núevos datos")
                                print("Desea ingresar otros datos de otro partido? (S/N)")
                                b = input()
                                if b == "s" or b =="S":
                                    print("Muy bien vamos a ello")
                                    print()
                                elif b == "n" or b == "N":
                                    print("Muy bien, acontinuación se presentara la lista con los partidos que van más alto hasta el más bajo")
                                    partidos.sort(reverse=True)
                                    print(partidos)
                                    nombre_archivo = "acta__de_notas_" + ".csv"#Este apartado crea el documento csv mediante la librería que importamos llamada csv
                                    with open(nombre_archivo, "w", newline="") as archivo:
                                        escritor_csv = csv.writer(archivo)
                                        escritor_csv.writerow(["Carnet", "Nombre", "Carrera", "Nota"])#Aquí crea los respectivos apartados en el documento csv donde marca el carnet, nombre, carrera y nota de cada estudiante
                                        total_notas = 0
                                        for partido in partidos:
                                            ([partido["Código"], partido["Nombre"], partido["Sigla"], partido["Departamento"], partido["Municipio"], partido["Número de mesa"], partido["Votos validos"]])#Aquí lo que hace es que empieza a generar el promediado de todos los partidos leyendo mediante un len la cantidad de los partidos y sumando las notas de todos ellos y luego dividiendola en el len anterior
                                            total_notas += partido["Votos validos"]
                                        promedio_notas = total_notas / len(partidos)
                                        escritor_csv.writerow([])
                                        escritor_csv.writerow(["Promedio de notas:", "", "", promedio_notas])
                                    print("Acta de notas exportada exitosamente.")
            else:
                print("Ingreso un dato invalido vuelva a intentar")
    elif datop == "2":
        print("Gracias por usar el programa :D")
        break
        