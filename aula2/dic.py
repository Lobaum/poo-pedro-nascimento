#Estrutura composta
import random
#tupla = () # fixa
#lista = []
#dicionario = {}
# del lista - apaga a lista
# lista.insert(1, 34) - insere itens dentro da lista (primeiro numero é a posição)
# lista.clear() # Apaga o conteudo da lista

#for x in lista1:
#    for y in lista2:
#        lista3.append(x)
#        lista3.append(y)
#lista1 = [1, 2, 3]
#lista2 = ['a', 'b', 'c']
#print(lista3)

#for i in lista3:
#  print(f'{lista3[2]}')

#######################



dicionario = {'Facil': {'Monstro1': 'Lobo', 'Defesa': random.randint(5, 10), 'Poder': random.randint(3, 7)},
              'Medio': {'Nomes2': 'Rogerio', 'Idade2': 324}}
print(f'{dicionario}')
for c, v in dicionario.items():
    print(f'chave {c}, valor {v}')