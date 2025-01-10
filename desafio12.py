'''Crie uma lista de frutas e outra de vegetais
Use um for loop aninhado dentro de outro for loop (Nested for loop) para imprimir todas as combinações
possíveis de frutas e vegetais, com a primeira fruta e o vegetal em segundo'''

frutas = ['Maçã', 'Morango', 'Manga', 'Uva']
vegetais = ['Alface', 'Brócolis', 'Repolho', 'Couve']

for fruta in frutas:
    for vegetal in vegetais:
        print(f'{fruta} e {vegetal}')