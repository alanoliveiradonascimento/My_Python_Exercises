# Importa a biblioteca colorama
import colorama

# Importa da biblioteca colorama: Fore: Cor da letra / Back: Background
from colorama import Fore, Back

# Realiza o reset dos padrões de cores do terminal e reinicia utilizando os do colorama
colorama.init(autoreset=True)

# Lista com usuário e senha
credenciais = ['alan', '123456']

# Variáveis que receberão nome e senha
nome = str(input('Digite seu nome: '))
senha = str(input('Digite sua senha: '))

# Estrutura condicional para validar o login
if nome == 'admin' and senha == 'admin':
    print(Back.GREEN + Fore.BLACK + "Usuário autenticado com sucesso!")
    print(Back.CYAN + Fore.BLACK + "Você está iniciando uma sessão como Administrador")

elif nome =='alan' and senha == '123456':
    print(Back.GREEN + Fore.BLACK + "Usuário autenticado com sucesso!")
    print(Back.CYAN + Fore.BLACK + f"Seja bem vindo {nome}!")

else:
    print(Back.RED + Fore.BLACK + 'Atenção!')
    print(Back.RED + Fore.BLACK + 'Digite um usuário ou senha válidos!')
