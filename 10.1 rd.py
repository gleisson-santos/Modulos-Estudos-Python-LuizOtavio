import random
import string

# Gera um número inteiro entra A e B
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um número de ponto flutuante entra A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Banana', 'Casa', 'Barco', 'Rosa', 'Pedr', 'Baú', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 1)
# sorteio = random.choices(lista, k=2)
# sorteio = random.choice(lista)


lista = ['Banana', 'Casa', 'Barco', 'Rosa', 'Pedra', 'Baú', 'Celular']

# Filtra os valores a partir do terceiro item que contêm "sa" na lista
valores_filtrados = [valor for valor in lista[2:] if "sa" in valor]

# Seleciona aleatoriamente um valor da lista filtrada
sorteio2 = random.choice(valores_filtrados)

#print(sorteio2)



# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
