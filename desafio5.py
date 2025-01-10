# Crie um script que solicite ao usuário 2 números, e depois mostre na tela a adição, subtração, divisão, multiplicação e exponenciação deles.

# Pedindo informações ao usuário
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Armazenando informações em variáveis
adicao = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2
exponenciacao = num1 ** num2

# Printando os resultados
print(f'O resultado da adição entre {num1} e {num2} é de {adicao}.')
print(f'O resultado da subtração entre {num1} e {num2} é de {subtracao}.')
print(f'O resultado da divisão entre {num1} e {num2} é de {divisao:.0f}.') 
print(f'O resultado da multiplicação entre {num1} e {num2} é de {multiplicacao}.')
print(f'O resultado da exponenciação entre {num1} e {num2} é de {exponenciacao:.2f}.')


