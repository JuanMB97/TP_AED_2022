import os.path
import pickle
from Proyecto import *
from datetime import datetime
from Popular import *


def mostrar_menu():
    print('\n=== MENÚ ===\n'
          '1) Cargar proyectos\n'
          '2) Mostrar proyectos que contengan cierta etiqueta (TAG)\n'
          '3) Determinar cantidad de proyectos por enguajes y listarlos de mayor a menor\n'
          '4) Crear matriz de popularidad\n'
          '5) Buscar proyecto para actualizar fecha y url.\n'
          '6) Guardar en disco un archivo con los datos de la matriz generada en el punto 4.\n'
          '7) Mostrar la matriz del archivo grabado en el punto 6.\n'
          '8) Salir del Programa\n')


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


def filtrar_linea(v, campos):
    res = True
    if campos[4] == '':
        res = False

    # Si el campo lenguaje no viene vacio, verificar si el proyecto ya existe en el vector a traves del URL.
    if res:
        for i in v:
            if campos[7] == i.url:
                res = False
    return res


def cargar_archivo(v, path_file='proyectos.csv'):
    # Datos es un vector con dos valores → 0: Cantidad de proyectos cargados 1: Cantidad de proyectos omitidos
    datos = [0] * 2

    if os.path.exists(path_file):
        nro_linea = 0
        m = open(path_file, mode='rt', encoding='utf8')
        for linea in m:
            nro_linea += 1
            if nro_linea == 1:
                continue

            if linea[-1] == '\n':
                linea = linea[:-1]
            campos = linea.split('|')
            
            if filtrar_linea(v, campos):
                datos[0] += 1
                nombre_usuario = campos[0]
                repositorio = campos[1]
                fecha_actualizacion = campos[3]
                lenguaje = campos[4]
                likes = float(campos[5][:-1])
                tags = campos[6].split(',')
                url = campos[7]
    
                proyecto = Proyecto(nombre_usuario, repositorio, fecha_actualizacion, lenguaje, likes, tags, url)
                add_in_order(v, proyecto)
            else:
                datos[1] += 1
        m.close()

    return datos


def mostrar_proyectos(v):
    print('nombre_usuario, repositorio, fecha_actualizacion, lenguaje, likes, tags, url')
    for proyecto in v:
        print(proyecto)


def determinar_estrellas(likes):
    stars = 1
    if 10.1 <= likes < 20.1:
        stars = 2
    elif 20.1 <= likes < 30.1:
        stars = 3
    elif 30.1 <= likes < 40.1:
        stars = 4
    elif likes >= 40.1:
        stars = 5
    return stars


def filtrado_x_tag(v, tag):
    v_tags = []
    for i in v:
        if tag in i.tags:
            v_tags.append(i)
    return v_tags


def mostrar_x_tags(v_tags, tag):
    print('\nListando proyectos con la etiqueta', tag, '\n')
    print('{:<20}'.format('Nombre de usuario ') +
          '{:<25}'.format('Fecha de actualiacion ') +
          '{:<15}'.format('Estrellas '))
    for i in v_tags:
        stars = determinar_estrellas(i.likes)
        proyecto = '{:<20}'.format(i.nombre_usuario)
        proyecto += '{:<25}'.format(i.fecha_actualizacion)
        proyecto += '{:<15}'.format('★' * stars)
        print(proyecto)


def grabar_registros(v, path_name='proyectos_filtrados.csv'):
    m = open(path_name, 'wt')
    m.write('nombre_usuario|repositorio|descripcion|fecha_actualizacion|lenguaje|estrellas|tags|url\n')
    for i in v:
        m.write(i.nombre_usuario + '|' +
                i.repositorio + '|' +
                i.fecha_actualizacion + '|' +
                i.lenguaje + '|' +
                str(i.likes) + 'k|' +
                ','.join(i.tags) + '|' +
                i.url + '\n')
    m.close()


def obtener_indice(v_leng, lenguaje):
    n = len(v_leng)
    indice = -1
    for i in range(n):
        if lenguaje == v_leng[i]:
            indice = i
            break
    return indice


def determinar_lenguajes(v):
    v_leng = []
    v_acum = []
    for i in v:
        indice = obtener_indice(v_leng, i.lenguaje)
        if indice == -1:
            v_leng.append(i.lenguaje)
            v_acum.append(1)
        else:
            v_acum[indice] += 1
    return v_leng, v_acum


def ordenar_x_lenguaje(v_leng, v_acum):
    n = len(v_leng)

    for i in range(n-1):
        for j in range(i+1, n):
            if v_acum[j] > v_acum[i]:
                v_acum[i], v_acum[j] = v_acum[j], v_acum[i]
                v_leng[i], v_leng[j] = v_leng[j], v_leng[i]


def mostrar_lenguajes_cantidad(v_leng, v_acum):
    n = len(v_leng)
    print('\nListando cantidad de proyectos por lenguaje\n')
    print('{:<20}'.format('Lenguaje') + 'Cantidad de proyectos')
    for i in range(n):
        print('{:<20}'.format(v_leng[i]) + str(v_acum[i]))


def determinar_mes(fecha):
    mes = int(fecha[5:7])
    return mes


def crear_martiz(v, matriz):
    for i in range(12):
        matriz.append([0] * 5)

    for i in v:
        stars = determinar_estrellas(i.likes) - 1
        mes = determinar_mes(i.fecha_actualizacion) - 1
        matriz[mes][stars] += 1


def obtener_num_mes(mes, meses):
    for j in range(len(meses)):
        if meses[j] == mes:
            mes = j
            break
    return mes


def recrear_matriz_popular(v, meses):
    matriz = []
    for i in range(12):
        matriz.append([0] * 5)
    for i in v:
        stars = determinar_estrellas(i.likes) - 1
        mes = obtener_num_mes(i.mes, meses)
        matriz[mes][stars] += 1
    return matriz


def mostrar_matriz(matriz, meses):
    fila = len(matriz)
    columna = len(matriz[0])
    star = '★'
    header = 'POPULARIDAD'

    for i in range(5):
        header += '{:>10}'.format(star * (i + 1))
    print(header)

    for i in range(fila):
        print('{:<20}'.format(meses[i]), end='')
        for j in range(columna):
            print('{:<10}'.format(matriz[i][j]), end=' ')
        print('\n')


def calcular_total_actualizados_mes(v, mes):
    n = len(v)
    acum = 0
    for i in range(n):
        fecha = determinar_mes(v[i].fecha_actualizacion)
        if fecha == mes:
            acum += 1
    return acum


def validar_mes(meses):
    msj = '\nVALOR MES\n'
    for i in range(12):
        msj += str(i+1) + ': ' + meses[i] + '\n'
    print(msj)

    mes = int(input('Ingrese el VALOR del mes que desea ver: '))
    while 1 > mes or mes > 12:
        mes = int(input('VALOR INCORRECTO!\nIngrese el VALOR del mes que desea ver: '))
    return mes


def validar_si_no(mensaje):
    n = int(input(mensaje + '(ESCRIBAR EL VALOR NUMERICO):' + '\n1:SI\n2:NO\n'))
    while 1 > n or n > 2:
        n = int(input(mensaje + '\n1:SI\n2:No\n'))
    return n


def buscar_repositorio(v, rep):
    n = len(v)
    indice = -1

    for i in range(n):
        if v[i].repositorio == rep:
            indice = i
            break
    return indice


def obtener_fecha():
    date = datetime.now()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)

    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    return year + '-' + month + '-' + day


def actualizar_campos(v, indice):
    user_name = input('Ingresa el nombre de usuario en github')
    repo = input('Ingresa el nombre del repositorio')
    v[indice].url = 'http://github.com/' + user_name + '/' + repo
    v[indice].fecha_actualizacion = obtener_fecha()


def grabar_binario(v, path_name='registros_populares.utn'):
    m = open(path_name, 'a+b')
    for i in v:
        pickle.dump(i, m)
    m.close()


def crear_vector_popular(vec, matriz, meses):
    fila = len(matriz)
    columna = len(matriz[0])

    for i in range(fila):
        for j in range(columna):
            cant_proyectos = matriz[i][j]
            if cant_proyectos != 0:
                reg = Popular(meses[i], j + 1, cant_proyectos)
                vec.append(reg)
                # print(reg)


def leer_binario(path_file='registros_populares.utn'):
    v = []
    if os.path.exists(path_file):
        m = open(path_file, 'rb')
        pos = os.path.getsize(path_file)
        while m.tell() < pos:
            registro = pickle.load(m)
            v.append(registro)
        m.close()
    return v


def principal():
    op = -1
    v = []
    vuelta = 0
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    press = 'Presione enter para continuar...'
    matriz = []
    v_popular = []

    while op != 8:
        vuelta += 1
        if op == 1:
            datos = cargar_archivo(v)
            if datos[0] == 0 and datos[1] == 0:
                print('La ruta del archivo no se encontro')
                input(press)
            else:
                print('Se cargaron', datos[0], 'registros exitosamente, y', datos[1], 'fueron omitidos.')
                input(press)

        elif 1 < op < 8:
            if len(v) == 0:
                input('Primero debe cargar los proyectos en memoria! ' + press)
            else:
                if op == 2:
                    tag = input('Ingrese la etiqueta a listar(TAG): ')
                    v_tags = filtrado_x_tag(v, tag)
                    if len(v_tags) != 0:
                        mostrar_x_tags(v_tags, tag)
                        res = validar_si_no('\nQuiere almacenar la lista en un archivo?')
                        if res == 1:
                            grabar_registros(v_tags)
                            input('Se grabaron ' + str(len(v_tags)) + ' registros. ' + press)
                    else:
                        input('Ningun proyecto tiene la etiqueta #' + tag + '. ' + press)
                elif op == 3:
                    v_leng, v_acum = determinar_lenguajes(v)
                    ordenar_x_lenguaje(v_leng, v_acum)
                    mostrar_lenguajes_cantidad(v_leng, v_acum)
                    input('\n' + press)

                elif op == 4:
                    crear_martiz(v, matriz)
                    mostrar_matriz(matriz, meses)
                    n = validar_si_no('\nDesea ver el total de proyectos actualizados en algun mes?')
                    if n == 1:
                        mes = validar_mes(meses)
                        total = calcular_total_actualizados_mes(v, mes)
                        print('El mes de', meses[mes-1], 'tiene un total de', total, 'proyectos actualizados.')

                elif op == 5:
                    rep = input('Ingrese el nombre del repositorio: ')
                    rep_indice = buscar_repositorio(v, rep)
                    if rep_indice != -1:
                        print('\nRepositorio encontrado!!!\n', v[rep_indice], '\nACTUALIZAR DATOS\n')
                        actualizar_campos(v, rep_indice)
                        print('\nProyecto actualizado!')
                        print(v[rep_indice])
                    else:
                        input('El repositorio no existe. ' + press)

                elif op == 6:
                    crear_vector_popular(v_popular, matriz, meses)
                    grabar_binario(v_popular)
                    print('Se ha grabado ')
                else:
                    v_archivo = leer_binario()
                    matriz_bin = recrear_matriz_popular(v_archivo, meses)
                    mostrar_matriz(matriz_bin, meses)
        elif vuelta > 1:
            input('El valor no corresponde a una opcion valida. ' + press)

        mostrar_menu()
        op = int(input('Ingrese opcion: '))

    print('Cerrando...')


if __name__ == '__main__':
    principal()
