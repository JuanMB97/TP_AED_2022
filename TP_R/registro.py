class Series:
    def __init__(self, link, title, date, certificate, time, genre, rating, resumen, votos):
        self.poster_link = link
        self.series_title = title
        self.runtime_of_series = date
        self.certificate = certificate
        self.runtime_of_episodes = time
        self.genre = genre
        self.IMDB_rating = rating
        self.overwiew = resumen
        self.not_of_vote = votos

    def __str__(self):
        cadena = '{:<80}'.format('Link: ' + self.poster_link)
        cadena += '{:<30}'.format('\nTitle: ' + self.series_title)
        cadena += '{:<15}'.format('\nDate: ' + self.runtime_of_series)
        cadena += '{:<15}'.format('\nCertificate: ' + self.certificate)
        cadena += '{:<15}'.format('\nTime: ' + str(self.runtime_of_episodes))
        cadena += '{:<15}'.format('\nGenre: ' + str(self.genre))
        cadena += '{:<15}'.format('\nRating: ' + self.IMDB_rating)
        cadena += '{:<30}'.format('\nOverwiew: ' + self.overwiew)
        cadena += '{:<10}'.format('\nVotes: ' + str(self.not_of_vote) + "\n")
        return cadena
