"""         TRABAJO PRÁCTICO N°3:
    MATERIA: ALGORITMOS Y ESTRUCTURAS DE DATOS
    Curso: 1K15
    Año: 2022
    Participantes:
    Barreto Juan Manuel, 77643, [1K15]
    Carrizo Nahuel, 87557, [1K15]
    Flores Principe Alejandro Hernan, 79059, [1K15] """

from registro import *
import string
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


def cargar_proyectos(vec, n):
    for i in range(n):
        # el numero debe aparecer UNA SOLA vez
        numero = random.randrange(1, 100)
        fecha = "20-02-2011"
        titulo = random.choice(["AR", "BR", "CH", "PR", "PE", "CO", "UR"])
        lenguaje = random.randint(0, 10)
        cant_lineas = random.randint(500, 800)
        proyecto = Proyecto(numero, fecha, titulo, lenguaje, cant_lineas)
        vec.append(proyecto)


# Número de proyecto
# Título
# Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
# Lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
# Cantidad de líneas de código


def ordenar_proyecto(vec):
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
    pass


def calcular_cantidad_lineas(vec):
    v = [] * 11
    for i in vec:
        v[i.lenguaje] += 1
    return v


def mostrar_cant_lineas(v_acum_lineas):
    for i in range(len(v_acum_lineas)):
        print("El lenguaje", convertir_titulo(i), " acumula ", v_acum_lineas[i], "lineas.")


def filtrar_lenguaje(vec, ln):
    pass


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
                    ordenar_proyecto(vec)
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
                    ln = input("Que lenguaje desea filtrar? ")
                    filtrar_lenguaje(vec, ln)
                elif op == 7:
                    pass
            else:
                print("Primero deber cargar los proyectos")
        mostrar_menu()
        op = int(input('\ningrese una opcion (Con cero sale):'))


if __name__ == '__main__':
    principal()
