from tkinter import *
import customtkinter as ctk
import math
import speedtest

janela = Tk()
janela.title("Teste de velocidade com Tkinter")
janela.iconbitmap("python.ico")
janela.resizable(False, False)
janela.geometry("500x250")



def byte_para_mb(tamanho_em_byte):
    # Variável pra evitar overflow no cálculo
    qualquer_nome_uma_variavel_qualquer = int(math.floor(math.log(tamanho_em_byte, 1024)))
    # Conversão para megabyte
    potencia = math.pow(1024, qualquer_nome_uma_variavel_qualquer)
    # Arredondamento
    tamanho = round(tamanho_em_byte / potencia, 2)
    # Máscara com a informação "Mbps"
    return f"{tamanho} Mbps"


def testar():

    internet = speedtest.Speedtest()


    print("Calculando velocidade de Upload...")
    intenet_upload = internet.upload()  # Faz o teste de upload em tempo real.


    print("Calculando velocidade de Download...")
    internet_download = internet.download()  # Faz o teste de download em tempo real.


    # Mostra os valores coletados de upload e download.
    print("Upload:  ", byte_para_mb(intenet_upload))
    print("Download: ", byte_para_mb(internet_download))
    upload = f''' Upload: {byte_para_mb(intenet_upload)} '''
    download = f''' Download: {byte_para_mb(internet_download)} '''

    resultado_upload["text"] = upload
    resultado_download["text"] = download


texto_1 = Label(janela,
                text="Clique no botão para testar \na velocidade da sua conexão!",
                font="Colibri 12 bold")

texto_1.pack(padx=10, pady=10)

resultado_upload = Label(janela,
                         text="",
                         font="Colibri 12 bold")
resultado_upload.pack(padx=10, pady=5)

resultado_download = Label(janela,
                           text="",
                           font="Colibri 12 bold")
resultado_download.pack(padx=10, pady=5)

testador = ctk.CTkButton(janela,
                         text="Testar",
                         command=testar)
testador.pack(anchor=CENTER, pady=10)

janela.mainloop()
