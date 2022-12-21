# Importando a Biblioteca Tkinter
from tkinter import *

# Importando o pacote Ttk da biblioteca Tkinter
from tkinter import ttk

# Criando uma instância de frame ou janela do Tkinter
win = Tk()

# Configurando a "geometria" da janela do Tkinter
win.geometry("750x250")


# Definindo a função para alterar o texto da janela
def change_text():
    label.configure(text="Welcome")


# Criando um Label
label = Label(win, text="Click the below button to Change this Text", font= 'Arial 20 bold')
label.pack(pady=30)

# Criando um widget Button
button = ttk.Button(win, text="Commit", command=lambda: change_text())
button.pack()

win.mainloop()
