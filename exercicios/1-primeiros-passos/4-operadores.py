ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade = ano_formatura - ano_nascimento
print(idade)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_formatura>ano_nascimento) # maior que 
print(ano_nascimento!=ano_formatura) # diferente de 
print(ano_nascimento<=ano_formatura) # menor ou igual a 
print(ano_formatura==ano_nascimento) # igual a 

 
# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((ano_nascimento<ano_formatura)and(ano_formatura>ano_nascimento)) #and compara se as duas são verdadeiras ao mesmo tempo
print((ano_nascimento<=ano_formatura)or (ano_nascimento>ano_formatura)) #or vê se uma delas é verdadeira 
print(not(ano_nascimento==ano_formatura)) # not mostra se o contrário dessa operação é verdadeiro 

#Teste
atividade = 'Giovanna' + ' ' + 'estuda' + ' ' + 'Python' # soma strings e o ' ' adiciona espaço entre as palavras 
print(atividade)
nome = 'Giovanna'
print((nome + ' ') * 7) # imprime a variável "nome" com um espaço entre as palavras 7 vezes

#Divisão

divisao = 1900/17
print(divisao)

#Divisão inteira

divisao_inteira = 1900//17
print(divisao_inteira)

#Contas com Variáveis 
a = 2
b = 3
print(a + b)
print(a / b) 
print(a // b) 
print(round(a / b)) #arredonda o valor 
print(b>a) #maior que 
print(b>=a) #maior ou igual a 
print(b<=a) #menor que 
print(b==a) #igual a 

print('pyton' != 'javaScript') #diferente != e essa operação compara o comprimento das palavras 