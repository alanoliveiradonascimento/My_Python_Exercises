# Vamos explorar algumas configurações da janela (frame)

from tkinter import *

# Uma forma de alterar o título da janela é passar o parâmetro: frame = Tk(className='Nome da janela').
# Mas não considero a melhor forma de fazermos isso.

frame = Tk()

# Considero o "title" uma forma melhor de atribuir nomes à janela.
frame.title("Minha janela de testes")

# .config(bg = '') podemos configurar a cor de fundo utilizando cores sólidas apenas informando o nome da cor
# Ou informando o código HEX da cor que se deseja usar
# Para mais: https://imagecolorpicker.com/color-code/27677d

frame.config(bg='yellow')

# Tamanho da Janela
frame.geometry('500x250')

# .resazable: Ativa (True) ou desativa (False) a opção de alterar o tamanho da janela com o mouse.
# O primeiro False desativa na horizontal e o segundo na vertical.
frame.resizable(False, False)

frame.mainloop()
