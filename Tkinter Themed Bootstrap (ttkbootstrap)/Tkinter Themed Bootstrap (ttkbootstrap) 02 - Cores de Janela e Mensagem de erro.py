# Importando TTk Bootstrap
import ttkbootstrap as ttkb

# Importando o módulo messagebox dentro do Tkinter: Ver mais em: https://www.educba.com/tkinter-messagebox/
from tkinter import messagebox

# Importando a biblioteca "os". Importa comportamentos do Sistema Operacional.
# Neste nosso caso usaremos na configuração do botão sair.
import os

# Lista com as opções a serem escolhidas
options = ["1", "2", "3", "01", "02", "03"]


# Classe com as definições do programa
class MinhaJanela:
    def __init__(self, janela):  # Indentada
        #Configuração dos Widgets texto(Label), entrada(Entry) e botões(Button) com TTk Bootstrap
        self.texto_01 = ttkb.Label(janela,
                                   text="Escolha uma cor: 01 / 02 / 03 / 04",
                                   font=("Helvetica", 20, "bold"),
                                   bootstyle="light")
        self.entrada = ttkb.Entry(janela,
                                  width=35,
                                  bootstyle="light")
        self.botao_01 = ttkb.Button(janela,
                                    text="Trocar Cor de Fundo",
                                    bootstyle="success, outline",
                                    command=self.change_color)
        self.botao_02 = ttkb.Button(janela,
                                    text="Sair",
                                    bootstyle="danger, outline",
                                    command=sair)

        # Posicionamento dos Widgets na janela.
        self.texto_01.place(x=35, y=30)
        self.entrada.place(x=140, y=80, height=30)
        self.botao_01.place(x=185, y=120, height=30)
        self.botao_02.place(x=215, y=165, height=30, width=70)

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


# Criando a Janela. Obs.: ttkb.Window aqui é com "W" maiúsculo.
# Ver mais em: https://ttkbootstrap.readthedocs.io/en/latest/themes/
janela = ttkb.Window(themename="superhero")

# Ícone no topo da Janela
janela.iconbitmap('python.ico')

# Declarando a janela para que a classe a reconheça
minhajanela = MinhaJanela(janela)

# Título da Janela
janela.title("Teste de janela TTKB com widget")

# Desativando a opção de mudar o tamanho da janela. Se alterar para "True" habilita a opção.
janela.resizable(False, False)

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
