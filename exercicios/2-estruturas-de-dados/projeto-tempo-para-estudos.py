# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input ('Qual seu nome?')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias =int (input('você estuda quantos dias na semana?'))

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas =int (input('Qual sua média de horas estudadas por dia?'))

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Qual é o curso que você está fazendo?')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f'{nome} que cursa {curso} costuma estudar {total_dias} dias por semana em uma média de {total_horas} horas por dia. Sendo assim, {nome} estuda uma média de {total_horas*total_dias} horas por semana. ')
