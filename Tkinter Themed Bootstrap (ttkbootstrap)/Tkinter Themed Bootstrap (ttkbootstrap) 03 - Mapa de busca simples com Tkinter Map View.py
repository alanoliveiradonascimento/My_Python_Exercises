# Importando Tkinter Map View: "https://github.com/TomSchimansky/TkinterMapView#create-position-markers"
from tkintermapview import TkinterMapView

# Importando Tkinter Bootstrap: "https://ttkbootstrap.readthedocs.io/en/latest/"
import ttkbootstrap as ttkb


# Função que pega o texto digitado e ao clicar no botão altera o valor da variável busca.
def buscar():
    busca = entrada01.get()
    map_widget.set_address(busca, marker=True)


# Parâmetros para criação da janela com ttkbootstrap como ttkb
janela = ttkb.Window(themename="superhero")
janela.title("Mapa com Busca")
janela.resizable(False, False)

# Definição do tamanho e posicionamento da janela
largura = 518
altura = 550
largura_monitor = janela.winfo_screenwidth()
altura_monitor = janela.winfo_screenheight()
posx = largura_monitor / 2 - largura / 2
posy = altura_monitor / 2 - altura / 2
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# Criação dos widgets Label, Entry e Button
texto01 = ttkb.Label(text="Digite a localidade: ", font='lucida 12 bold', style='default')
texto01.place(x=17, y=22)
entrada01 = ttkb.Entry(font="lucida 12 bold", bootstyle='light')
entrada01.focus()
entrada01.place(x=177, y=19)
botao_ok = ttkb.Button(janela, text='Buscar', style='primary-outline', command=buscar)
botao_ok.configure(width=15)
botao_ok.place(x=382, y=20)

# Criação do widget de map
map_widget = TkinterMapView(janela, width=480, height=450, corner_radius=0)
map_widget.place(x=17, y=80)

# Servidor padrão do servidor
map_widget.set_tile_server("https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}", max_zoom=15)

# Posição inicial do mapa
map_widget.set_address("São joão de Meriti")

marcador = map_widget.set_marker(-22.80223, -43.37079, text='São João de Meriti')

janela.mainloop()
