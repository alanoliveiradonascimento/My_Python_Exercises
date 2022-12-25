# Importando a biblioteca Tkinter
from tkinter import *

# Importando o módulo messagebox dentro do Tkinter: Ver mais em: https://www.educba.com/tkinter-messagebox/
from tkinter import messagebox

# Importando a biblioteca "os". Importa comportamentos do Sistema Operacional.
# Neste nosso caso usaremos na configuração do botão sair.
import os

# Lista de opções possíveis no programa
options = ["1", "2", "3", "4", "01", "02", "03", "04"]


# Classe com as definições do programa
class MinhaJanela:
    def __init__(self, janela):  # Indentada
        #Configuração dos Widgets texto(Label), entrada(Entry) e botões(Button)
        self.texto_01 = Label(janela, text="Escolha uma cor: 01 / 02 / 03 / 04",
                              font="Lucida 20 bold",
                              bg="#363636", fg="white")
        self.entrada = Entry(janela, bd=3,
                             width=35,
                             justify=LEFT)
        self.botao_01 = Button(janela, text="Trocar Cor de Fundo",
                               font="Helvetica 14 bold",
                               command=self.change_color)  # Change to self.change_color
        self.botao_02 = Button(janela, text="Sair",
                               font="Arial 14 bold",
                               command=sair)

        # Posicionamento dos Widgets na janela.
        self.texto_01.place(x=35, y=30)
        self.entrada.place(x=140, y=80, height=30)
        self.botao_01.place(x=140, y=120)
        self.botao_02.place(x=220, y=165, height=30)


    # Função alterar cor
    def change_color(self):  # Indentada
        cor = (self.entrada.get())
        if cor == "1" or cor == "01":
            janela.config(bg="green")
        if cor == "2" or cor == "02":
            janela.config(bg="red")
        if cor == "3" or cor == "03":
            janela.config(bg="yellow")
        if cor == "4" or cor == "04":
            janela.config(bg="purple")
        if cor not in options:
            messagebox.showwarning("Atenção", "Escolha apenas os números informados!")


# Função do botão sair
def sair():   # Sem indentação
    os._exit(0)


# Crianção da Janela
janela = Tk()

# Declarando a janela para que a classe a reconheça
minhajanela = MinhaJanela(janela)

# Título da Janela
janela.title("Teste de janela com widget")

# Desativando a opção de mudar o tamanho da janela. Se alterar para "True" habilita a opção.
janela.resizable(False, False)

# Cor de fundo da janela
janela.configure(bg="#363636")

# Definição de posicionamento da janela

# Tamanho da janela
largura = 500
altura = 300

# Buscando largura e altura do monitor em uso
largura_do_monitor = janela.winfo_screenwidth()
altura_do_monitor = janela.winfo_screenheight()

# Cálculo do posicionamento centralizado da janela em relação ao monitor
posx = largura_do_monitor / 2 - largura / 2
posy = altura_do_monitor / 2 - altura / 2
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# “Loop” para manter a janela aberta
janela.mainloop()
