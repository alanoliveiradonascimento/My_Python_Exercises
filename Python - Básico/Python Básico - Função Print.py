# Função Print
# Sintaxe: print(objeto, argumentos_de_palavra-chave)
# Argumentos de palavra-chave:
#      sep='separador' - Especifica como os objetos serão separados, se houver mais do que um.
#                        Por padrão é um espaço em branco.
#      end='caractere' - Especifica o caractere que é impresso no final da linha.
#                        O padrão é uma quebra de linha (\n).
#      file - Especifica um objeto com um método write, com um arquivo.
#             O padrão é o dispositivo sys.stdout (saída padrão / a tela).
#      flush - Valor booleno que especifica se a saída é eliminada (True) ou gravada em buffer (False).
#              O padrão é False.

# Exemplo 01 - print(variável) - Imprime o valor de uma variável.

a = 30
print(a)

# exemplo 01.1 - sep adicionará o que for informado dentro das aspas como separador entre os objetos informados.
# print("texto", "texto", sep="nada ou qualquer coisa aqui dentro")

print("carro", "casa", "barco", sep="-")

# exemplo 01.2 - end adicionará o que for informado dentro das aspas após os objetos informados.
# print("texto", "texto", end="nada ou qualquer coisa aqui dentro")
print("carro", "casa", "barco", end="-")


# Exemplo 02 - Tipos de conversão (formatação)
# %s - Substitui %s pela variável que está fora das aspas, após o outro %. Sintaxe: print("texto %s" % variável)

a = "pizza"
print("Gosto de %s" % a)

# Tabela de exemplos de uso do %:
# %d - Converte para decimal inteiro.
# %f - Converte para decimal flutuante.
# %o - Converte para octal
# %x - Converte para hexadecimal (minúscula)
# %X - Converte para hexadecimal (maiúscula)
# %c - Exibe 1 caracter
# %s - Converte para string

# Exemplo 03 - Tipos de formatação - Multiplas substituições.

a = "pizza"
b = 50
print("A %s custa R$ %d" % (a, b))

# Exemplo 04 - Método str.format
# sintaxe 01: print("texto {variável 01} texto {variável 02}.".format(variável 01, variável 02))

x = "carro"
y = "amarela"
print("Não curto {} com a cor {}.".format(x, y))

# sintaxe 02: print("texto {posição 0} texto {posição 1}.".format(variável 01, variável 02))
# Nesta caso se invertermos o ídice (0 e 1) o conteúdo do {} também muda.

x = "não"
y = "sim"
print("O {0} eu já tenho. O {1} depende de mim.".format(x, y))

# sintaxe 03: print(f"texto {variável 01} texto {variável 02}.")

x = "feijão"
y = "arroz"
print(f"Prefiro {x} com {y}.")

