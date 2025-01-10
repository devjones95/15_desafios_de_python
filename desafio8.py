'''Utilize a lista do eercício anterior, altere o segundo elemento da lista de banana para morango.
Depois adicione a fruta abacaxi ao final da lista, e por fim, imprima a lista modificada na tela'''

frutas = ['Maçã', 'Banana', 'Manga', 'Uva']

# Modificando o item Banana para Morango
frutas[1] = 'Morango' # acessamos o item da lista sempre utilizando slices ou integers e modificamos

# Adicionando Abacaxi ao FINAL da lista
frutas.append('Abacaxi') # append adiciona itens na lista

# Printando a lista modificada
print(frutas)
 
