class SeriesReducido:
    def __init__(self, num, genero, cantidad):
        self.num = num
        self.genero = genero
        self.cantidad = cantidad

    def __str__(self):
        cadena = '{:<15}'.format('Numero: ' + str(self.num))
        cadena += '{:<30}'.format('Genero: ' + self.genero)
        cadena += '{:<25}'.format('Cantidad de series: ' + str(self.cantidad))
        return cadena
