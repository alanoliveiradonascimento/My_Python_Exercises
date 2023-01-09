# Importante este exercício deve ser feito utilizando o Jupyter Notebook para melhor aproveitamento
# No meu caso este exercício foi feito no VSCode

# Importando a bibilioteca para criação de mapas
import folium

# Variável com as 7 maravilhas do mundo antigo
sete_maravilhas_nomes = ['Grande Pirâmide de Gizé',
                         'Jardins Suspensos da Babilônia',
                         'Templo de Ártemis',
                         'Estátua de Zeus em Olímpia',
                         'Mausoléu de Halicarnasso',
                         'Colosso de Rodes',
                         'Farol de Alexandria']

# Variável com as coordenadas das 7 maravilhas (altitude e longitude)
sete_maravilhas_coordenadas = [[29.978, 31.1344],
                               [32.531, 44.455],
                               [37.9455, 27.3913],
                               [37.6336, 21.6575],
                               [37.0336, 27.4516],
                               [36.4468, 28.2553],
                               [31.2094, 29.913]]

# Dentro de 'Map' a primeira coisa a ser informada é o ponto central do mapa.
# Neste exemplo a primeira coordenada será o ponto central (location)
# O parâmetro zoom mostra o quão próximo ou quão afastado está o mapa
# "control scale" mostra a escala no rodapé da janela
# "tiles" mostra o tipo de mapa

sete_maravilhas_mapa = folium.Map(location=[29.978, 31.1344],
                                   zoom_start=5,
                                   control_scale=True,
                                   tiles='cartodbpositron')


# Adicionar as 7 maravilhas ao mapa
# item i dentro da lista sete_maravilhas_coordenadas
for i in range(len(sete_maravilhas_coordenadas)):
    # A coordenada dentro da lista sete_maravilhas_coordenadas
    coordenada = sete_maravilhas_coordenadas[i]
    # O nome dentro da lista sete_maravilhas_nomes
    maravilha = sete_maravilhas_nomes[i]
    # folium.Marker - Mostra no mapa as 7 maravilhas (pins)
    # popup: mostra os nomes das maravilhas nos pins ao clicar sobre
    # icon=folium.Icon: altera os ícones dos pins em uso no mapa: ver mais: "getbootstrap.com/docs/3.3/components/"
    folium.Marker(coordenada, popup=maravilha, icon=folium.Icon(icon='glyphicon glyphicon-camera',
                                                                color='black',
                                                                icon_color='white',
                                                                prefix='glyphicon')).add_to(sete_maravilhas_mapa)

# Mostra latitude e longitude ao clicar
sete_maravilhas_mapa.add_child(folium.LatLngPopup())

# Salva o mapa em um arquivo HTML dentro da pasta do programa
sete_maravilhas_mapa.save("sete_maravilhas.html")

