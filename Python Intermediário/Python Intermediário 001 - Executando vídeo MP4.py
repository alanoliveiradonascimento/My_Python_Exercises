class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"

movie = Movie_MP4(r"I:\Imagens para programas\Projetos com Vídeo\Brazilian dog dancing - Hilarious.mp4")
movie.play()
