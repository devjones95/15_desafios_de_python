'''Use a lista frutas do exercício anterior.
Remova a Manga da lista usando o método remove().
Depois remova o último item da lista usando o método del().
Por fim, imprima na tela a lista modificada.'''

frutas = ['Maçã', 'Morango', 'Manga', 'Uva', 'Abacaxi']

# Removendo a Manga da lista
frutas.remove('Manga')

# Removendo o último item da lista utilizando o del().
del frutas[-1]

# Printando a nova lista modificada
print(frutas)

