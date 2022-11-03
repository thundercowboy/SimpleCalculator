# Projeto Calculadora Simples

valor_resultado = 0
valor_resultado = float(valor_resultado)

primeiro_numero = input('Digite o primeiro valor: ')
segundo_numero = input('Digite o segundo valor: ')

if not primeiro_numero.isdigit() or not segundo_numero.isdigit():
    print('Por favor, insira um número válido.')
    exit()
else:
    ...

primeiro_numero = float(primeiro_numero)
segundo_numero = float(segundo_numero)

operacao = input('Informe a operacao: [+][-][*][/] ')

if operacao == '+':
    valor_resultado = primeiro_numero + segundo_numero
    op_usado = 'soma'
elif operacao == '-':
    valor_resultado = primeiro_numero - segundo_numero
    op_usado = 'subtração'
elif operacao == '*':
    valor_resultado = primeiro_numero * segundo_numero
    op_usado = 'multiplicação'
elif operacao == '/':
    valor_resultado = primeiro_numero / segundo_numero
    op_usado = 'divisão'
else:
    print('Insira um operador válido. ')

valor_resultado = float(valor_resultado)

print(f'O resultado da operação:', op_usado, 'entre', primeiro_numero, 'e', segundo_numero,
      'é igual a', valor_resultado)
