#Vamos adicionar um Label a uma janela com Tkinter.

#Importando o módulo Tkinter
from tkinter import *

#Criação de uma instância de frame ou janela do Tkinter. Pode ter qualquer nome do lugar de "root"
root = Tk()

#Configuração de "geometria", tamanho do frame ou janela do Tkinter.
#No caso abaixo "750" corresponde à largura e "250" à altura.
root.geometry("750x250")

#Criação de um Widget de Label(texto). Pode ter qualquer nome no lugar de "texto"
#Dentro de "Label" vai a referência à qual janela ele aparecerá: root.
#O texto que será mostrado na janela: "Esse é um Widget de Label!"
#A fonte e tamanho da fonte do texto que será exibido: Fonte: Arial, Tamanho: 20
texto = Label(root, text="Esse é um Widget de Label!", font='Arial 20')
#Pack é o método que irá inserir o Lable texto no frame ou janela.
texto.pack()

#Loop que mantém a janela aberta. Sem isso a janela se abre e fecha antes de ser mostrada na tela.
root.mainloop()
