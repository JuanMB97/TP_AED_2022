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


def principal():
    op = -1
    v = []
    vuelta = 0
    press = 'Presione enter para continuar...'

    while op != 8:
        vuelta += 1
        if op == 1:
            pass
        elif 1 < op < 8:
            if len(v) == 0:
                input('Primero debe cargar los proyectos en memoria! ' + press)
            else:
                if op == 2:
                    pass
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
            input('El valor no corresponde a una opcion valida. ' + press)

        mostrar_menu()
        op = int(input('Ingrese opcion por favor: '))

    print('Cerrando...')


if __name__ == '__main__':
    principal()