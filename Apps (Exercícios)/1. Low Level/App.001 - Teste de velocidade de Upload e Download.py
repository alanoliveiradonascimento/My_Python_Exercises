# Importando "math" para calcular a conversão de bytes para megabytes;
import math

# Importando "speedtest" para o teste própriamente dito.
# Obs.: Para este exercício: 1 - Não instalar o módulo speedtest;
#                            2 - Instalar apenas o módulo speedtest-cli (pip install speedtest-cli)
#                            3 - Caso esteja com erro no "speedtest.Speedtest" será necessário desinstalar
#                                o "speedtest" sem o cli. (pip unistall speedtest).
import speedtest


# O speedtest retorna os valores de upload e download em bytes, o que gera um nº gigante.
# Criaremos uma Classe que irá converter byte para megabyte.
def byte_para_mb(tamanho_em_byte):
    # Variável pra evitar overflow no cálculo
    qualquer_nome_uma_variavel_qualquer = int(math.floor(math.log(tamanho_em_byte, 1024)))
    # Conversão para megabyte
    potencia = math.pow(1024, qualquer_nome_uma_variavel_qualquer)
    # Arredondamento
    tamanho = round(tamanho_em_byte / potencia, 2)
    # Máscara com a informação "Mbps"
    return f"{tamanho} Mbps"


internet = speedtest.Speedtest()

print("Calculando velocidade de Upload...")
intenet_upload = internet.upload() # Faz o teste de upload em tempo real.

print("Calculando velocidade de Download...")
internet_download = internet.download() # Faz o teste de download em tempo real.

#Mostra os valores coletados de upload e download.
print("Upload:  ", byte_para_mb(intenet_upload))
print("Download: ", byte_para_mb(internet_download))
