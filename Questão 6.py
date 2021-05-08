from time import sleep
print('''Contagem regressiva para os FOGOS!!
Digite a opção
[ 1 ] para acender''')
opção = int(input('Digite a opção: '))
if opção == 1:
    for c in range(10, -1, -1):
        sleep(0.5)
        print(c)
    print('KABUMMM!!!')