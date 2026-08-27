# Crie uma lista apenas com elementos numéricos
numeros = [1,2,3,4,5,6,7,8,9,10,10.5]
print(numeros)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
elementos = [10, 'Giovanna', [1,2,3,5],2010,'r',True, False]
print(elementos)
# Imprima na tela apenas os 5 primeiros elementos da lista
print(numeros [0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_indice_Par = numeros[::2]
print(elementos_indice_Par)
# Remova da lista o último item
elementos.pop()
print(elementos)
# Insira na lista um novo item
elementos.append('Dados')
print(elementos)

# Remova da lista um item específico
elementos.remove('r')
print(elementos)

#Subistitua um item da lista elementos 

elementos[1] = 'Alice'
print(elementos)