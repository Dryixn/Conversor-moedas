dolar = 0
euro = 0
iene = 0
r = 's'
from time import sleep
print('=' * 80)
while True:
    print('Moedas disponíveis para conversão para real:')
    escolha = str(input('Dólar, Euro ou Iene ')).strip().upper()
    print('=' * 80)
    if escolha == 'DÓLAR' or escolha == 'DOLAR':
        dolar = float(input('Valor a ser convertido: US$'))
        print(f'O valor convertido para reais fica R${dolar*5:.2f}')
        print('=' * 80)
    elif escolha == 'EURO':
        euro = float(input('Valor a ser convertido: €'))
        print(f'O valor convertido para reais fica R${euro*5.41:.2f}')
        print('=' * 80)
    elif escolha == 'IENE':
        iene = float(input('Valor a ser convertido: ¥'))
        print(f'O valor convertido para reais fica R${iene*0.036:.2f}')
        print('=' * 80)
    else:
        print('Opção inválida. Tente novamente.')
        print('=' * 80)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'S':
        print('Ok. Qual sua escolha?')
    if r == 'N':
        print('Ok. Programa sendo finalizado.')
        sleep(3)
        break
print('=' * 80)
print('Programa finalizado.')
