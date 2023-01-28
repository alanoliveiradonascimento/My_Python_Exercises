from tkinter import *
import ttkbootstrap as ttkb
from PIL import Image, ImageTk


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


janela_principal = ttkb.Window(themename='darkly', iconphoto='none', title='Movie Center')
janela_principal.iconbitmap('img/mvredicon.ico')

img_file = Image.open("I:\Imagens para programas\Diversas\dogdance.jpg")
img_file = img_file.resize((120, 150))
img = ImageTk.PhotoImage(img_file)
b1 = Button(janela_principal, image=img, command=first).place(x=50, y=50)

janela_principal.mainloop()
