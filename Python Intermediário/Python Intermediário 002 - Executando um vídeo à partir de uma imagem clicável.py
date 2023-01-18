from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()


def first():
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


img_file = Image.open("I:\Imagens para programas\Diversas\dogdance.jpg")
img_file = img_file.resize((150, 150))
img = ImageTk.PhotoImage(img_file)
b1 = Button(canvas, image=img, command=first).pack()


root.mainloop()
