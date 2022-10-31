import os.path
import pickle

from registro import *
from registro_reducido import *


def mostrar_menu():
    equals = '='
    print('\n' + equals * 25 + ' Sistema de Gestión de Series ' + equals * 25 + '\n'
          '1) Procesar el archivo de texto generos.txt.\n'
          '2) Procesar el archivo de texto series.csv.\n'
          '3) Mostrar aquellas series que tengan una duracion entre A y B, estas ingresadas por teclado.\n'
          '4) Crear un vector de conteo que determine la cantidad de series por genero.\n'
          '5) Generar un binario en el que almacenen registros sobre las series.\n'
          '6) Mostrar el archivo generado en el punto 5.\n'
          '7) Buscar en el vector de series si se encuentra una serie, ingresando el titulo por teclado.\n'
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
                votes = int(campo[12])
                registro = Series(link, title, date, certificate, time, genre, rating, resumen, votes)
                if filtrar_registro(registro):
                    registro.runtime_of_episodes = int(registro.runtime_of_episodes[:-4])
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


def validar_duracion(mensaje):
    valor = int(input(mensaje))
    return valor


def mostrar_entre(v_csv, a, b):
    cont = 0
    acum = 0
    v = []
    for i in v_csv:
        if a <= i.runtime_of_episodes <= b:
            cont += 1
            acum += i.runtime_of_episodes
            v.append(i)
            print(i)
    prom = acum // cont
    print('El tiempo promedio de duracion de todas las series es de ' + str(prom) + ' min.\n')
    return v


def validar_booleano(mensaje):
    res = input(mensaje)
    while res not in ("1", "2"):
        res = input("Respuesta invalida! " + mensaje)
    return int(res)


def grabar_csv(v_duracion, v_txt, file_name='punto3_archivo.csv'):
    m = open(file_name, 'wt')
    m.write('Poster_Link|Series_Title|Runtime_of_Series|Certificate|'
            'Runtime_of_Episodes|Genre|IMDB_Rating|Overview|No_of_Votes\n')
    for i in v_duracion:
        cadena = i.poster_link + '|'
        cadena += i.series_title + '|'
        cadena += i.runtime_of_series + '|'
        cadena += i.certificate + '|'
        cadena += str(i.runtime_of_episodes) + ' min|'
        cadena += v_txt[i.genre] + '|'
        cadena += i.IMDB_rating + '|'
        cadena += i.overwiew + '|'
        cadena += i.not_of_vote + '\n'
        m.write(cadena)
    m.close()


def mostrar_por_genero(v_csv, v_txt):
    v_conteo = [0] * len(v_txt)
    for i in v_csv:
        indice = i.genre
        v_conteo[indice] += 1

    for i in range(len(v_txt)):
        print('Del genero', v_txt[i], 'hay', v_conteo[i], 'series.')

    return v_conteo


def grabar_binario(v, v_txt, file_name='punto4_archivo.utn'):
    m = open(file_name, 'wb')
    for i in range(len(v_txt)):
        nom_genero = v_txt[i]
        registro = SeriesReducido(i, nom_genero, v[i])
        pickle.dump(registro, m)
    m.close()


def leer_binario(path_file='punto4_archivo.utn'):
    v = []
    if os.path.exists(path_file):
        m = open(path_file, 'rb')
        pos = os.path.getsize(path_file)
        while m.tell() < pos:
            registro = pickle.load(m)
            v.append(registro)
        m.close()
    return v


def mostrar_vector(v):
    for i in v:
        print(i)


def buscar_titulo(v, tit):
    # La busqueda binaria no sirve, ya que el arreglo fue ordenado por otro atributo.
    indice = -1
    for i in range(len(v)):
        if v[i].series_title == tit:
            indice = i
            break
    return indice


def principal():
    op = -1
    v_txt = []
    v_csv = []
    v_conteo = None
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
                    a = validar_duracion("Ingrese la duraccion minima (A): ")
                    b = validar_duracion("Ingrese la duraccion maxima (B): ")
                    save = validar_booleano("Desea guardar el resultado en otro archivo de texto?"
                                            "(INGRESE EL VALOR) \n1: SI \n2: NO\n")
                    if save == 1:
                        v_duracion = mostrar_entre(v_csv, a, b)
                        grabar_csv(v_duracion, v_txt)

                    else:
                        mostrar_entre(v_csv, a, b)

                elif op == 4:
                    v_conteo = mostrar_por_genero(v_csv, v_txt)
                    input(press)
                elif op == 5:
                    if v_conteo is not None:
                        grabar_binario(v_conteo, v_txt)
                        input('El archivo binario fue creado con exito!. ' + press)
                    else:
                        input('Primero debe generar el vector de conteo en el punto 4!. ' + press)
                elif op == 6:
                    v = leer_binario()
                    mostrar_vector(v)
                else:
                    tit = input('Ingrese el titulo de la serie que desea buscar: ')
                    indice = buscar_titulo(v_csv, tit)
                    if indice != -1:
                        v_csv[indice].not_of_vote += 1
                        input('Los votos de la serie ' + tit + ' ha sido actualizada. ' + press)
                    else:
                        input('La serie con el titulo ' + tit + ' no se encuentra. ' + press)

        elif vuelta > 1:
            input('El valor no corresponde a una opcion valida. ' + press)

        mostrar_menu()
        op = int(input('Ingrese opcion por favor: '))

    print('Cerrando...')


if __name__ == '__main__':
    principal()
