# Declare 4 variáveis do tipo numérica
# Crie uma estrutura condicional para comparar dois números
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"

a = 1
b = 19
c = 30
d = 2

if (b > d) or (b > a): 
  print(f'A condição foi cumprida, {b} é maior que {d} ou {a}')

else:
  print(f'A condição não foi cumprida, o número {b} é maior que {a}')

# ~-~--~-~-~--~-~-~-~-~-~-~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~-~--~~--~-

if (d == b) and (d < a):
  print(f'A condição foi cumprida, {d} é igual a {b}')

elif d != a:
  print(f'A condição foi cumprida {d} é diferente de {a}')

else:
  print(f'Nenhuma das condições foi cumprida)')  

# ~-~-~-~-~--~-~-~-~-~-~--~-~-~-~-~-~--~-~-~-~-~-~--~-~-~-~-~--~-~-~-~-
if a < c:
  print(f'A condição se cumpriu, {a} é menor que {c}')

if c > a:
  print(f'A condição se cumpriu, {c} é maior que {a}')