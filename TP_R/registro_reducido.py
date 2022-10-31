class SeriesReducido:
    def __int__(self, num, genero, cantidad):
        self.num = num
        self.genero = genero
        self.cantidad = cantidad

    def __str__(self):
        cadena = '{:<15}'.format('Numero: ' + self.num)
        cadena += '{:<15}'.format('Numero: ' + self.genero)
        cadena += '{:<15}'.format('Numero: ' + str(self.cantidad))
        return cadena
