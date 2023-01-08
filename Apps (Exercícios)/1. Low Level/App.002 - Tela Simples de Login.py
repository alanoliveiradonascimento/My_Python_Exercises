# Importando a biblioteca Tkinter
from tkinter import *

# Importando a biblioteca de caixas de mensagem
import messagebox

# Lista contendo usuário e senha
credenciais = ['alan', '123456']

# Função de validação do Login:
def validar():
    # Pega o valor da Entry nome e atribui à variável nome
    nome = entrada_nome.get()
    # Pega o valor da Entry senha e atribui à variável senha
    senha = entrada_senha.get()

    # Compara se o nome e senha digitados equivalem aos valores válidos: admin e admin
    if nome == 'admin' and senha == 'admin':
        # Se verdadeiro mostra uma caixa de mensagem com a mensagem abaixo
        messagebox.showinfo("Login", "Você está iniciando \numa sessão como \nAdministrador")

    # Compara se o nome e senha digitados equivalem aos valores existentes na lista credenciais
    elif credenciais[0] == nome and credenciais[1] == senha:
        # Se verdadeiro mostra uma caixa de mensagem com a mensagem abaixo
        messagebox.showinfo("Login", "Seja bem vindo " + credenciais[0])

    # Se falso mostra uma caixa de mensagem com a mensagem abaixo
    else:
        messagebox.showwarning("Erro", "Senha ou login inválidos")


# Configurações da janela: Ícone, título, se pode ou não redimensionar, tamanho e posição na tela.
janela = Tk()
janela.iconbitmap("python.ico")
janela.title("App Teste")
janela.resizable(False, False)
largura = 450
altura = 250

largura_monitor = janela.winfo_screenwidth()
altura_monitor = janela.winfo_screenheight()
posx = largura_monitor / 2 - largura / 2
posy = altura_monitor / 2 - altura / 2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# Atributos dos Labels, Entrys e do Button
texto_01 = Label(text='Digite seu nome: ', font='arial 14 bold')
entrada_nome = Entry(bd=3, width=30)
texto_02 = Label(text='Digite sua senha: ', font='arial 14 bold')
entrada_senha = Entry(bd=3, width=30, show="*")
botaook = Button(text="Confirmar", font="arial 14 bold", command=validar)

# Posicionamento na tela dos Labels, Entrys e do Button
texto_01.place(x=10, y=50)
entrada_nome.focus()
entrada_nome.place(x=180, y=55)
texto_02.place(x=10, y=100)
entrada_senha.place(x=180, y=100)
botaook.place(x=180, y=155, width=110, height=35)

# Loop para manter a janela aberta
janela.mainloop()