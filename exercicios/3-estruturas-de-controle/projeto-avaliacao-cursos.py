# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos = ['python', 'Java', 'SQL', 'excel', 'PowerBi']

curso_python = 'python'
curso_java = 'Java'
curso_sql = 'SQL'

notas_curso = {}

if curso_python in cursos:
  print(f'Este curso está em nosso catálogo, dê uma nota a esse curso')
  notas_curso[curso_python] = int(input('Dê uma nota de 0 a 5 para esse curso:'))

if curso_java in cursos:
  print(f'Este curso está em nosso catálogo')
notas_curso[curso_java] = int(input('Dê uma nota de 0 a 5 para esse curso:'))

if curso_sql in cursos:
  print(f'Este curso está em nosso catálogo')  
  notas_curso[curso_sql] = int(input('Dê uma nota de 0 a 5 para esse curso:'))
  
else:
  print(f'Esse curso não faz parte do nosso catálogo')

print(notas_curso)
