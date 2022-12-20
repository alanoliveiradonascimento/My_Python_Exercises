#from tkinter import *
#from ttkbootstrap.constants import *
import ttkbootstrap as ttkb

#themename no TTK Bootstrap são temas já existentes na biblioteca.
# Ver mais em: https://ttkbootstrap.readthedocs.io/en/latest/themes/
# Os temas existentes no momento são:
# Temas light: cosmo, flatly, journal, litera, lumen, minty, pulse, sandstone, united,
#              yeti, morph, simplex, cerculean,
#Temas Dark (do mais claro ao mais escuro): solar, superhero, darkly, cyborg, vapor

root = ttkb.Window(themename="darkly")

root.title("TTK BootStrap!")
root.iconbitmap('python.ico')
root.geometry('500x300')

counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="Hello World!")
    else:
        my_label.config(text="Goodbye World!")

# Temas bootstyle: primary, secondary, success, info, warning, danger, light e dark.
# Aqui é possível, também, inverter as cores do label com o comando inverse.
# sintaxe: bootstyle="success, inverse"
my_label = ttkb.Label(text="Hello World!", font=("Helvetica", 28), bootstyle="danger")
my_label.pack(pady=50)

# No caso dos botões o comando outline deixa o botão com uma animação responsiva ao passar o mouse por ele.
# Se no lugar de outline colocarmos o comando "link" o botão fica com a aparência de um link.
my_button = ttkb.Button(text="Botão", bootstyle="success, outline", command=changer)
my_button.pack()

root.mainloop()
