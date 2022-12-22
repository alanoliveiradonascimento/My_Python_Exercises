# Importando Tkinter
from tkinter import *
# Importando customtkinter e atribuindo um "apelido" ctk
import customtkinter as ctk

# Configuração de janela do Tkinter: Quem é a janela, Título da janela, dimensões e cor de fundo.
root = Tk()
root.title('Teste CTK')
root.geometry("450x250")
root.configure(background="light grey")


# Função para mostrar no terminal se o botão foi clicado
def clicou():
    print("Clicou, né!?")


# Widget Button do CTK
botao = ctk.CTkButton(text="Clica aí!", command=clicou)
botao.pack(anchor=CENTER, pady=100)

root.mainloop()
