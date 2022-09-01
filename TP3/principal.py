"""         TRABAJO PRÁCTICO N°3:
    MATERIA: ALGORITMOS Y ESTRUCTURAS DE DATOS
    Curso: 1K15
    Año: 2022
    Participantes:
    Barreto Juan Manuel, 77643, [1K15]
    Carrizo Nahuel, 87557, [1K15]
    Flores Principe Alejandro Hernan, 79059, [1K15]

"""

from registro import *
import random


def mostrar_menu():
    sep = "=" * 90
    texto = "\n" + sep
    texto += "\n\t\t\t\t\t\t\t\t\tMenu de opciones\n"
    texto += sep
    texto += '\n1- Cargar proyectos'
    texto += '\n2- Listar proyectos: Mostrar proyectos ordenados por titulo.'
    texto += '\n3- Actualizar proyecto: Modificar la cantidad de lineas y la fecha de actualizacion.'
    texto += '\n4- Resumen por lenguaje: Calcular la cantidad de lineas por lenguaje.'
    texto += '\n5- Resumen por año: Calcular la cantidad de proyectos actualizados por anio.'
    texto += '\n6- Filtrar lenguaje: Mostrar ordenados por numero, los proyectos hecho en un lenguaje.'
    texto += '\n7- Productividad: Mostrar el/los anio con mayor cantidad de proyectos actualizados.'
    texto += '\n0- Salir del Programa.\n'
    texto += sep
    return texto


def esta_numero(vec, n):
    esta = False
    for i in vec:
        if i.numero == n:
            esta = True
            break
    return esta


def crear_proyecto_random():
    numero = random.randint(1, 9999999)
    dia = str(random.randint(1, 31))
    mes = str(random.randint(1, 12))
    if len(dia) == 1:
        dia = "0" + dia
    if len(mes) == 1:
        mes = "0" + mes
    anio = str(random.randint(2000, 2022))
    fecha = dia + "-" + mes + "-" + anio
    titulo = random.choice(["AR", "BR", "CH", "PR", "PE", "CO", "UR"])
    lenguaje = random.randint(0, 10)
    cant_lineas = random.randint(500, 800)
    return Proyecto(numero, fecha, titulo, lenguaje, cant_lineas)


def validar_fecha(fecha):
    numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    dato = ""
    valido = False
    n = len(fecha)
    if n == 10:
        valido = True
        for i in range(n):
            if i in (2, 5):
                if fecha[i] != "-":
                    valido = False
                    break
                if i == 2:
                    if not 0 < int(dato) < 32:
                        valido = False
                        break
                else:
                    if not 0 < int(dato) < 13:
                        valido = False
                        break
                dato = ""
            else:
                if fecha[i] not in numeros:
                    valido = False
                    break
                dato = dato + fecha[i]
                if i == n-1:
                    if not 1999 < int(dato) < 2023:
                        valido = False
                        break
    return valido


def crear_proyecto_manual(n):
    n = str(n)
    numero = int(input(n + "-Ingrese el numero del proyecto: "))
    while numero < 1:
        numero = int(input(n + "-Ingrese el numero del proyecto: "))
    fecha = input(n + "-Fecha de creacion (Formato dd-mm-yyyy): ")
    while not validar_fecha(fecha):
        fecha = input(n + "-Fecha de creacion (Formato dd-mm-yyyy): ")
    titulo = input(n + "-Ingrese el nombre del proyecto: ")
    print("\n" + mostrar_lenguajes())
    lenguaje = int(input(n + "-Ingrese el valor que corresponda: "))
    cant_lineas = int(input(n + "-Ingrese la cantidad de lineas del proyecto: "))
    return Proyecto(numero, fecha, titulo, lenguaje, cant_lineas)


def cargar_proyectos(vec, n):
    texto_opc = "\nAgregar proyectos de forma: \n1)Automatica \n2)Manual: \nRta: "
    opc = int(input(texto_opc))
    while 1 > opc or opc > 2:
        opc = int(input(texto_opc))
    for i in range(n):
        if opc == 1:
            proyecto = crear_proyecto_random(i+1)
        else:
            proyecto = crear_proyecto_manual(i+1)
        while esta_numero(vec, proyecto.numero):
            if opc == 2:
                print("\nEl proyecto N:", proyecto.numero, "ya existe, intente cargar otro.")
            proyecto = crear_proyecto_manual(i+1)
        vec.append(proyecto)


def ordenar_x_titulo(vec):
    n = len(vec)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if vec[i].titulo > vec[j].titulo:
                vec[i], vec[j] = vec[j], vec[i]


def mostrar_proyecto(vec):
    for proyecto in vec:
        print(proyecto)


def busqueda_secuencial(vec, x):
    res = None
    for i in range(len(vec)):
        if vec[i].numero == x:
            res = i
            break
    return res


def actualizar_proyecto(proyecto):
    lineas = int(input("Cantidad de lineas actualizada de " + proyecto.titulo + ": "))
    while lineas < 0:
        lineas = int(input("La cantidad de lineas no puede ser menor a uno. Reintentelo: "))
    fecha = input("Fecha de actualizacion de " + proyecto.titulo + ". Con formato (dd-mm-yyyy): ")
    while not validar_fecha(fecha):
        fecha = input("Fecha de actualizacion de " + proyecto.titulo + ". Con formato (dd-mm-yyyy):")
    proyecto.cant_lineas = lineas
    proyecto.fecha = fecha


def calcular_cantidad_lineas(vec):
    v = [0] * 11
    for i in vec:
        v[i.lenguaje] += i.cant_lineas
    return v


def mostrar_cant_lineas(v_acum_lineas):
    for i in range(len(v_acum_lineas)):
        print("El lenguaje", convertir_titulo(i), "acumula", v_acum_lineas[i], "lineas.")


def ordenar_x_numero(vec):
    for i in range(len(vec) - 1):
        for j in range(i + 1, len(vec)):
            if vec[i].numero > vec[j].numero:
                vec[i], vec[j] = vec[j], vec[i]


def mostrar_x_lenguaje(vec, ln):
    for i in vec:
        if i.lenguaje == ln:
            print(i)


def mostrar_lenguajes():
    texto = "{:<3}".format("ID") + "| LENGUAJE"
    for i in range(11):
        texto += "\n" + "{:<3}".format(str(i)) + "| " + str(convertir_titulo(i))
    return texto


def calcular_proyectos_x_anio(vec, v_cant):
    for i in range(len(vec)):
        anio = int(vec[i].fecha[6:10])
        v_cant[anio-2000] += 1
    return v_cant


def mostrar_proyectos_anio(v_indice):
    texto = ""
    for i in range(len(v_indice)):
        if v_indice[i] != 0:
            texto += "\nEn el año " + str(i + 2000) + " se actualizaron " + str(v_indice[i]) + " proyectos."
    return texto


def obtener_cant_mayor(v_cant_x_fecha):
    my = 0
    for i in v_cant_x_fecha:
        if i > my:
            my = i
    return my


def mostrar_cant_mayor(v_cant, x):
    v = []
    texto = "La mayor cantidad de proyecto actualizados es de " + str(x)
    for i in range(len(v_cant)):
        if v_cant[i] == x:
            v.append(i + 2000)
    if len(v) == 1:
        texto += " y fue en el año " + str(v[0])
    else:
        texto += " y fue en los siguientes años"
        for i in v:
            texto += ", " + str(i)
        texto += "."
    return texto


def principal():
    vec = []
    v_cant_x_fecha = [0] * 23
    op = -1
    bandera_5 = False

    while op != 0:
        if op == 1:
            n = int(input('Ingrese la cantidad de proyectos a cargar:'))
            while n < 1:
                n = int(input('Ingrese la cantidad de proyectos a cargar (Mayor a cero):'))
            cargar_proyectos(vec, n)
            print('Proyectos cargados...')
            bandera_5 = False
        elif 2 <= op <= 7:
            if len(vec) != 0:
                if op == 2:
                    ordenar_x_titulo(vec)
                    mostrar_proyecto(vec)

                elif op == 3:
                    x = int(input('ACTUALIZAR: Ingrese el numero del proyecto:'))
                    indice = busqueda_secuencial(vec, x)
                    if indice is not None:
                        print("Proyecto encontrado!!!")
                        actualizar_proyecto(vec[indice])
                    else:
                        print("El proyecto Nº", x, "no existe.")

                elif op == 4:
                    v_acum_lineas = calcular_cantidad_lineas(vec)
                    mostrar_cant_lineas(v_acum_lineas)

                elif op == 5:
                    calcular_proyectos_x_anio(vec, v_cant_x_fecha)
                    print(mostrar_proyectos_anio(v_cant_x_fecha))
                    bandera_5 = True

                elif op == 6:
                    print(mostrar_lenguajes())
                    ln = int(input("Que lenguaje desea filtrar? (Escriba el ID): "))
                    while ln < 0 or ln > 10:
                        ln = int(input("ERROR - Que lenguaje desea filtrar? (Escriba el ID): "))
                    ordenar_x_numero(vec)
                    mostrar_x_lenguaje(vec, ln)

                elif op == 7:
                    if bandera_5:
                        x = obtener_cant_mayor(v_cant_x_fecha)
                        print(mostrar_cant_mayor(v_cant_x_fecha, x))
                    else:
                        print("Primero debe calcular la cantidad de proyectos por año (PUNTO 5), "
                              "o volver a calcularlo en caso de haber agregado nuevos proyectos.")

            else:
                print("Primero deber cargar los proyectos (PUNTO 1)")
        print(mostrar_menu())
        op = int(input('\nIngrese una opcion (Con cero sale):'))


if __name__ == '__main__':
    principal()
