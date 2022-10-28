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
        cadena = '{:<30}'.format('Link: ' + self.poster_link)
        cadena += '{:<30}'.format('Title: ' + self.series_title)
        cadena += '{:<30}'.format('Date: ' + self.runtime_of_series)
        cadena += '{:<30}'.format('Certificate: ' + self.certificate)
        cadena += '{:<30}'.format('Time: ' + self.runtime_of_episodes)
        cadena += '{:<30}'.format('Genre: ' + self.genre)
        cadena += '{:<30}'.format('Rating: ' + self.IMDB_rating)
        cadena += '{:<30}'.format('Overwiew: ' + self.overwiew)
        cadena += '{:<30}'.format('Votes: ' + self.not_of_vote)

