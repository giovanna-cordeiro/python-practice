resumo = "Giovanna é uma mulher de 20 anos que estuda Ciência da Computação e está aprendendo 'Python'."

# Imprima na tela a variável "resumo"
print(resumo)

# Imprima na tela apenas a segunda letra da variável
print(resumo[1])

# Imprima na tela a idade de Giovanna (resposta esperada: "20")
print(resumo[25:27])

# Imprima na tela o trecho final da variável

print(resumo[32:])
# Converta todos as letras para minúsculo e imprima na tela
print(resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela
print(resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela

print(resumo.title())
# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print(resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
idade = 20
print(f"Giovanna é uma mulher de {idade} anos que estuda Ciência da Computação e está aprendendo 'Python'.")