# Criando listas 

lista1 = [5,1,3,2,4,6,8,7,9,10]

# Alguns comandos importantes com uma nova lista

frutas = [] # A lista está vazia, existe outras maneiras de adicionar conteúdo a ela.

frutas.append("Morango") #.append pode fazer isso sem problema (append significa acrescentar)
frutas.append("Tomate") 
frutas.append("Kiwi")
# Mas como ele obedece a forma que o python lê (que é de cima pra baixo) 
# O próximo item vai aparecer em segundo e o próximo em terceiro.

frutas.insert(0,"Uva")
# Já no .insert você pode escolher onde colocar o item se colocar um numero (não se esqueça da vírgula) e o item entre aspas.
# Essa ordem se chama INDEX e veremos ele de novo justo do próximo comando.
# Colocamos a Uva no index 0 porque o python começa a contar a posição do 0. 
# Apesar do Morango ter sido lido primeiro, por causa do comando .insert, conseguimos colocar a Uva na frente.

frutas.pop(2) 
# O .pop retira da lista usando o número do index.
# No caso do python o index começa do 0 como dito anteriormente.
# Logo as posições são: Uva(0) , Morango(1) , Kiwi (2) , Tomate(saiu da lista, por que não é fruta).
#                        ^                      ^
#                        |                      |
#                por causa do insert    por causa do pop

# Mas em casos onde a lista é muito grande contar o número de posições (INDEX) não é viável. 
# Por isso se usa "frutas.index("Tomate")" para substituir o número
# Assim você não precisa ficar ocupado procurando pelo index certo. Ele já faz isso.

# EXEMPLO:
frutas.pop(frutas.index("Kiwi"))
# Agora o Kiwi não está mais na lista. (Odeio kiwi).


# Existe também uma maneira de colocar tudo em ordem alfabética ou em numérica (crescente) com o comando .sort (que significa ordenar em inglês)
frutas.sort()
# Agora a lista de frutas está em ordem alfabética.


# Com a primeira lista agora.
lista1.sort()
# Agora quando printarmos a lista começará com 1 e terminará com 10 em ordem crescente


# EXEMPLO:
lista_alunos = []

lista_alunos.append("Carlin "+"Roberts "+"Markz "+"Paulão")
lista_alunos.sort()
# Agora temos uma lista de alunos em ordem alfabética



print (frutas)
print (lista1)
print (lista_alunos)

