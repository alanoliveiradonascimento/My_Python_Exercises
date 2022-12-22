from tkinter import *
import customtkinter as ctk

root = Tk()
root.title('Teste CTK')
root.geometry("450x250")
root.configure(background="light grey")


def clicou():
    print("Clicou, né!?")


botao = ctk.CTkButton(text="Clica aí!", command=clicou)
botao.pack(anchor=CENTER, pady=100)

root.mainloop()
