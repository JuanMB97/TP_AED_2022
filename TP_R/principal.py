import os.path
from registro import *


def mostrar_menu():
    equals = '='
    print('\n' + equals * 25 + ' Gestión de Proyectos [v2.0]' + equals * 25 + '\n'
          '1) Cargar proyectos\n'
          '2) Mostrar proyectos que contengan cierta etiqueta (TAG)\n'
          '3) Determinar cantidad de proyectos por enguajes y listarlos de mayor a menor\n'
          '4) Crear matriz de popularidad\n'
          '5) Buscar proyecto para actualizar fecha y url.\n'
          '6) Guardar en disco un archivo con los datos de la matriz generada en el punto 4.\n'
          '7) Mostrar la matriz del archivo grabado en el punto 6.\n'
          '8) Salir del Programa\n')


def leer_txt(v, archivo):
    if os.path.exists(archivo):
        m = open(archivo, "rt")
        for linea in m:
            linea = linea[:-1]
            v.append(linea)
        m.close()


def filtrar_registro(registro):
    filtro = True
    if registro.runtime_of_episodes == '':
        filtro = False
    return filtro


def leer_csv(v_txt, v_csv, archivo):
    if os.path.exists(archivo):
        cont = 0
        m = open(archivo, 'rt')
        for linea in m:
            cont += 1
            if cont == 1:
                continue
            else:
                linea = linea[:-1]
                campo = linea.split('|')
                link = campo[0]
                title = campo[1]
                date = campo[2]
                certificate = campo[3]
                time = campo[4]
                genre = campo[5]
                rating = campo[6]
                resumen = campo[7]
                votes = campo[12]
                registro = Series(link, title, date, certificate, time, genre, rating, resumen, votes)
                if filtrar_registro(registro):
                    registro.runtime_of_episodes = registro.runtime_of_episodes[:-4]
                    registro.genre = obtener_indice_genero(v_txt, registro.genre)
                    add_in_order(v_csv, registro)
        m.close()


def obtener_indice_genero(v_generos, genero):
    indice = -1
    for i in range(len(v_generos)):
        if v_generos[i] == genero:
            indice = i
    return indice


def add_in_order(vec, registro):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].not_of_vote == registro.not_of_vote:
            pos = c
            break
        if registro.not_of_vote < vec[c].not_of_vote:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [registro]


def principal():
    op = -1
    v_txt = []
    v_csv = []
    vuelta = 0
    press = 'Presione enter para continuar...'
    generos = "generos.txt"
    series = "series_aed.csv"

    while op != 8:
        vuelta += 1
        if op == 1:
            leer_txt(v_txt, generos)
            if len(v_txt) != 0:
                input('El archivo TXT se leyo con exito!. ' + press)
            else:
                input('ERROR: El archivo TXT no pudo ser leido o está vacio. ' + press)
        elif op == 2 and len(v_txt) != 0:
            leer_csv(v_txt, v_csv, series)
            if len(v_txt) != 0:
                input('El archivo CSV se leyo con exito!. ' + press)
            else:
                input('ERROR: El archivo CSV no pudo ser leido o está vacio. ' + press)
        elif 2 < op < 8:
            if len(v_csv) == 0:
                input('Primero debe leer los archivos y cargarlos en memoria! (PUNTOS 1 Y 2). ' + press)
            else:
                if op == 3:
                    pass
                elif op == 4:
                    pass
                elif op == 5:
                    pass
                elif op == 6:
                    pass
                else:
                    pass
        elif vuelta > 1:
            input('El valor no corresponde a una opcion valida. ' + press)

        mostrar_menu()
        op = int(input('Ingrese opcion por favor: '))

    print('Cerrando...')


if __name__ == '__main__':
    principal()
