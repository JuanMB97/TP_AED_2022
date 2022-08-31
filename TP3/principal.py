"""         TRABAJO PRÁCTICO N°3:
    MATERIA: ALGORITMOS Y ESTRUCTURAS DE DATOS
    Curso: 1K15
    Año: 2022
    Participantes:
    Barreto Juan Manuel, 77643, [1K15]
    Carrizo Nahuel, 87557, [1K15]
    Flores Principe Alejandro Hernan, 79059, [1K15] """

from registro import *
import random


def mostrar_menu():
    print("\n==================================================================================")
    print("\t\t\t\t\t\t\tMenu de Búsqueda")
    print("==================================================================================")
    print('\t1- Cargar proyectos', end=' | ')
    print('2- Listar proyectos', end=' | ')
    print('3- Actualizar proyecto')
    print('\t4- Resumen por lenguaje', end=' | ')
    print('5- Resumen por año', end=' | ')
    print('6- Filtrar lenguaje')
    print('\t' * 3, '7- Productividad:', end=' | ')
    print('0- Salir del Programa', end=' | ')
    print("\n==================================================================================")


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


def crear_proyecto_manual():
    numero = int(input("Ingrese el numero del proyecto: "))
    fecha = input("Fecha de creacion (Formato dd-mm-yyyy): ")
    while not validar_fecha(fecha):
        fecha = input("Fecha de creacion (Formato dd-mm-yyyy): ")
    titulo = input("Ingrese el nombre del proyecto: ")
    lenguaje = int(input("Ingrese el valor que corresponda: "))
    cant_lineas = int(input("Ingrese la cantidad de lineas del proyecto: "))
    return Proyecto(numero, fecha, titulo, lenguaje, cant_lineas)


def cargar_proyectos(vec, n):
    texto_opc = "\nAgregar proyectos de forma: \n1)Automatica \n2)Manual: \nRta: "
    for i in range(n):
        opc = int(input(texto_opc))
        while 1 > opc or opc > 2:
            opc = int(input(texto_opc))
        if opc == 1:
            proyecto = crear_proyecto_random()
        else:
            proyecto = crear_proyecto_manual()
        while esta_numero(vec, proyecto.numero):
            proyecto = crear_proyecto_manual()
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


def actualizar_proyecto(vec, indice, lineas, fecha):
    return True


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


def principal():
    vec = []
    op = -1
    while op != 0:
        if op == 1:
            n = int(input('Ingrese la cantidad de proyectos a cargar:'))
            while n < 1:
                n = int(input('Ingrese la cantidad de proyectos a cargar (Mayor a cero):'))
            cargar_proyectos(vec, n)
            print('Proyectos cargados...')

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
                        lineas = input("Cantidad de lineas: ")
                        fecha = input("Fecha de actualizacion: ")
                        actualizar_proyecto(vec, indice, lineas, fecha)
                    else:
                        print('El numero de proyecto no se encuentra')
                elif op == 4:
                    v_acum_lineas = calcular_cantidad_lineas(vec)
                    mostrar_cant_lineas(v_acum_lineas)
                elif op == 5:
                    pass
                elif op == 6:
                    for i in range(11):
                        print(i, ":", convertir_titulo(i))
                    ln = int(input("Que lenguaje desea filtrar? "))
                    ordenar_x_numero(vec)
                    mostrar_x_lenguaje(vec, ln)
                elif op == 7:
                    pass
            else:
                print("Primero deber cargar los proyectos")
        mostrar_menu()
        op = int(input('\ningrese una opcion (Con cero sale):'))


if __name__ == '__main__':
    principal()
