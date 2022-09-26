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
        cadena = '\nuser: ' + self.nombre_usuario + "\n"
        cadena += 'repo: ' + self.repositorio + "\n"
        cadena += 'last-update: ' + self.fecha_actualizacion + "\n"
        cadena += 'language: ' + self.lenguaje + "\n"
        cadena += 'likes: ' + str(self.likes) + "k\n"
        cadena += 'tags: ' + ','.join(self.tags) + "\n"
        cadena += 'url: ' + self.url + "\n"
        return cadena

