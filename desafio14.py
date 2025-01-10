'''Crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim qie chegar a 5 usando 
o comando break. Em seguida, crie um segundo loop que imprima os números de 1 a 10, mas pule a impressão 
do número 5 usando o comando continue'''

print('Loop do Break')
for numero in range(1, 11):
    if numero > 5:
        break

    print(numero)

print('-----------------------')

print('Loop do Continue')
for numero in range(1, 11):
    if numero == 5:
         continue

    print(numero)