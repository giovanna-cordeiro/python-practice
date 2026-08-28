pessoa = {'nome':'Giovanna', 
          'idade':20, 
          'ano_formatura':2027, 
          'linguagens_programacao':['python', 'Java', 'javascript', 'C', 'C#'], 
          'brasileira':True, 
          'hobby':['Ler', 'correr', 'Ver filmes'], 
          'animal_estimacao':True}

# Imprima na tela o valor equivalente a chave "hobby"
print(pessoa['hobby'])

# Imprima na tela uma lista apenas com os valores do dicionário
valores = list(pessoa.values())
print(valores)

# Imprima na tela uma lista apenas com as chaves do dicionário
chaves = list(pessoa.keys())
print(chaves)

# Insira um novo par chave-valor no dicionário
pessoa['altura'] = 1.65
print(pessoa['altura'])