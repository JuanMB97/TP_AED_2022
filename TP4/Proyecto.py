
class Proyecto:
    def __init__(self, nombre_usuario, repositorio, fecha_actualizacion, lenguaje, likes, tags, url):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url

    def __str__(self):
        cadena = '{:<24} {:<60} {} {:<20} {:<5} {:<330} {}'
        return cadena.format(self.nombre_usuario,
                             self.repositorio,
                             self.fecha_actualizacion,
                             self.lenguaje,
                             self.likes,
                             self.tags,
                             self.url)
