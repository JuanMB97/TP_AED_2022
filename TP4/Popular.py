class Popular:
    def __init__(self, mes, estrellas, cant_proyectos):
        self.mes = mes
        self.estrellas = estrellas
        self.cant_proyectos = cant_proyectos

    def __str__(self):
        cadena = '{:<20}'.format('Mes: ' + self.mes)
        cadena += '{:<15}'.format('Estrellas:' + str(self.estrellas))
        cadena += 'Cantidad de proyectos:' + str(self.cant_proyectos)
        return cadena
