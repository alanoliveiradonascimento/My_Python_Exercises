# Importa o Tkinter
from tkinter import *

# Importa Tkvideo
from tkvideo import *

# Importa a biblioteca Video File Clip dentro de moviepy
from moviepy.editor import VideoFileClip

# Criando uma instância Tkinter
janela = Tk()

# Tamanho da Janela
janela.geometry('550x650')

# Não Deixa o tamanho ser alterado
janela.resizable(False, False)

# Criação de uma Label
minha_label = Label()
minha_label.place(x=50, y=50)

# Criação do clip que será aplicado dentro da Label
clip = VideoFileClip('Brazilian dog dancing - Hilarious.mp4')

# Variável que será responsável por rodar a imagem dentro do Label
player = TkVideo(clip, minha_label, loop=50, size=(450, 550))
player.play()

janela.mainloop()
