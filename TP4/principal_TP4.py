import os.path
from registro_TP4 import *


def mostrar_menu():
    print('\n=== MENÚ ===\n'
          '1) Cargar proyectos\n'
          '2) Filtrar por tag\n'
          '3) Lenguajes\n'
          '4) Popularidad\n'
          '5) Buscar proyecto actualizado\n'
          '6) Guardar populares\n'
          '7) Mostrar archivo\n'
          '0) Salir del Programa\n')


def add_in_order(vec, proyecto):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].repositorio == proyecto.repositorio:
            pos = c
            break
        if proyecto.repositorio < vec[c].repositorio:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [proyecto]


def cargar_archivo(nombre):
    if not os.path.exists(nombre):
        print('Archivo inexistente')
        return

    vec = []
    nro_linea = 0
    m = open(nombre, mode="rt", encoding="utf8")
    for linea in m:
        nro_linea += 1
        if nro_linea == 1:
            continue

        if linea[-1] == '\n':
            linea = linea[:-1]
        campos = linea.split('|')
        nombre_usuario = campos[0]
        repositorio = campos[1]
        fecha_actualizacion = campos[3]
        lenguaje = campos[4]
        likes = campos[5][:-1] + '.'
        tags = campos[6]
        url = campos[7]
        proyecto = Proyecto(nombre_usuario, repositorio, fecha_actualizacion, lenguaje, likes, tags, url)
        add_in_order(vec, proyecto)
    m.close()
    return vec


def mostrar_proyectos(v):
    print('nombre_usuario, repositorio, fecha_actualizacion, lenguaje, likes, tags, url')
    for proyecto in v:
        print(proyecto)


def principal():
    op = -1
    while op != 0:
        mostrar_menu()
        op = int(input('ingrese opcion: '))
        if op == 1:
            v = cargar_archivo('proyectos.csv')
            mostrar_proyectos(v)


if __name__ == '__main__':
    principal()
