'''CRie uma lista de frutas com 6 frutas, onde inclua maçã 3x, e outras frutas de sua escolha.
Use um loop for para contar quantas vezes a palavra maçã aparece na lista e imprima o resultado'''

# criando a lista de frutas
frutas = ['maçã', 'maçã', 'uva', 'banana', 'maçã', 'morango']

# criando o contador
contador = 0

# adicionando o loop de repetição == maçã
for fruta in frutas:
    if fruta == 'maçã':
        contador += 1
    
# printando o resultado
print(f'Número de maçãs na lista: {contador}')