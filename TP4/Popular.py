class Popular:
    def __init__(self, mes, estrellas, cant_proyectos):
        self.mes = mes
        self.likes = estrellas
        self.cant_proyectos = cant_proyectos

    def __str__(self):
        cadena = '{:<20}'.format('Mes: ' + self.mes)
        cadena += '{:<15}'.format('Estrellas:' + str(self.likes))
        cadena += 'Cantidad de proyectos:' + str(self.cant_proyectos)
        return cadena
