# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}

estudante['nome'] = input('Qual é o seu nome?')
estudante['ano_conheceu_linkekdIn'] = int(input('Em qual ano você conheceu o LinkedIn?'))
estudante['ano_atual'] = int(input('Qual é o ano atual?'))
cursos = input('Quais foram os cursos que você realizou no Linkedin Learning? (separados por vírgula)')

estudante['cursos'] = cursos.split(', ')

total_anos = estudante['ano_atual'] - estudante['ano_conheceu_linkekdIn']
total_cursos = len(estudante['cursos'])


print(f"Oi,{estudante['nome']}, desde {estudante['ano_conheceu_linkekdIn']} você conhece o Linkedin, nesses {total_anos} anos você fez {total_cursos} cursos! ")