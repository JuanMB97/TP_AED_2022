import os.path
from Proyecto import *


def mostrar_menu():
    print('\n=== MENÚ ===\n'
          '1) Cargar proyectos\n'
          '2) Mostrar proyectos que contengan cierta etiqueta (TAG)\n'
          '3) Lenguajes\n'
          '4) Popularidad\n'
          '5) Buscar proyecto actualizado\n'
          '6) Guardar populares\n'
          '7) Mostrar archivo\n'
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
    if campos[4] == "":
        res = False

    # Si el campo lenguaje no viene vacio, verificar si el proyecto ya existe en el vector a traves del URL.
    if res:
        for i in v:
            if campos[7] == i.url:
                res = False
    return res


def cargar_archivo(v, path_file="proyectos.csv"):
    # Datos es un vector con dos valores → 0: Cantidad de proyectos cargados 1: Cantidad de proyectos omitidos
    datos = [0] * 2

    if os.path.exists(path_file):
        nro_linea = 0
        m = open(path_file, mode="rt", encoding="utf8")
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
                tags = campos[6].split(",")
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
    print("\nListando proyectos con la etiqueta", tag, "\n")
    print('{:<20}'.format("Nombre de usuario ") +
          '{:<25}'.format("Fecha de actualiacion ") +
          '{:<15}'.format("Estrellas "))
    for i in v_tags:
        stars = determinar_estrellas(i.likes)
        proyecto = '{:<20}'.format(i.nombre_usuario)
        proyecto += '{:<25}'.format(i.fecha_actualizacion)
        proyecto += '{:<15}'.format("★" * stars)
        print(proyecto)


def grabar_registros(v):
    pass


def principal():
    op = -1
    v = []
    vuelta = 0
    press = "Presione enter para continuar..."
    while op != 8:
        vuelta += 1
        if op == 1:
            datos = cargar_archivo(v)
            if datos[0] == 0 and datos[1] == 0:
                print("La ruta del archivo no se encontro")
                input(press)
            else:
                print("Se cargaron", datos[0], "registros exitosamente, y", datos[1], "fueron omitidos.")
                input(press)
        elif 1 < op < 8:
            if len(v) == 0:
                input("Primero debe cargar los proyectos en memoria!")
            else:
                if op == 2:
                    tag = input("Ingrese la etiqueta a listar(TAG)")
                    v_tags = filtrado_x_tag(v, tag)
                    mostrar_x_tags(v_tags, tag)
                    res = input("\nQuiere almacenar la lista en un archivo? \n1: Si \n2: No\n")
                    if res == 1:
                        grabar_registros(v_tags)
                elif op == 3:
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
            input("El valor no corresponde a una opcion valida. " + press)

        mostrar_menu()
        op = int(input('Ingrese opcion: '))

    print("Cerrando...")


if __name__ == '__main__':
    principal()
